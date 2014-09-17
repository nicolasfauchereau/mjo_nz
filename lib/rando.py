def rando(p):
    import numpy as np
    u = np.random.random_sample()
    i = 0.
    s = p[0]

    while ( (u > s) & (i < p.__len__())  ):
        i+=1.
        s = s + p[i]
    index = i
    return index

