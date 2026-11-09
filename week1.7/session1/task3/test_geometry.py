# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle
import pytest

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance_to(p2) == 5.0
    
    # complete the implementation for
    # testing distance_to()
    

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates

def test_circle_point_constructor():
    c = Circle(1.0)
    assert c.radius == 1.0
    assert c.centre.x == 0.0
    assert c.centre.y == 0.0

    cir = Circle(1.0, Point(1.0 , 2.0))
    assert cir.centre.x == 1.0
    assert cir.centre.y == 2.0

def test_area():
    assert Circle(1.0).area() == pytest.approx(3.1415)

def test_perimeter():
    assert Circle(1.0).perimeter() == pytest.approx(6.2831)