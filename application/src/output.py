import legolize
import image_utils
import color_utils
import utils
from PIL import Image


logger = utils.init_log()

def create_image_with_pixel(lego_image):
    new_image = Image.new('RGB', lego_image.new_size)
    for p in lego_image.points:
        new_image.putpixel(p[0], p[1])
    return new_image


def create(lego_image, palette, file_name, progress):
    f = open(file_name, "a")

    pixel_to_image_x = palette.image_size[0]
    pixel_to_image_y = palette.image_size[1]
    new_image = Image.new(
        'RGB', (lego_image.new_size[0] * pixel_to_image_x, lego_image.new_size[1] * pixel_to_image_y))
    count = 1
    rgbs = palette.rgbs
    l = len(lego_image.points)
    for p in lego_image.points:
        position = p[0]
        color = p[1]

        the_color_palette = color_utils.nearest(rgbs, color)
        pixel_image = palette.image_palette(the_color_palette)

        f.write(f"{position} - {the_color_palette[0]}\n")
        
        logger.info(f"{count}/{l}")
        progress(count, l)

        pixel_image_dimension_x = pixel_image.size[0]
        pixel_image_dimension_y = pixel_image.size[1]
        for x in range(pixel_image_dimension_x):
            for y in range(pixel_image_dimension_y):
                new_x = position[0] * pixel_image_dimension_x + x
                new_y = position[1] * pixel_image_dimension_y + y
                new_image.putpixel(
                    (new_x, new_y), pixel_image.getpixel((x, y)))
        count = count + 1

    f.close()


    return new_image

