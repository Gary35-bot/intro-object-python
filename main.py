class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def area(self):
        print("I an a :" + self.name + "\n" +
              "I have " + self.sides + "sides")

class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length=len1
        self.width=wid1
    def area(self):
        result = self.length * self.width
        return result
obj_book = Rectangle (10, 7)
obj_screen = Rectangle(5, 7)
print("The area of a book is " + str(obj_book.area()))

class Circle(Shapes):
    def __init__(self, rad1, rad2, pie):
        self.radius = rad1
        self.radius1 = rad2
        self.pie = 3.14

    def area(self):
        result = self.radius * self.radius1 * self.pie
        return result

obj_plate = Circle(10, 5, 3.14)
print("The area of the plate " + str(obj_plate.area()))

class Triangle(Shapes):
    def __init__(self, b, heid0):
        self.base = b
        self.height = heid0
    def area(self):
        result = self.base * self.height
        return result
obj_sign =Triangle(5, 3)
print("The area of the sign" + str(obj_sign.area()))
