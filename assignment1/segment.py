# GEO1000 - Assignment 1
# Authors: Daan Noordam & Joost de Witte
# Studentnumbers: 5148766 & 5656176

import math


def distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points by using basic Pythagoras rule.
    """
    distance_x = abs(x1 - x2)
    distance_y = abs(y1 - y2)
    calculated_distance = (distance_x ** 2 + distance_y ** 2) ** 0.5
    return calculated_distance


def heron(a, b, c):
    """
    Calculate the area of the triangle formed by the three segments
    """
    s = (a + b + c) / 2
    calculated_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return calculated_area


def angle(a, b, c):
    """
    This function calculates the angle based on the segment lengths (a,b and c).

    When any of the segment lengths is 0, all angles are 0.
    """
    if a == 0 or b == 0 or c == 0:
        calculated_angle = 0
    else:
        calculated_angle = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    return calculated_angle


def segment_point_dist(s1x, s1y, s2x, s2y, px, py):
    """
    Calculate the distance between a point p and the base (line segment between
    point s1 and s2). In the case where point p is not directly above/below the base
    the distance from point p to s1 or s2 (whichever is closest) is calculated.
    """
    distance_s1_p = distance(s1x, s1y, px, py)
    distance_s1_s2 = distance(s1x, s1y, s2x, s2y)
    distance_s2_p = distance(s2x, s2y, px, py)
    angle_alpha = angle(distance_s1_p, distance_s1_s2, distance_s2_p)
    angle_beta = angle(distance_s2_p, distance_s1_s2, distance_s1_p)

    if angle_alpha <= (math.pi / 2) and angle_beta <= (math.pi / 2):
        area_triangle = heron(distance_s1_p, distance_s2_p, distance_s1_s2)
        calculated_segment_point_distance = (2 * area_triangle) / distance_s1_s2
    else:
        calculated_segment_point_distance = min(distance_s1_p, distance_s2_p)
    return calculated_segment_point_distance


print(segment_point_dist(0, 0, 10, 0, 5, 10))
print(segment_point_dist(0, 0, 10, 0, 20, 0))
print(segment_point_dist(0, 0, 10, 0, 0, 0))
print(segment_point_dist(0, 0, 10, 0, 5, 0))
print(segment_point_dist(0, 0, 10, 10, 0, -12))
