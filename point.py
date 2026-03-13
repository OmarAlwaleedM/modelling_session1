class Point:
    """
    Simple class to represent a point in 2D space.
    """
    def __init__(self, x, y): # Because this def is inside a class, it is now a called a method instead of "function". in methods self is always the first param.
        """
        Constructor for Point class.
        :param x: x coordinate of point.
        :param y: y coordinate of point.
        """
        self.x = x # x is a class attribute
        self.y = y # y is a class attribute
    def __str__(self):
        """
        String representation of Point class.
        :return: string representation of Point class.
        """
        return f"P<{self.x},{self.y}>"

p1 = Point(1, 2)
p2 = Point(3, 4)
# p3 = Point("bob", [1,2,3]) this is possible but not ideal

print(p1.x, p1.y)
print(p2.x, p2.y)
# print(p3.x, p3.y)
print(p1) # P<1,2>.  The output is in base 16!!! hence this code "0x10cdf6a50" is a NUMBER. this is where this point is stored in memory.