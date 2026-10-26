# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """
    
    # Add constructor here
    def __init__(self,x,y):
        '''
        Creates a point, given x and y coordinates. 
        '''
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self,x,y):
        '''
        returns distance from origin
        '''
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    def distance_to(self, point):
        '''
        returns distance from this point to the specified point.
        '''
        return math.hypot(self.x - point.x, self.y - point.y)
    
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point

p = Point(1.5, 4.2)
q = Point(3.7, 2.6)

print(p.distance_to(q))