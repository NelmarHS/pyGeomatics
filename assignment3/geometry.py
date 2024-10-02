# GEO1000 - Assignment 3
# Authors:
# Studentnumbers:

import math

# __all__ leaves out _test method and only makes
# the classes available for "from geometry import *":
__all__ = ["Point", "Circle", "Rectangle"]


class Point:

    def __init__(self, x, y):
        """Constructor. 
        Takes the x and y coordinates to define the Point instance.
        """
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        """Returns WKT String "POINT (x y)".
        """
        return f"POINT ({self.x} {self.y})"

    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.

        other - Point, Circle or Rectangle

        returns - True / False
        """
        if isinstance(other, Point):
            # If coordinates collide, the points are on top of eachother
            return self.x == other.x and self.y == other.y
        elif isinstance(other, Circle):
            # Find distance between point and center by Pythagoras, if distance <= radius, they collide
            dx = self.x - other.center.x
            dy = self.y - other.center.y
            distance_point_center = math.sqrt(dx ** 2 + dy ** 2)
            return distance_point_center <= other.radius
        elif isinstance(other, Rectangle):
            # Find the boundaries by finding min/max x and y, then, when point coordinates are within min/max x y
            # the point and rectangle collide
            x_min = min(other.ll.x, other.ur.x)
            x_max = max(other.ll.x, other.ur.x)
            y_min = min(other.ll.y, other.ur.y)
            y_max = max(other.ll.y, other.ur.y)
            return x_min <= self.x <= x_max and y_min <= self.y <= y_max
        else:
            return False

    def distance(self, other):
        """Returns cartesian distance between self and other Point
        """
        dx = self.x - other.x
        dy = self.y - other.y
        distance_points = math.sqrt(dx ** 2 + dy ** 2)
        return distance_points


class Circle:

    def __init__(self, center, radius):
        """Constructor. 
        Takes the center point and radius defining the Circle.
        """
        assert radius > 0
        assert isinstance(center, Point)
        self.center = center
        self.radius = float(radius)

    def __str__(self):
        """Returns WKT str, discretizing the boundary of the circle 
        into straight line segments
        """
        N = 400
        step = 2 * math.pi / N
        pts = []
        for i in range(N):
            pts.append(Point(self.center.x + math.cos(i * step) * self.radius,
                             self.center.y + math.sin(i * step) * self.radius))
        pts.append(pts[0])
        coordinates = ["{0} {1}".format(pt.x, pt.y) for pt in pts]
        coordinates = ", ".join(coordinates)
        return "POLYGON (({0}))".format(coordinates)

    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.

        other - Point, Circle or Rectangle

        Returns - True / False
        """
        if isinstance(other, Point):
            # Make use of symmetry (point vs. circle = circle vs. point)
            # self = circle, other = point
            return other.intersects(self)
        elif isinstance(other, Circle):
            # Two circles collide if the distance between centers is less than or equal to sum of radi
            dx = other.center.x - self.center.x
            dy = other.center.y - self.center.y
            distance_centers = math.sqrt(dx ** 2 + dy ** 2)
            return distance_centers <= (self.radius + other.radius)
        elif isinstance(other, Rectangle):
            # Circle collides with rectangle if the closest point on the rectangle to the circle center
            # is within the circle radius
            closest_x = max(other.ll.x, min(self.center.x, other.ur.x))
            closest_y = max(other.ll.y, min(self.center.y, other.ur.y))
            dx = closest_x - self.center.x
            dy = closest_y - self.center.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            return distance <= self.radius
        else:
            return False



