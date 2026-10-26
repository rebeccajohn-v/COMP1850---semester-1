# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

class Point:
    """
    A Point in 2D space.
    """
    def __init__(self,x,y):
        '''
        Creates a point, given x and y coordinates. 
        '''
        self.x = x
        self.y = y


    def distance(self,x,y):
        '''
        returns distance from origin
        '''
        return math.hypot(self.x, self.y)

    
    def distance_to(self, point):
        '''
        returns distance from this point to the specified point.
        '''
        return math.hypot(self.x - point.x, self.y - point.y)
    

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle


class Circle:
    '''
    A circle with radius and centre coordinates.
    '''
    def __init__(self, radius, centre = (0.0, 0.0)):
        '''
        creates circle with given radius and centre coordinates.
        centre corordinates default to (0,0)
        '''
        self.centre = centre
        self.radius = radius

    def area(self):
        '''
        returns area of circle.
        '''
        return math.pi * self.radius * self.radius

    def perimeter(self):
        '''
        returns perimeter/ circumference of circle.
        '''
        return 2 * math.pi * self.radius

        
# Don't add any testing code to this file!
