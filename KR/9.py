for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if ((x <= y) and (y == z) and (z or w)) == 1:
                    print(w, z, x, y)
