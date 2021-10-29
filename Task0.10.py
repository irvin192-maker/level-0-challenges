def common(par, par2):
    one = par.lower()
    two = par2.lower()
    seq = []
    com = ','
    for o in one:
        if o in two:
            seq.append(o)
    print("Common letters:", com.join(seq))





