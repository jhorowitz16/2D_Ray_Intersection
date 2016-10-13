import math

class Ray:

    def __init__(self, origin=(0,0), angle=math.pi/2):
        """Ray - origin, (polar) heading, and (x,y) representation"""
        self.origin = origin
        self.angle = angle
        self.cartesian = self.polar_to_cartesian(1, angle)

    def polar_to_cartesian(self, r, theta):
        """return tuple with x and y components of the vector"""
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return (x, y)

    def __str__(self):
        """print with degrees for clarity"""
        deg = round(math.degrees(self.angle), 2)
        return str(self.origin) + " | " + str(deg)


def find_intersection(ray_one, ray_two):
    return -1


def test_ray_constructor():
    """testing"""
    ray_up = Ray()
    ray_down = Ray((0,0), 3*math.pi/2)
    ray_one_one = Ray((1,1), math.pi)
    import pdb; pdb.set_trace()



test_ray_constructor()
