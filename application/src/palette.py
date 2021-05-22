from PIL import Image
import image_utils
import csv
import color_utils

IMAGE_PALETTE = "lego-point.png"


class Palette:
    def __init__(self, COMPUTE_IMAGE = False):
        self.colors = {}
        self.rgbs = []

        self._image_size = Image.open(IMAGE_PALETTE).size if COMPUTE_IMAGE else None
        self._id_2_rgb = {}
        with open("20210509-rebrickable-colors.csv") as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                self._add_color(int(row[0]), row[1], color_utils.html_to_rgb(row[2], 255), 't' == row[3], COMPUTE_IMAGE)

    def _add_color(self, id, name, rgb, is_trans, compute_image):
        image = image_utils.move_image_color(IMAGE_PALETTE, rgb) if compute_image else None
        self.colors[rgb] = (id, name, is_trans, image)
        self._id_2_rgb[id] = rgb
        self.rgbs.append(rgb)

    def image_palette(self, color):
        return self.colors[color][3]

    def id_palette(self, color):
        return self.colors[color][0]

    def id_to_rgb(self, id):
        return self._id_2_rgb[id]
