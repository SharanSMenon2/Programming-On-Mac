import math
from functools import reduce


def add(a, b): return a + b


def subtract(a, b): return a - b


def info1(grp, rows):
    finalList = []
    for value in grp:
        app = abs(math.log(value/rows, 2) * (value/rows))
        finalList.append(app)
    return reduce(add, finalList)


def info2(rows, group):
    finalValues = []
    for values in group:
        sm = reduce(add, values)
        lst = []
        for value in values:
            vl = math.log(value/sm, 2) * value/sm
            lst.append(abs(vl))
            # print(vl)
        finalValues.append(reduce(add, lst)*(sm/rows))
    return reduce(add, finalValues)


def gain(rows, group1, group2):
    print("Info 1: "+str(info1(group1, rows)))
    print("Info 2: "+str(info2(rows, group2)))
    return info1(group1, rows) - info2(rows, group2)


print(gain(8, [5, 3], [[2, 1],[3],[2]]))
