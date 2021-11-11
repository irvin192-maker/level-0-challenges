def time(val):
    floor = val // 60
    mod = val % 60
    if floor == 1 and mod == 1:
        print(str(floor) + ' hour', str(mod) + ' minute')
    elif floor > 1 and mod > 1:
        print(str(floor) + ' hours', str(mod) + ' minutes')
    elif floor == 1 and mod > 1:
        print(str(floor) + ' hour', str(mod) + ' minutes')
    elif mod == 0 and floor == 1:
        print(str(floor) + ' hour')
    elif mod == 0 and floor > 1:
        print(str(floor) + ' hours')
    elif mod == 1 and floor > 1:
        print(str(floor) + ' hours', str(mod) + ' minute')
    elif mod == 1 and floor < 1:
        print(f'{mod} minute')
    elif mod > 1:
        print(f'{mod} minutes')
