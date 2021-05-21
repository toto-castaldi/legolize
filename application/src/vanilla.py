def pieces(points_on_palette):
    res = {}
    for color, positions in points_on_palette.items():
        for pos in positions:
            key = (1, 1, color)
            if key not in res:
                res[key] = []
            res[key].append((pos[1], pos[0]))
    return (None, res)