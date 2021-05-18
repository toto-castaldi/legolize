from flask import Flask, request, make_response, send_file
from flask_cors import CORS
from flask_sock import Sock
import os
import uuid
import utils
import image_utils
import json
from PIL import Image
import color_utils
import traceback
import legolize
import time
import palette
import csv
import base64
from io import BytesIO


logger = utils.init_log()
app = Flask(__name__)
CORS(app)
HOST = os.environ['HOST']
DEBUG = os.environ.get('DEBUG', 'False')
sock = Sock(app)

pal = palette.Palette()
with open("20210509-rebrickable-colors.csv") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        logger.debug(row[2])
        pal.add_color(row[0], row[1], color_utils.html_to_rgb(row[2], 255), 't' == row[3])
        
logger.info(f"palette loaded of {len(pal.colors)} colors")

@app.route('/upload', methods=['POST'])
def upload():
    uid = str(uuid.uuid4())

    file = request.files['file']

    file.save(utils.input_name(uid))

    image = image_utils.image_thumbnail(utils.input_name(uid))
    image.save(utils.thumb_name(uid))

    logger.debug(f"saved {utils.thumb_name(uid)}")

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

            generating_events = {}
            generating_events['new_size'] = generating_events_new_size
            generating_events['point'] = generating_events_point
            generating_events['apply_palette'] = generating_events_palette

            lego_image = legolize.load(image, step, step, generating_events)

            legolize.apply_palette(lego_image, pal, generating_events)

            ws.send(json.dumps({'action' : 'end'}))

        except simple_websocket.ws.ConnectionClosed:
            pass
        except Exception:
            traceback.print_exc()

        

@app.route('/generate', methods=['POST'])
def generate():
    size = request.json['size']
    uid = request.json['uid']

    cup_file_name = utils.cup_name(uid)
    if os.path.exists(cup_file_name):
        os.remove(cup_file_name)

    if os.path.exists(utils.output_name(uid)):
        os.remove(utils.output_name(uid))
    if os.path.exists(utils.point_name(uid)):
        os.remove(utils.point_name(uid))

    cup = open(cup_file_name, "a")
    cup.write(str(size))
    cup.close()

    return make_response({'uid': uid}, 200)


@app.route('/input/<uid>', methods=['GET'])
def input(uid):
    return send_file(utils.thumb_name(uid), mimetype='image/png')

@app.route('/output/<uid>', methods=['GET'])
def output(uid):
    name = utils.output_name(uid)
    if os.path.exists(name):
        return send_file(name, mimetype='image/png')
    else:
        return make_response({}, 404)

@app.route('/points/<uid>', methods=['GET'])
def points(uid):
    name = utils.point_name(uid)
    if os.path.exists(name):
        return send_file(name, mimetype='text/plain')
    else:
        return make_response({}, 404)

if __name__ == '__main__':
    logger.info("flask booting up")
    app.run(port=5000, debug=DEBUG == 'True', host=HOST)
