def AND(x, y):
    w1 = 0.5
    w2 = 0.5
    theta = 0.7
    tmp = x * w1 + y * w2

    if tmp <= theta:
        return 0
    else:
        return 1

def NAND(x, y):
    w1 = -0.5
    w2 = -0.5
    theta = -0.7
    tmp = x * w1 + y * w2

    if tmp <= theta:
        return 0
    else:
        return 1

def OR(x, y):
    w1 = 0.5
    w2 = 0.5
    theta = 0.3
    tmp = x * w1 + y * w2

    if tmp <= theta:
        return 0
    else:
        return 1

def XOR(x, y):
    s1=NAND(x, y)
    s2=OR(x, y)
    s3=AND(s1, s2)

    return y


