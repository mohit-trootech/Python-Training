# Program to find distance between two points in XY plane
from check_number_input import is_number
import math


def distance_2_points(p1,p2):
    if len(p1) == 2 and len(p2) == 2:
        if is_number(p1[0]) and is_number(p1[1]) and is_number(p2[0]) and is_number(p2[1]):
            return math.sqrt(((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))
    else:
        print("Points Must Contain Exactly Two Coordinated X & y")


def distance_from_origin(p):
    if len(p) == 2:
        if is_number(p[0]) and is_number(p[1]):
            return round(math.sqrt(((p[0])**2) + ((p[1])**2)), 2)
    else:
        print("Points Must Contain Exactly Two Coordinated X & y")
