def pieces(points_on_palette):
    res = []
    for p in points_on_palette:
        res.append((p[0], (1,1), p[2]))
    return res