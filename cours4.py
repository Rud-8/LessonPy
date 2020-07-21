
def maximum(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a or b



def absolu(x):
    if x < 0:
        print (abs(x))
    else:
        print (x)
    return x

absolu(-12)