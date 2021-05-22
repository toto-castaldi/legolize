from flask import Flask, request, make_response, send_file
from flask_cors import CORS
from flask_sock import Sock
import os
import uuid
import utils
import image_utils
import json
from PIL import Image
import traceback
import legolize
import palette
import base64
from io import BytesIO
import simple_websocket


logger = utils.init_log()
app = Flask(__name__)
CORS(app)
HOST = os.environ['HOST']
DEBUG = os.environ.get('DEBUG', 'False')
sock = Sock(app)

pal = palette.Palette()
        
logger.info(f"palette loaded of {len(pal.colors)} colors")

@app.route('/upload/<size>', methods=['POST'])
def upload(size):
    uid = str(uuid.uuid4())
    input_name = utils.input_name(uid)

    file = request.files['file']

    file.save(input_name)

    image = image_utils.image_thumbnail(input_name)
    image.save(utils.thumb_name(uid))

    image = image_utils.image_thumbnail(input_name, MAX_SIZE=(int(size), int(size)))
    image.save(utils.waiting_name(uid))

    logger.debug(f"saved thumbnails")

    return make_response({'uid': uid}, 200)

@sock.route('/fullgenerate')
def full_gen(ws):
    while True:
        try:
            req_json = json.loads(ws.receive())

            uid = req_json['uid']
            size = int(req_json['size'])

            logger.debug(f"uid {uid} size {size}")

            image = legolize.image(utils.input_name(uid))

            max_len = legolize.max_len(image)

            logger.debug(f"max_len {max_len}")

            step = max_len // size

            def generating_events_new_size(new_size):
                ws.send(json.dumps({'action' : 'size', 'w': new_size[0], 'h': new_size[1]}))

            def generating_events_point(point):
                ws.send(json.dumps({'action' : 'point', 'x': point[0][0], 'y': point[0][1], 'color' : point[1]}))

            def generating_events_palette(point):
                try:
                    buffered = BytesIO()
                    image = point[2]
                    image.save(buffered, format='PNG')
                    img_str = base64.b64encode(buffered.getvalue()).decode('ascii')
                    ws.send(json.dumps({'action' : 'palette', 'x': point[0][0], 'y': point[0][1], 'color' : point[1], 'palette_id' : point[3], 'palette_img' : img_str}))
                except Exception:
                    traceback.print_exc()

            def generating_events_pieces(position, size, color):
                try:
                    ws.send(json.dumps({'action' : 'piece', 'position': position, 'size': size, 'color' : color}))
                except Exception:
                    traceback.print_exc()

            generating_events = {}
            generating_events['new_size'] = generating_events_new_size
            generating_events['point'] = generating_events_point
            generating_events['apply_palette'] = generating_events_palette
            generating_events['pieces'] = generating_events_pieces

            lego_image = legolize.load(image, step, step, generating_events)

            lego_image.apply_palette(pal, generating_events)

            ws.send(json.dumps({'action' : 'endPalette'}))

            lego_image.pieces(pal, generating_events)          

            ws.send(json.dumps({'action' : 'endPiece'}))
        except simple_websocket.ws.ConnectionClosed:
            pass
        except Exception:
            traceback.print_exc()


@app.route('/thumbnail/<uid>', methods=['GET'])
def thumbnail(uid):
    return send_file(utils.thumb_name(uid), mimetype='image/png')

@app.route('/waiting/<uid>', methods=['GET'])
def waiting(uid):
    return send_file(utils.waiting_name(uid), mimetype='image/png')

if __name__ == '__main__':
    logger.info("flask booting up")
    app.run(port=5000, debug=DEBUG == 'True', host=HOST)
