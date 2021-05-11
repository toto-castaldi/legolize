from flask import Flask, request, make_response, send_file
from flask_cors import CORS
import os
import uuid
import utils

logger = utils.init_log()


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.environ['UPLOAD_FOLDER']

os.makedirs(UPLOAD_FOLDER, exist_ok = True)

@app.route('/upload', methods=['POST'])
def upload():
    uid = str(uuid.uuid4())

    file = request.files['file']
    
    logger.debug(os.path.join(UPLOAD_FOLDER, uid))

    file.save(os.path.join(UPLOAD_FOLDER, uid))

    return make_response({ 'uid' : uid}, 200)

@app.route('/input/<uid>', methods=['GET'])
def input(uid):
    filename = os.path.join(UPLOAD_FOLDER, uid)

    logger.debug(filename)

    return send_file(filename, mimetype='image/gif')


if __name__ == '__main__':
    app.run(port=5000, debug=True)