def area_tri(a, b, c):
    s = 1/2 * (a + b + c)
    h = ((s - a) * (s - b) * (s - c) * s) ** (1/2)
    return h



