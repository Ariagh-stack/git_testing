# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def make_sound(self):
#         print("Generic animal sound!")
#
#
# class Mammal(Animal):
#     def __init__(self, leg_count, **kwargs):
#         super().__init__(**kwargs)
#         self.leg_count = leg_count
#
#     def make_sound(self):
#         print("Generic mammal sound!")
#
#
# class Dog(Mammal):
#     def __init__(self, race, **kwargs):
#         super().__init__(**kwargs)
#         self.race = race
#
#     def make_sound(self):
#         print("Woof!")
#
#
# dog = Dog(name="Nigga", race="Nigga", leg_count=4, species="Dog")
# dog.make_sound()



# -------------------------------------------------------------------------

# # Parent Class
# class Vehicle:
#     def __init__(self, color, weight, speed):
#         self.color = color
#         self.weight = weight
#         self.speed = speed
#
#     def move(self):
#         raise NotImplementedError("Subclasses must implement this method")
#
#
# # Child Classes
# class Car(Vehicle):
#     def move(self):
#         return f"The car is driving at {self.speed} km/h."
#
#
# class Bicycle(Vehicle):
#     def move(self):
#         return f"The bicycle is pedaling at {self.speed} km/h."
#
#
# class Airplane(Vehicle):
#     def move(self):
#         return f"The airplane is flying at {self.speed} km/h."
#
#
# # Grandchild Classes
# class Lamborghini(Car):
#     def __init__(self, color, weight, speed, model):
#         super().__init__(color, weight, speed)
#         self.model = model
#
#     def move(self):
#         return f"The {self.model} Lamborghini zooms at {self.speed} km/h!"
#
#
# class Benz(Car):
#     def __init__(self, color, weight, speed, model):
#         super().__init__(color, weight, speed)
#         self.model = model
#
#     def move(self):
#         return f"The {self.model} Benz glides at {self.speed} km/h!"
#
#
# # Example usage
# def main():
#     vehicles = [
#         Lamborghini("Red", 1500, 300, "Aventador"),
#         Benz("Black", 1700, 250, "S-Class"),
#         Bicycle("Blue", 15, 20),
#         Airplane("White", 50000, 900),
#         Car("red", 200, 95)
#     ]
#
#     for vehicle in vehicles:
#         print(vehicle.move())
#
#
# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------

# class PrintInfoMixin:
#     def info_print(self):
#         class_name = self.__class__.__name__
#         attributes = vars(self)
#         print(f"Class Name: {class_name}")
#         print("Attributes:")
#         for attr, value in attributes.items():
#             print(f"  {attr}: {value}")
#
#
# # Example usage
# class MyClass(PrintInfoMixin):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # Create an instance of MyClass
# obj = MyClass("Alice", 30)
# # Call the info_print method
# obj.info_print()

# --------------------------------------------------------------------

# class MathOperationsMixin:
#
#     def addition(self):
#         return self.x + self.y
#
#     def subtraction(self):
#         return self.x - self.y
#
#     def multiplication(self):
#         return self.x * self.y
#
#     def division(self):
#         if self.y == 0:
#             raise ZeroDivisionError("Division by zero!!!")
#         else:
#             return self.x / self.y
#
#
# class Calculator(MathOperationsMixin):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# obj = Calculator(10, 5)
# print("Addition: ", obj.addition())
# print("Subtraction: ", obj.subtraction())
# print("Multiplication: ", obj.multiplication())
# print("Division: ", obj.division())

# ----------------------------------------------------------------------------

# import logging
#
# # Configure the logging
# logging.basicConfig(level=logging.INFO)
#
# class LoggerMixin:
#     def log_method_call(self, method_name, *args, **kwargs):
#         logging.info(f"Method '{method_name}' called with arguments: {args}, {kwargs}")
#
#     def __getattribute__(self, name):
#         # Get the attribute without entering the custom __getattribute__
#         attr = object.__getattribute__(self, name)
#         if callable(attr):  # Check if the attribute is callable (i.e., a method)
#             def wrapped(*args, **kwargs):
#                 self.log_method_call(name, *args, **kwargs)
#                 return attr(*args, **kwargs)
#             return wrapped
#         return attr
#
# # Example usage
# class MyClass(LoggerMixin):
#     def add(self, x, y):
#         return x + y
#
#     def multiply(self, x, y):
#         return x * y
#
# # Create an instance of MyClass
# obj = MyClass()
#
# # Call methods
# result_add = obj.add(10, 5)
# result_multiply = obj.multiply(10, 5)

# -----------------------------------------------------------------------------

# class Shape:
#     def __init__(self, **kwargs):
#         self.area = 0
#         self.perimeter = 0
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#
#     def calculate_area(self):
#         pass
#
#     def calculate_perimeter(self):
#         pass
#
#     def show(self):
#         info = ""
#         for key, value in self.__dict__.items():
#             if value > 0:
#                 info += f"{key} : {value:.2f}\n"
#         print(info)
#
#     def __str__(self):
#         return self.__class__.__name__
#
#
# class Rectangle(Shape):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#
#     def calculate_area(self):
#         self.area = self.length * self.width
#
#     def calculate_perimeter(self):
#         self.perimeter = 2 * (self.width + self.length)
#
#
# s = Rectangle(length=10, width=14)
# print(s)
# s.calculate_area()
# s.calculate_perimeter()
# s.show()
#

# ------------------------------------------------------------------------

# from datetime import datetime
#
#
# class Product:
#     def __init__(self, product_name, price, off):
#         self.product_name = product_name
#         self.price = price
#         self.off = off
#
#     def __str__(self):
#         return self.product_name
#
# class Comment:
#     website_name = "sabzlearn.ir"
#
#     def __init__(self, product, name, description, like_count, dislike_count):
#         self.product = product
#         self.name = name
#         self.description = description
#         self.like_count = like_count
#         self.dislike_count = dislike_count
#         self.date = datetime.now()
#
#     def show(self):
#         print(f"product : {self.product}\n"
#               f"name : {self.name}\n"
#               f"description : {self.description}\n"
#               f"date : {self.date}\n"
#               f"like : {self.like_count} and dislike : {self.dislike_count}")
#
#
# python_course = Product("python expert", 0, 0)
# c1 = Comment(python_course, "reza", "very good course", 50, 5)
# c1.show()

# ----------------------------------------------------------------------

# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self._radius = None  # Using a private variable for internal storage
#         self.radius = radius  # Use the setter to initialize
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         if value <= 0:
#             raise ValueError("Radius must be a positive value.")
#         self._radius = value
#
#     @property
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
#
# # Example usage:
# try:
#     circle = Circle(5)
#     print(f"Circle radius: {circle.radius}")
#     print(f"Circle area: {circle.area}")
#
#     # Attempting to set a negative radius
#     circle.radius = -3
# except ValueError as e:
#     print(e)

# ---------------------------------------------------------------------------

# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius
#
#     @property
#     def fahrenheit(self):
#         return (self.celsius * 9/5) + 32
#
# # Example usage:
# temp = Temperature(25)
# print(f"Temperature in Celsius: {temp.celsius}°C")
# print(f"Temperature in Fahrenheit: {temp.fahrenheit}°F")

# ----------------------------------------------------------------------------












