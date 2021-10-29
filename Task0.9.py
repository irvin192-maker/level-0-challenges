def letters(par):
    vowels = "aeiou"
    string = par.lower()
    seq = []
    comma = ','
    for v in vowels:
        if v in string:
            seq.append(v)

    print("Vowels:", comma.join(seq))
    return




