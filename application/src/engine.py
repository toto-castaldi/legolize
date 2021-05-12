import traceback
import os
import utils
import time
import legolize
import palette
import csv
import color_utils
import image_output
from os import listdir
from os.path import isfile, join

logger = utils.init_log()

pal = palette.Palette()
with open("20210509-rebrickable-colors.csv") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        logger.debug(row[2])
        pal.add_color(row[0], row[1], color_utils.html_to_rgb(row[2], 255), 't' == row[3])
        
logger.info(f"palette loaded of {len(pal.colors)} colors")

def lego(uid, precision):
    lego_image = legolize.load(utils.input_name(uid), precision, precision)
    image = image_output.create_image_with_image(lego_image, pal)
    image.save(utils.output_name(uid))


while True:
    logger.debug("check for files")
    try:
        only_files = [f for f in listdir(utils.TMP_FOLDER) if isfile(join(utils.TMP_FOLDER, f))]
        for f in only_files:
            uid = utils.seed(f)
            cup_name = utils.cup_name(uid)
            if utils.is_input_file(f) and os.path.exists(cup_name):
                precision_str = ""
                with open(cup_name) as f:
                    precision_str = f.read()
                os.remove(cup_name)
                precision = int(precision_str.strip())
                logger.debug(f"{f}, {precision}")
                lego(uid, precision)

    except Exception:
        traceback.print_exc()
    
    time.sleep(10)