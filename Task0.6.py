
def maximum(*arg1):
    element = None
    for n in arg1:
        if element is None or n > element:
            element = n

    return element

