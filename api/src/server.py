from flask import Flask, request, make_response, send_file
from flask_cors import CORS
import os
import uuid
import utils
import image_utils
import color_utils
import image_output
from multiprocessing import Process
import legolize
import palette
import csv


logger = utils.init_log()
app = Flask(__name__)
CORS(app)
TMP_FOLDER = os.environ['UPLOAD_FOLDER']
os.makedirs(TMP_FOLDER, exist_ok=True)
processes = {}
w = 20
h = 20

pal = palette.Palette()
with open("20210509-rebrickable-colors.csv") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        logger.debug(row[2])
        pal.add_color(row[0], row[1], color_utils.html_to_rgb(row[2], 255), 't' == row[3])
        
logger.info(f"palette loaded of {len(pal.colors)} colors")

def input_name(uid):
    return os.path.join(TMP_FOLDER, f"{uid}-input")

def thumb_name(uid):
    return os.path.join(TMP_FOLDER, f"{uid}-thumb.png")

def output_name(uid):
    return os.path.join(TMP_FOLDER, f"{uid}-output.png")

def lego(uid):
    lego_image = legolize.load(input_name(uid), w, h)
    image = image_output.create_image_with_image(lego_image, pal)
    image.save(output_name(uid))

@app.route('/upload', methods=['POST'])
def upload():
    uid = str(uuid.uuid4())

    file = request.files['file']

    file.save(input_name(uid))

    image = image_utils.image_thumbnail(input_name(uid))
    image.save(thumb_name(uid))

    p = Process(target=lego, args=(uid,))
    p.start()
    p.join()
    processes[uid] = p

    return make_response({'uid': uid}, 200)


@app.route('/input/<uid>', methods=['GET'])
def input(uid):
    return send_file(thumb_name(uid), mimetype='image/png')

@app.route('/output/<uid>', methods=['GET'])
def output(uid):
    return send_file(output_name(uid), mimetype='image/png')

@app.route('/outputcheck/<uid>', methods=['GET'])
def outputcheck(uid):
    finished = False
    if uid in processes:
        logger.debug(processes[uid].is_alive())
        finished = not processes[uid].is_alive()

    return make_response({'finished': finished}, 200)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
