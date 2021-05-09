import image_utils
from PIL import Image


IMAGE_PALETTE = "lego-point.png"


class Palette:
    def __init__(self):
        self.colors = {}
        self.image_size = Image.open(IMAGE_PALETTE).size
        self.rgbs = []

    def add_color(self, id, name, rgb, is_trans):
        image = image_utils.move_image_color(IMAGE_PALETTE, rgb)
        self.colors[rgb] = (id, name, is_trans, image)
        self.rgbs.append(rgb)

    def image_palette(self, color):
        return self.colors[color][3]
