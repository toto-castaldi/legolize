import image_utils
import legolize
import palette
import json


input_image = "smiling-emoji.jpg"
size = 20
print_backgrounds = False


thumbnail_image = "demo-thumbnail.png"
palette_point_file = "demo-palette-points.json"
css_palette = "palette.css"

pal = palette.Palette()

image = image_utils.image_thumbnail(input_image, (300, 300))
image.save(thumbnail_image)

image = legolize.image(input_image)
max_len = legolize.max_len(image)

step = max_len // size

palette_point = []

new_size = None

def generating_events_new_size(ns):
    global new_size
    new_size = ns

def generating_events_point(point):
    pass #print(point)

def generating_events_palette(point):
    palette_point.append({
        "pos" : {
            "x" : point[0][0],
            "y" : point[0][1]
        },
        "color" : {
            "r" : point[1][0],
            "g" : point[1][1],
            "b" : point[1][2],
            "a" : point[1][3]
        },
        "colorId" : point[3]
    })

def generating_events_pieces(position, size, color):
    pass #print(position, size, color)

generating_events = {}
generating_events['new_size'] = generating_events_new_size
generating_events['point'] = generating_events_point
generating_events['apply_palette'] = generating_events_palette
generating_events['pieces'] = generating_events_pieces

lego_image = legolize.load(image, step, step, generating_events)
lego_image.apply_palette(pal, generating_events)
lego_image.pieces(pal, generating_events)

with open(palette_point_file, 'w') as outfile:
    json.dump({ "h" : new_size[0], "w": new_size[1], "points" : palette_point}, outfile)

with open(css_palette, 'w') as outfile:
    for rgb in pal.rgbs:
        id = pal.id_palette(rgb)
        if print_backgrounds:
            image = pal.image_palette(rgb)
            image.save(f"pal-color-{id}.png")
        outfile.write(f'''
div.palette-{id} {{ 
    background-image: url("../images/pal-color-{id}.png");
}}

        '''
        )
        
