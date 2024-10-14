

class Point(object):
    def __init__(self, xinit, yinit):
        self.x = xinit
        self.y = yinit

    def reflect_x(self):
        reflected_point_x = Point(self.x, - self.y)
        return reflected_point_x

# Reflected_point_x instance with object(Point(3, 5))
reflected_point_x = Point.reflect_x(Point(3, 5))

# To access a variable from within the instance, outside the instance:
# - instance_name.instance_variable_name - i.e. reflected_point_x.x
print(f"Reflected Point: ({reflected_point_x.x}, {reflected_point_x.y})")
