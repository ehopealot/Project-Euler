import math, fractions



def reduce(num, denom):
    reducing = True
    divisor = min(num,denom)
#    print "reducing " + str(num) + " " + str(denom)
    while True:
        if divisor < 2: break
        if num% divisor == 0 and denom % divisor == 0:
            num /= divisor
            denom /= divisor
            divisor = min(num,denom)
        else: divisor -= 1
#    print "reduced " + str(num) + " " + str(denom)
    return num, denom

def find_period(x):
    sqrt = math.sqrt(x)
    a = math.floor(sqrt)
    #Not interested in squares
    if sqrt == a: return None
    looking_for_cycle = True
    continued_fraction = []
    seen = {}
    numerator = 1
    denominator = sqrt - a
    add_subtract_term = a
    counter = 0
    while looking_for_cycle:
        counter += 1
#        print add_subtract_term
        denominator = x - add_subtract_term**2
        numerator,denominator = reduce(numerator,denominator)
#        print numerator,denominator
        next = (numerator/denominator)*(sqrt+add_subtract_term)

        a = math.floor(next)
        numerator = denominator
        add_subtract_term = abs(add_subtract_term - numerator*a)
#        denominator = sqrt - add_subtract_term


        if (numerator,add_subtract_term) in seen: break
        seen[(numerator,add_subtract_term)] = True
        continued_fraction.append(a)
#    print continued_fraction
    return len(continued_fraction)
    
def do_64(top):
    odd = 0
    for i in range(2, top+1):
        x = find_period(i)
        if x and x%2 == 1: odd += 1
    return odd
