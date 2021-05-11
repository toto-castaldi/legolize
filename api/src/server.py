from flask import Flask, request, make_response
from flask_cors import CORS
import os
import uuid

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'UPLOAD_FOLDER'

os.makedirs(UPLOAD_FOLDER, exist_ok = True)

@app.route('/upload', methods=['POST'])
def upload():
    uid = str(uuid.uuid4())

    file = request.files['file']
    
    file.save(os.path.join('UPLOAD_FOLDER', uid))

    return make_response({ 'uid' : uid}, 200)


if __name__ == '__main__':
    app.run(port=5000, debug=True)