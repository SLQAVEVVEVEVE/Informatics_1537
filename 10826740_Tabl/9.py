for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(y <= (x == w)) and (z <= x):
                    print(x, y, z, w)