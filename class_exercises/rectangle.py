class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = (self.width * self.height)
        return area

    def perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter

    def display(self):
        print("_"*40)
        print(f"Perimeter of this rectangle : {self.perimeter()}\nArea of this rectangle : {self.area()}")


def main():
    wid = int(input("Enter width: "))
    hei = int(input("Enter height: "))
    r1 = Rectangle(wid, hei)
    print(f"You hava a Rectangle with width {r1.width} and height {r1.height}")
    r1.display()


if __name__ == '__main__':
    main()