class Rectangle:

    def __init__(self, pt_ll, pt_ur):
        """Constructor. 
        Takes the lower left and upper right point defining the Rectangle.
        """
        assert isinstance(pt_ll, Point)
        assert isinstance(pt_ur, Point)
        self.ll = pt_ll
        self.ur = pt_ur

    def __str__(self):
        """Returns WKT String "POLYGON ((x0 y0, x1 y1, ..., x0 y0))"
        """
        return f"POLYGON ({self.ll.x} {self.ll.y}, {self.ur.x} {self.ur.y})"

    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.

        other - Point, Circle or Rectangle

        Returns - True / False
        """
        if isinstance(other, Point):
            # Make use of symmetry (point vs. rect = rect vs. point)
            # self = rect, other = point
            return other.intersects(self)
        elif isinstance(other, Circle):
            # Make use of symmetry (circ vs. rect = rect vs. circ)
            # self = rect, other = circ
            return other.intersects(self)
        elif isinstance(other, Rectangle):
            # find the coordinates of the "common" overlapping rectangle
            x_left = max(self.ll.x, other.ll.x)
            y_bottom = max(self.ll.y, other.ll.y)
            x_right = min(self.ur.x, other.ur.x)
            y_top = min(self.ur.y, other.ur.y)
            # find the width and height of the "common" overlapping rectangle
            width = x_right - x_left
            height = y_top - y_bottom
            # if the width and height are positive, there is overlapping
            return width > 0 and height > 0
        else:
            return False

    def width(self):
        """Returns the width of the Rectangle.

        Returns - float
        """
        return abs(self.ur.x - self.ll.x)

    def height(self):
        """Returns the height of the Rectangle.

        Returns - float
        """
        return abs(self.ur.y - self.ll.y)


def _test():
    """Test whether your implementation of all methods works correctly.
    Test checklist:
    point - point
    rect - rect
    circle - circle
    circle - rect
    circle - point
    rect - point
    """
    # point - point collision
    pt0 = Point(0, 0)
    pt1 = Point(0, 0)
    pt2 = Point(10, 10)
    assert pt0.intersects(pt1)
    assert pt1.intersects(pt0)
    assert not pt0.intersects(pt2)
    assert not pt2.intersects(pt0)

    # rectangle - circle collision
    c = Circle(Point(-1, -1), 1)
    r4 = Rectangle(Point(0, 0), Point(10, 10)) # does not collide circle
    r5 = Rectangle(Point(-5, -5), Point(10, 10))  # collides with circle
    assert not c.intersects(r4)
    assert not r4.intersects(c)
    assert c.intersects(r5)
    assert r5.intersects(c)


    # Extend this method to be sure that you test all intersects methods!
    # Read Section 16.5 of the book if you have never seen the assert statement

    # circle - point collision
    circle_p = Circle(Point(0, 0), 5)
    p_inside_c = Point(3, 3)  # distance from center = 5 -> on the circle boundary
    p_outside_c = Point(6, 8)  # distance from center = 10 -> outside circle
    assert p_inside_c.intersects(circle_p)
    assert circle_p.intersects(p_inside_c)
    assert not p_outside_c.intersects(circle_p)
    assert not circle_p.intersects(p_outside_c)

    # point - rectangle collision
    rect_p = Rectangle(Point(0, 0), Point(10, 10))
    p_inside_r = Point(5, 5)  # in the center of the rectangle
    p_outside_r = Point(15, 15)  # outside the rectangle
    assert p_inside_r.intersects(rect_p)
    assert rect_p.intersects(p_inside_r)
    assert not p_outside_r.intersects(rect_p)
    assert not rect_p.intersects(p_outside_r)

    # Circle - circle collision
    c1 = Circle(Point(0, 0), 5)
    c2 = Circle(Point(8, 0), 5)  # collides with c1 (center distance = 8, radius sum = 10)
    c3 = Circle(Point(12, 0), 1) #  does not collide with c1 (center distance = 12, radius sum = 6)
    assert c1.intersects(c2)
    assert c2.intersects(c1)
    assert not c1.intersects(c3)
    assert not c3.intersects(c1)

    # rect - rect collision
    r1 = Rectangle(Point(0, 0), Point(10, 10))
    r2 = Rectangle(Point(5, 5), Point(15, 15))  # collides (ll is in center of r1)
    r3 = Rectangle(Point(20, 20), Point(30, 30)) # does not collide (ur is rightside-above r1)
    assert r1.intersects(r2)
    assert r2.intersects(r1)
    assert not r1.intersects(r3)
    assert not r3.intersects(r1)

if __name__ == "__main__":
    _test()
