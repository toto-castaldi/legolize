from flask import Flask, request, make_response
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'UPLOAD_FOLDER'

os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join('UPLOAD_FOLDER', filename))

    return make_response({}, 200)


if __name__ == '__main__':
    app.run(port=5000, debug=True)