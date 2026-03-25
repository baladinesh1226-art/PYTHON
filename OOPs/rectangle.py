class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        area = self.width * self.height
        print(area)

    def perimeter(self):
        perimeter = 2*(self.width * self.height)
        print(perimeter)



rt = Rectangle(2,6)

rt.area()
rt.perimeter()
