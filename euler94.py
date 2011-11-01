# Pythagorean triples: m^2 - n^2 : 2*m*n : m^2 + n^2
import math

def do_94():

    top = 167000000
    result = 0
    counter = 0
    smaller = True
    for a in xrange(3, top):
        if a% 10000000 == 0: print a
        c = a*2-1
        b_squared = c**2 - a**2
        b = math.sqrt(b_squared)
        if b%1 == 0:
            print a*2, c, c
            result += a*2 + c*2
        else:
            c = a*2+1
            b_squared = c**2 - a**2
            b = math.sqrt(b_squared)
            if b%1 ==0:
                print a*2, c, c
                result += a*2 + c*2
                          
        
    return result
