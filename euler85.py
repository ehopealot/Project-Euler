import math, time


answer = 10000
coordinates = ()

def run(max_width, max_height):
   global answer, coordinates

   for width in range(1, max_width+1):
#        if width%25 == 0: print "%i" % (width)
       w = float(width)
       if w == 4: print across
       across = width*(width+1)/2
#        across = sum(width-x+1 for x in xrange(1, width+1))
       for height in range(1, max_height+1):
           rectangles = across*((height*(height+1))/2)
           new_answer = abs(2000000-rectangles)
           if new_answer < answer:
               answer = new_answer
               coordinates = (width,height)
#            print width,height,rectangles
   print reduce(lambda x,y: x*y, coordinates, 1), coordinates



if __name__ == "__main__":
    s = time.time()
    run(100,100)
    print time.time() - s
