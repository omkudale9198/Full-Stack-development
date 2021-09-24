def circle(r):
    area=3.14*(r**2)
    return area

def rect(l,w):
    area=l*w
    return area

def square(l):
    area=l*l
    return area

cir=circle(2)
print("Area of circle:", cir)

rec=rect(5,2)
print("Area of Rectangle:", rec)

sq=square(9)
print("Area of Square:", sq)