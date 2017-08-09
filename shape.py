from turtle import *

speed(0)
def recursiveShape(size):
    if size < 1 * 10 ** (-40):
        return 1

    pu()
    goto(0,0)
    pd()

    goto(size,0)
    goto(size,size)
    goto(0,size)
    goto(0,0)
    
    pu()
    goto(size/2,size)
    pd()
    goto(size/2,size * (3/4))
    goto(size/4,size * (3/4))
    goto(size/4,size/2)
    goto(0,size/2)
    goto(size/2,size/2)
    goto(size/2,0)
    goto(size/2,size/4)
    goto(size * (3/4),size/4)
    goto(size * (3/4),size/2)
    goto(size,size/2)
    goto(size * (3/4),size/2)
    goto(size * (3/4),size * (3/4))
    goto(size/2,size * (3/4))
    pu()
    goto(0,0)
    recursiveShape(size/2)
    

recursiveShape(500)
