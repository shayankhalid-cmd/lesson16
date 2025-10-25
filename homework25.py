class circle:
    def __init__(self, radius):
        self.radius = radius
    def calcuate_area(self):
        area = 3.14 * (radius*radius)
        print("area of circle with radius", radius, "is:", area)
    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * radius
        print("perimeter of a circle is", perimeter)
radius = int(input("enter radius of circle: "))
obj = circle(radius)
obj.calcuate_area()
obj.calculate_perimeter()