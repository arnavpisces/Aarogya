import math, random, operator
from math import atan2
from functools import reduce

coords=[]
for i in range(10):
    r = float(2500/111300)
    y0 = 28.635901
    x0 = 77.201854
    u = random.uniform(0, 1)+1
    v = random.uniform(0, 1)+1
    w = r * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y1 = w * math.sin(t)
    x1 = x / math.cos(y0)
    newY = y0 + y1
    newX = x0 + x1
    coords.append([newX,newY])

center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), coords), [len(coords)] * 2))
sortedcor=sorted(coords, key=lambda coords: (-135 - math.degrees(math.atan2(*tuple(map(operator.sub, coords, center))[::-1]))) % 360)
sortedcor.append(sortedcor[0])
print(sortedcor)

    