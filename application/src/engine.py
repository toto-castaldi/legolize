import traceback
import os
import utils
import time
import legolize
import palette
import csv
import color_utils
import output
import redis
import math
from PIL import Image
from os import listdir
from os.path import isfile, join

redis_url = os.environ.get("REDIS", "")
logger = utils.init_log()
time_to_expire_s = 2 * 3600
storage_redis = redis.Redis.from_url(redis_url, decode_responses=True)

pal = palette.Palette()
with open("20210509-rebrickable-colors.csv") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        logger.debug(row[2])
        pal.add_color(row[0], row[1], color_utils.html_to_rgb(row[2], 255), 't' == row[3])
        
logger.info(f"palette loaded of {len(pal.colors)} colors")

def progress(uid):
    def set_progess(count, total):
        storage_redis.set(uid, math.ceil(count / total * 100), ex=time_to_expire_s)
    return set_progess

def lego(uid, size):
    output_file_name = utils.output_name(uid)

    if os.path.exists(output_file_name):
        os.remove(output_file_name)

    image_file = utils.input_name(uid)
    image = Image.open(image_file)
    max_len = image.size[0] if image.size[0] > image.size[1] else image.size[1]
    step = max_len // size

    lego_image = legolize.load_from_image(image, step, step)
    image = output.create(lego_image, pal, utils.point_name(uid), progress(uid))
    image.save(output_file_name)


while True:
    logger.debug("check for files")
    try:
        only_files = [f for f in listdir(utils.TMP_FOLDER) if isfile(join(utils.TMP_FOLDER, f))]
        for f in only_files:
            uid = utils.seed(f)
            cup_name = utils.cup_name(uid)
            if utils.is_input_file(f) and os.path.exists(cup_name):
                size_str = ""
                with open(cup_name) as f:
                    size_str = f.read()
                os.remove(cup_name)
                size = int(size_str.strip())
                logger.debug(f"{uid}, {size}")
                lego(uid, size)

    except Exception:
        traceback.print_exc()
    
    time.sleep(10)