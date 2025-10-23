class circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def calcuate_area(self):
        area = 3.14 * (radius*radius)
        print("area of circle with radius", radius, "is:", area)
radius = int(input("enter radius of circle: "))
obj = circle(radius)

obj.calcuate_area()
