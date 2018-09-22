#Задание1
class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4
    
a_rectangle = Rectangle(25, 50)
a_square = Square(20)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())

#Задание2
class Square():
    def __init__(self, s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4
    def change_size(self, new_size):
        self.s1 += new_size
a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)

#Задание3
class Shape():
    def what_am_i(self):
        print("Я - фигура")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square(Shape):
    def __init__(self,s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4
a_rectangle = Rectangle(20, 50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()

#Задание4
class Horse():
    def __init__(self, name):
        self.name = name


class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

harry_the_horse = Horse("Гарри")
the_rider = Rider("Салли", harry_the_horse)

print(the_rider.horse.name)
    

    
