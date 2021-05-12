import time
import sys
import utils
import legolize
import image_output
import palette
import csv
import color_utils

logger = utils.init_log()

def cli():
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    image_file_name  = None
    w = 10
    h = 10

    for opt in enumerate(opts):
        if "-f" == opt[1]:
            image_file_name = args[opt[0]]
        if "-w" == opt[1]:
            w = int(args[opt[0]])
        if "-h" == opt[1]:
            h = int(args[opt[0]])
        
    if image_file_name is None:
        raise SystemExit(f"Usage: {sys.argv[0]} -f [image_file_name]")

    logger.info(f"{image_file_name} {w} {h}")

    p = palette.Palette()
    with open("20210509-rebrickable-colors.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            logger.debug(row[2])
            p.add_color(row[0], row[1], color_utils.html_to_rgb(row[2], 255), 't' == row[3])
            
    logger.info(f"palette loaded of {len(p.colors)} colors")

    lego_image = legolize.load(image_file_name, w, h)
    image = image_output.create_image_with_image(lego_image, p)
    image.save("output.png")

    

if __name__ == "__main__":
    cli()