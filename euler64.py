import math, time

def reduce(num, denom):
    reducing = True
    divisor = min(num,denom)
#    print "reducing " + str(num) + " " + str(denom)
    a, b, t = num,denom,0
    while b!=0:
        t = b
        b = a%b
        a = t
    return num/a,denom/a
    return num, denom

def find_period(x):
    sqrt = math.sqrt(x)
    a = math.floor(sqrt)
    #Not interested in squares
    if sqrt == a: return None
    continued_fraction = []
    seen = {}
    numerator = 1
    add_subtract_term = a
    while True:
        denominator = x - add_subtract_term**2
        numerator,denominator = reduce(numerator,denominator)
        next = (numerator/denominator)*(sqrt+add_subtract_term)
        a = math.floor(next)
        numerator = denominator
        add_subtract_term = abs(add_subtract_term - numerator*a)
        if (numerator,add_subtract_term) in seen: 
            break
        seen[(numerator,add_subtract_term)] = True
        continued_fraction.append(a)
    return len(continued_fraction)
    
def do_64(top):
    odd = 0
    start = time.time()
    for i in range(2, top+1):
        x = find_period(i)
        if x and x%2 == 1: odd += 1
    print time.time() - start
    return odd
