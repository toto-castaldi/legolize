import image_utils
from PIL import Image


IMAGE_PALETTE = "lego-point.png"


class Palette:
    def __init__(self):
        self.colors = {}
        self.image_size = Image.open(IMAGE_PALETTE).size
        self.rgbs = []
        self.id_2_rgb = {}

    def add_color(self, id, name, rgb, is_trans):
        image = image_utils.move_image_color(IMAGE_PALETTE, rgb)
        self.colors[rgb] = (id, name, is_trans, image)
        self.id_2_rgb[id] = rgb
        self.rgbs.append(rgb)

    def image_palette(self, color):
        return self.colors[color][3]

    def id_palette(self, color):
        return self.colors[color][0]

    def id_to_rgb(self, id):
        return self.id_2_rgb[id]
