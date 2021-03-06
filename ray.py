import math

class Ray:
    """represent an infinite length Ray at a single moment"""

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
        deg = math.degrees(self.angle)
        deg_txt = "{:3.1f}".format(deg) 
        origin_txt = ("({:4.1f}".format(self.origin[0]) + ", "  
            "{:4.1f}".format(self.origin[1]) + ")")

        if deg < 10:
            return origin_txt + " |   " + deg_txt 
        if deg < 100:
            return origin_txt + " |  " + deg_txt 
        return origin_txt + " | " + deg_txt 

    def __repr__(self):
        """print with degrees for clarity"""
        return str(self)

