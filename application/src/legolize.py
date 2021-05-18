from traceback import print_stack
from PIL import Image
import utils
import color_utils

logger = utils.init_log()

class Lego_Image:
    def __init__(self, w, h, original_size, new_size, points):
        self.w = w
        self.h = h
        self.original_size = original_size
        self.new_size = new_size
        self.points = points


def image(image_file_name):
    return Image.open(image_file_name)

def max_len(image):
    return image.size[0] if image.size[0] > image.size[1] else image.size[1]

def load(image, w, h, generating_events):
    logger.debug("aaaaa")
    logger.debug(f"{image.format}, {image.size}, {image.mode}")
    
    new_size = (image.size[0] // w, image.size[1] // h)
    logger.debug(f"new size {new_size}")
    generating_events['new_size'](new_size)
    points = []
    new_y = 0
    for y in range(h // 2, image.size[1], h):
        new_x = 0
        for x in range(w // 2, image.size[0], w):
            (left, upper, right, lower) = (x - w // 2, y - h // 2, x + w // 2, y + h // 2)
            crop = image.crop((left, upper, right, lower))
            pixel = color_utils.mean(crop)
            if new_x < new_size[0] and new_y < new_size[1]:
                point = ((new_x, new_y), pixel)
                generating_events['point'](point)
                points.append(point)
            new_x = new_x + 1
        new_y = new_y + 1

    return Lego_Image(w, h, image.size, new_size, points)
