from math import sin, cos, pi


def convertToRad(a):
    return a / 180 * pi


def isAngleNotToleranceForF1(a):
    return a % 180 == 0 and (a / 180) % 2 != 0


def f1(a):
    num = sin(2 * a) + sin(5 * a) - sin(3 * a)
    denom = cos(a) + 1 - 2 * sin(2 * a) * sin(2 * a)

    return num / denom


def f2(a):
    return 2 * sin(a)


values = []

with open("lab1.txt", "r") as f:
    for line in f.readlines():
        for value in line.split(' '):
            values.append(float(value))

for a in values:
    x = convertToRad(a)

    if (isAngleNotToleranceForF1(a)):
        print('{0} is not tolerance for f1'.format(a))
    else:
        print('f1({0}) = {1}'.format(a, f1(x)))

    print('f2({0}) = {1}\n\n'.format(a, f2(x)))
