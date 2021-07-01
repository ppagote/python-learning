"""[summary]
    """
class Line:
    """[summary]
    """

    def __init__(self, coor1, coor2):
        """[summary]

        Arguments:
            coor1 {[tuple]} -- [description]
            coor2 {[tuple]} -- [description]
        """
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return ((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1]-self.coor1[1])**2)**0.5

    def slope(self):
        """[summary]

        Returns:
            [float] -- [description]
        """
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])


my_line = Line((3, 2), (8, 10))

print(my_line.slope())
print(my_line.distance())


class Cylinder:
    """[summary]
    """

    def __init__(self, height=1, radius=1):
        """[summary]

        Keyword Arguments:
            height {int} -- [description] (default: {1})
            radius {int} -- [description] (default: {1})
        """
        self.height = height
        self.radius = radius

    def volume(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return self.height*3.14*(self.radius)**2

    def surface_area(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)


my_cylinder = Cylinder(1, 1)
print(my_cylinder.volume())
print(my_cylinder.surface_area())
