import math
import decimal as dec
import numpy as np
from ray import Ray
from device import Device

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
        # deals with the case where the lines intersect, but rays don't
        return None 

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

    # round and return a tuple - (rounding doesn't work for vals like 5.6)
    def display(val):
        if val >= 0:
            return "+{:4.1f}".format(val)
        else:
            val *= -1
            return "-{:4.1f}".format(val)

    return "(" + display(inter[0]) + ", " + display(inter[1]) + ")"


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


def device_test_one():
    """check behavior of multiple devicing with same generator"""
    device_one = Device(0, 0, .01)
    device_two = Device(0, 0, -.01)
    while True:
        y = device_one.simple_poll()
        z = device_two.simple_poll()
        import pdb; pdb.set_trace()


def device_test_two():
    """one device polls twice as fast as the other"""
    rotating_slow = Device(0, 0, 0.1, 0.5, "rotating_slow")
    rotating_fast = Device(0, 0, 0.1, 1.0, "rotating_fast")
    monitor_time_step = 1
    time = 0
    while time < 10:
        ray_a = Ray((0, 0), rotating_slow.global_poll(time))
        ray_b = Ray((-1, -1), rotating_fast.global_poll(time))
        print(ray_a, ray_b)
        time += monitor_time_step


def device_test_three():
    """devices poll at very different rates (2 vs 3)"""
    rotating_medium = Device(0, 0, 0.1, 2.0, "rotating_medium")
    rotating_fast = Device(0, 0, 0.1, 3.0, "rotating_fast")
    monitor_time_step = 1
    time = 0
    while time < 10:
        ray_a = Ray((0, 0), rotating_medium.global_poll(time))
        ray_b = Ray((-1, -1), rotating_fast.global_poll(time))
        print(ray_a, ray_b)
        time += monitor_time_step


def device_test_four():
    """same as last test, but slow monitor"""
    rotating_medium = Device(0, 0, 0.01, 2.0, "rotating_medium")
    rotating_fast = Device(0, 0, 0.01, 3.0, "rotating_fast")
    monitor_time_step = 4.0 
    time = 0
    while time < 40:
        ray_a = Ray((0, 0), rotating_medium.global_poll(time))
        ray_b = Ray((-1, -1), rotating_fast.global_poll(time))
        i = find_intersection(ray_a, ray_b)
        print (ray_a, "|||", ray_b, "|||", i)
        time += monitor_time_step


def device_test_five():
    """same as last test, but more realistic frequencies"""
    rotating_medium = Device(0, 0, 0.01, 60.0, "rotating_medium")
    rotating_fast = Device(0, 0, 0.01, 100.0, "rotating_fast")
    monitor_time_step = 1 / 75.0  # 75 hertz monitor
    time, count = 0, 0
    while count < 60:
        ray_a = Ray((0, 0), rotating_medium.global_poll(time))
        ray_b = Ray((-1, -1), rotating_fast.global_poll(time))
        i = find_intersection(ray_a, ray_b)
        print (ray_a, "|||", ray_b, "|||", i)
        time += monitor_time_step
        count += 1


