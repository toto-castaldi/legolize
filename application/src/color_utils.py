import math
from traceback import print_stack


def html_to_rgb(html_code, alpha=None):
    r = int(html_code[0:2], 16)
    g = int(html_code[2:4], 16)
    b = int(html_code[4:6], 16)
    a = alpha if alpha else 255

    return (r, g, b, a)


def distance(colorA, colorB):
    a = 255
    if len(colorA) > 3 and len(colorB) > 3:
        a = colorA[3] - colorB[3]

    return (colorA[0] - colorB[0], colorA[1] - colorB[1], colorA[2] - colorB[2], a)


def vector_distance(colorA, colorB):
    d = distance(colorA, colorB)
    return math.sqrt(d[0] ** 2 + d[1] ** 2 + d[2] ** 2)

def limit(i, min, max):
    i = i if i > 0 else 0
    i = i if i < 256 else 255
    return i


def move(color, distance):
    r = color[0] + distance[0]
    g = color[1] + distance[1]
    b = color[2] + distance[2]
    a = color[3] + distance[3]
    r = limit(r, 0, 255)
    g = limit(g, 0, 255)
    b = limit(b, 0, 255)
    a = limit(a, 0, 255)
    return (r, g, b, a)


def mean(image):
    r = 0
    g = 0
    b = 0
    a = 0
    count = 0
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            pixel = image.getpixel((x, y))
            r = r + pixel[0]
            g = g + pixel[1]
            b = b + pixel[2]
            a = a + (pixel[3] if len(pixel) > 3 else 255)
            count = count + 1
    return (r // count, g // count, b // count, a // count)


def nearest(colors, color):
    result = None
    min_dist = None
    for c in colors:
        d = vector_distance(c, color)
        if min_dist is None or d < min_dist:
            min_dist = d
            result = c
    return result
