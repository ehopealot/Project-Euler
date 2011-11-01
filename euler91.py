from sets import Set
from fractions import Fraction


m = 50


points = Set()
for y in range(m, 0, -1):
    for x in range(1, m+1):
        points.add((0,y,x,0))

for y in range(m, 0, -1):
    for x in range(m, 0, -1):
        points.add((x,y,x,0))

for y in range(m, 0, -1):
    for x in range(1, m+1):
        points.add((0,y,x,y))


for y in range(m, 0, -1):
    for x in range(0, m+1):
        print x,y
        slope = Fraction(-x,y)
        print x,y,slope
        other_y = y
        for other_x in range(x+1, m+1):
            other_y += slope
            if other_y < 0: break
            if other_y % 1 == 0:
                points.add((x,y,other_x,other_y))
        other_y = y

        for other_x in range(x-1, -1, -1):
            other_y -= slope
            if other_y > m: break
            if other_y %1 == 0:
                points.add((x,y,other_x,other_y))



print  len(points)
