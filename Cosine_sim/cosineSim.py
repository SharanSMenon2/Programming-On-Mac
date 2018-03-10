from functools import reduce
import math
add = lambda x,y: x + y
cosSim = lambda l1, l2:round(reduce(add,[l1[i] * l2[i] for i in range(len(l1))])/(math.sqrt(reduce(add,[x**2 for x in l1])) * math.sqrt(reduce(add,[x**2 for x in l2]))),2)
l1 = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0]
l2 = [1,1,0,0,1,0,0,0,1,0,0,0,1,1,1,1]
print(cosSim(l1,l2))
