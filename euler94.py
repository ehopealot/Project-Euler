# b = a+-1
# c = a
# A = (1/2)*sqrt(a^4-()(2a^2 - (a-1)^2)/2)
#
#

import math

def do_94():

#    top = 167000000
    top = 10000
    result = 0
    counter = 0
    smaller = True

    for c in xrange(5,top):
        if c%10000000 == 0 : print c
        if c%2 == 0: continue

        a = .5
        if (c-1)%4 == 0:
            a = ((c-1)/4)*math.sqrt((3*c-1)*(c+1))

        if a%1 == 0:
 
            print c, c, c-1
            result += c-1+c+c

#           print b, c, c
        a = .5
        if (c+1)%4 == 0:
            a = ((c+1)/4)*math.sqrt((3*c+1)*(c-1))
        if a%1 == 0:
 
            print c, c, c+1
            result += c+c+c+1
    return result

#     for a in xrange(3, top):
#         if a% 10000000 == 0: print a
#         c = a*2-1
#         b_squared = c**2 - a**2
#         b = math.sqrt(b_squared)
#         if b % 1 == 0:
#             print a*2, c, c, a*2+c*2
#             result += a*2 + c*2
#         else:
#             c = a*2+1
#             b_squared = c**2 - a**2
#             b = math.sqrt(b_squared)
#             if b % 1 == 0:
#                 print a*2, c, c, a*2 + c*2
#                 result += a*2 + c*2
                          
        
    return result
