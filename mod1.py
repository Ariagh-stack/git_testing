# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __call__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
# # Example usage
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1(p2)
# print(p3.x, p3.y)  # Output: 4 6

# --------------------------------------------------------------

# from abc import ABC, abstractmethod
#
# class Car(ABC):
#     def __init__(self, brand):
#         self.brand = brand
#
#     @abstractmethod
#     def start(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class SportsCar(Car):
#     def __init__(self, brand, max_speed):
#         super().__init__(brand)
#         self.max_speed = max_speed
#
#     def start(self):
#         return f"{self.brand} SportsCar is starting with max speed {self.max_speed} km/h."
#
#     def stop(self):
#         return f"{self.brand} SportsCar is stopping."
#
# class Sedan(Car):
#     def __init__(self, brand, comfort_level):
#         super().__init__(brand)
#         self.comfort_level = comfort_level
#
#     def start(self):
#         return f"{self.brand} Sedan is starting with comfort level {self.comfort_level}."
#
#     def stop(self):
#         return f"{self.brand} Sedan is stopping."
#
# # Example usage
# sports_car = SportsCar("Ferrari", 200)
# print(sports_car.start())
# print(sports_car.stop())
#
# sedan = Sedan("Toyota", "High")
# print(sedan.start())
# print(sedan.stop())

# ----------------------------------------------------------------------

# from abc import ABC, abstractmethod
#
# class Person(ABC):
#     def __init__(self, name, age, role):
#         self.name = name
#         self.age = age
#         self.role = role
#
#     @abstractmethod
#     def greet(self):
#         pass
#
#     @abstractmethod
#     def introduce(self):
#         pass
#
# class Student(Person):
#     def __init__(self, name, age, school):
#         super().__init__(name, age, "Student")
#         self.school = school
#
#     def greet(self):
#         return f"Hello, I am {self.name}."
#
#     def introduce(self):
#         return f"I am {self.name}, a {self.age}-year-old student at {self.school}."
#
# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age, "Teacher")
#         self.subject = subject
#
#     def greet(self):
#         return f"Hello, I am {self.name}."
#
#     def introduce(self):
#         return f"I am {self.name}, a {self.age}-year-old teacher of {self.subject}."
#
# # Example usage
# student = Student("Alice", 20, "XYZ University")
# print(student.greet())
# print(student.introduce())
#
# teacher = Teacher("Bob", 35, "Mathematics")
# print(teacher.greet())
# print(teacher.introduce())

# ---------------------------------------------------------------------

# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def __call__(self, other):
#         return ComplexNumber(self.real + other.real, self.imag + other.imag)
#
#     def __sub__(self, other):
#         return ComplexNumber(self.real - other.real, self.imag - other.imag)
#
#     def __mul__(self, other):
#         real = self.real * other.real - self.imag * other.imag
#         imag = self.real * other.imag + self.imag * other.real
#         return ComplexNumber(real, imag)
#
# # Example usage
# c1 = ComplexNumber(2, 3)
# c2 = ComplexNumber(4, 5)
# c3 = c1(c2)
# c4 = c1 - c2
# c5 = c1 * c2
# print(c3.real, c3.imag)  # Output: 6 8
# print(c4.real, c4.imag)  # Output: -2 -2
# print(c5.real, c5.imag)  # Output: -7 22

# -------------------------------------------------------------------------

# class Matrix:
#     def __init__(self, a11, a12, a21, a22):
#         self.a11 = a11
#         self.a12 = a12
#         self.a21 = a21
#         self.a22 = a22
#
#     def __add__(self, other):
#         return Matrix(
#             self.a11 + other.a11, self.a12 + other.a12,
#             self.a21 + other.a21, self.a22 + other.a22
#         )
#
#     def __sub__(self, other):
#         return Matrix(
#             self.a11 - other.a11, self.a12 - other.a12,
#             self.a21 - other.a21, self.a22 - other.a22
#         )
#
#     def __str__(self):
#         return f"{self.a11}\t{self.a12}\n{self.a21}\t{self.a22}"
#
#
# # Example usage
# m1 = Matrix(1, 2, 3, 4)
# m2 = Matrix(5, 6, 7, 8)
# m3 = m1 + m2
# m4 = m1 - m2
# print(m3)  # Output: 6 8
# #                  10 12
# print()
# print(m4)  # Output: -4 -4
# #                  -4 -4

# -----------------------------------------------------------------------

# def sum_of_numbers1(lst):
#     total = 0
#     for item in lst:
#         if not isinstance(item, (int, float)):
#             raise TypeError(f"Non-numeric element encountered: {item}")
#         total += item
#     return total
#
#
# try:
#     result = sum_of_numbers1([1, 2, 'three', 4.5])
# except TypeError as e:
#     print(e)
#
#
# def sum_of_numbers2(lst):
#     total = 0
#     for item in lst:
#         try:
#             total += int(item)
#         except ValueError:
#             # If the item cannot be converted to an integer, skip it
#             continue
#     return total
#
#
# s = sum_of_numbers2([1, 2, 'three', 4.5])
# print(s)

# ---------------------------------------------------------------------

# def read_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             return content
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#
#
# file_content = read_file('example.txt')
# if file_content:
#     print(file_content)

# --------------------------------------------------------------------

# def returning_value(dic: dict, key):
#     try:
#         print(dic[key])
#     except KeyError:
#         print("Key not found!")
#
#
# d = {"a": 1, "b": 2, "c": 3}
# returning_value(d, "c")

# --------------------------------------------------------------------

# def return_int(s: str):
#     try:
#         return int(s)
#     except ValueError:
#         return None
#
#
# s = return_int("123t")
# print(s)

# ---------------------------------------------------------------

# def returning_sum(lst: list):
#     try:
#         return sum(lst)
#     except TypeError:
#         return "invalid input!"
#
#
# s = returning_sum([1, 2, "3", 4, 5])
# print(s)

# ----------------------------------------------------------------
