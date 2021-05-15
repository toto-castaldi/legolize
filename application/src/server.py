from flask import Flask, request, make_response, send_file
from flask_cors import CORS
import os
import uuid
import utils
import image_utils


logger = utils.init_log()
app = Flask(__name__)
CORS(app)
HOST = os.environ['HOST']
DEBUG = os.environ.get('DEBUG', 'False')

@app.route('/upload', methods=['POST'])
def upload():
    uid = str(uuid.uuid4())

    file = request.files['file']

    file.save(utils.input_name(uid))

    image = image_utils.image_thumbnail(utils.input_name(uid))
    image.save(utils.thumb_name(uid))

    logger.debug(f"saved {utils.thumb_name(uid)}")

    return make_response({'uid': uid}, 200)

@app.route('/generate', methods=['POST'])
def generate():
    size = request.json['size']
    uid = request.json['uid']

    cup_file_name = utils.cup_name(uid)
    if os.path.exists(cup_file_name):
        os.remove(cup_file_name)

    if os.path.exists(utils.output_name(uid)):
        os.remove(utils.output_name(uid))

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

@app.route('/outputcheck/<uid>', methods=['GET'])
def outputcheck(uid):
    name = utils.output_name(uid)
    return make_response({'finished': os.path.exists(name)}, 200)

if __name__ == '__main__':
    logger.info("flask booting up")
    app.run(port=5000, debug=DEBUG == 'True', host=HOST)
