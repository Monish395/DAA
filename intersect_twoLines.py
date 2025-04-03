# import numpy as np

# a = np.array([1,2])
# b = np.array([3,3])
# c= np.array([0,2.5])

# cross = np.cross((a-c),(b-c))
# print(cross)
class point:
    def __init__(self,x,y):
        self.x = x
        self.y=y

def direction(p1,p2,p3):
    x1 = (p2.x-p1.x)
    x2 = (p3.x-p1.x)
    y1 = (p2.y-p1.y)
    y2 = (p3.y-p1.y)
    return (x1*y2 - x2*y1)

def onsegment(p1,p2,p3):
    if(((p3.x >= min(p1.x,p2.x))and (p3.x <= max(p1.x,p2.x))) and ((p3.y >= min(p1.y,p2.y))and (p3.y <= max(p1.y,p2.y)))):
        return True
    else :
        return False

def intersect(p1,p2,p3,p4):
    d1 = direction(p3,p4,p1)
    d2 = direction(p3,p4,p2)
    d3 = direction(p1,p2,p3)
    d4 = direction(p1,p2,p4)

    if(((d1>0 and d2<0) or (d1<0 and d2>0))and((d3>0 and d4<0) or (d3<0 and d4>0))):
        return True
    elif d1==0 and onsegment(p3,p4,p1):
        return True
    elif d2==0 and onsegment(p3,p4,p2):
        return True
    elif d3==0 and onsegment(p1,p2,p3):
        return True
    elif d4==0 and onsegment(p1,p2,p4):
        return True
    else:
        return False

p1 = point(1,2)
p2 = point(3,3)
p3 = point(0,2.5)
p4 = point(1,2)

print(intersect(p1,p2,p3,p4))


