import math
import numpy as np

class Ray:

    def __init__(self, origin=(0,0), angle=math.pi/2):
        """Ray - origin, (polar) heading, and (x,y) representation"""
        self.origin = origin
        self.angle = angle
        # use vectors of length of 1 for normalized printouts
        self.direction = self.polar_to_cartesian(1, angle)

    def polar_to_cartesian(self, r, theta):
        """return tuple with x and y components of the vector"""
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return (x, y)

    def __str__(self):
        """print with degrees for clarity"""
        deg = round(math.degrees(self.angle), 2)
        return str(self.origin) + " | " + str(deg)


def exists_intersection(ray_a, ray_b):
    """return if the rays intersect"""

    dx = ray_b.origin[0] - ray_a.origin[0]
    dy = ray_b.origin[1] - ray_a.origin[1]
    det = ray_b.direction[0] * ray_a.direction[1] \
            - ray_b.direction[1] * ray_a.direction[0]
    if det == 0:
        return False
    uu = (dy * ray_b.direction[0] - dx * ray_b.direction[1]) / det
    vv = (dy * ray_a.direction[0] - dx * ray_a.direction[1]) / det
    return uu > 0 and vv > 0 

def find_intersection(ray_a, ray_b):
    """finds intersection assuming it exists (or return False)"""

    if not exists_intersection(ray_a, ray_b):
        return False

    # two equations, two unknowns
    # solve for constants a1 and a2 
    # start from rays origins, and add a1*<ray_1> and a2*<ray_2>
    # find a1 and a2 s.t. left side = right side (intersection)

    a_origin = np.array(ray_a.origin)
    b_origin = np.array(ray_b.origin)
    a_vect = np.array(ray_a.direction)
    b_vect = np.array(ray_b.direction)

    # build a square matrix representing the constants for a1 and a2
    # throw all other constants into a "b" vector s.t. Ax = b
    # use numpy.linalg.solve(a, b) to find a1 and a2

    b_constants = b_origin - a_origin
    square = np.array([[a_vect[0], b_vect[0]], [a_vect[1], b_vect[1]]])
    soln = np.linalg.solve(square, b_constants)

    # use a1 and a2 to recreate the point
    inter = a_origin + soln[0] * a_vect

    # round and return a tuple
    return (round(inter[0], 3), round(inter[1], 3))

def test_ray_constructor():
    """testing"""
    ray_up = Ray()
    ray_down = Ray((0, 0), 3*math.pi/2)
    ray_one_one = Ray((1, 1), math.pi)

def test_intersection():
    """testing"""
    ray_up = Ray()
    ray_one_one = Ray((1, 1), math.pi)
    exists_intersection(ray_up, ray_one_one)
    inter_zero_one = find_intersection(ray_up, ray_one_one)

    ray_45 = Ray((0, 0), math.pi/4)
    ray_135 = Ray((6, 0), 3*math.pi/4)
    inter_three_three = find_intersection(ray_45, ray_135)

    ray_135_neg = Ray((-6, 0), 3*math.pi/4)
    no_inter = find_intersection(ray_45, ray_135_neg)
    import pdb; pdb.set_trace()

test_intersection()
