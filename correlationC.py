import math
from functools import reduce
add = lambda x, y: x + y
def correlation(l1,l2):
    xmean = reduce(add, l1)/len(l1)
    ymean = reduce(add, l2)/len(l2)
    xlist = [x-xmean for x in l1]
    xsql = [x**2 for x in xlist]
    ylist = [y-ymean for y in l2]
    ysql = [y**2 for y in ylist]
    xylist = [x*y for (x,y) in zip(xlist,ylist)]
    top = reduce(add, xylist)
    # print(top)
    bottom1 = reduce(add, ysql)
    bottom2 = reduce(add, xsql)
    bottom = math.sqrt(bottom1*bottom2)
    print(bottom)
    return top/bottom
print(correlation([6.9,6.7,6.9,5.8,6.8],[3.1,3.1,3.1,2.7,3.2]))
