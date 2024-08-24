# def print_diamonds(n):
#     # Print the top half of the diamonds
#     for i in range(2, ((n+1) // 2)+1):
#         spaces = ' ' * (2*(i-1))  # Leading spaces for centering
#         # Print both diamonds with a space in between
#         print(spaces + )
#
#         # Print the bottom half of the diamonds
#     for i in range(n - 1, 0, -1):
#         spaces = ' ' * (n - i)  # Leading spaces for centering
#         # Print both diamonds with a space in between
#         print(spaces + '*' * (2 * i - 1) + ' ' + '*' * (2 * i - 1))
#
#     # Input
#
#
# n = int(input("Enter a number n: "))
# print_diamonds(n)

# ---------------------------------------------------------------------

# # Function to print full pyramid pattern
# def full_pyramid(n):
#     for i in range(1, n + 1):
#         # Print leading spaces
#         for j in range(n-i):
#             print(" ", end="")
#
#         # Print asterisks for the current row
#         for k in range(1, 2*i):
#             print("*", end="")
#         print()

# n = int(input())
# full_pyramid(n)

# -------------------------------------------------------------

# def A1(a: int, b: int) -> int:
#     def A2(a: int, b: int) -> int:
#         return a + b
#     return A2(a, b) + 5
#
#
# print(A1(4, 5))

# -------------------------------------------------------------

# string = input("Enter your name: ")
# print("Original string is:", string)
#
# result = string[0]
#
# middle = len(string) // 2
#
# last = string[len(string) - 1]
# result += string[middle] + last
#
# print("the result:", result)

# --------------------------------------------------------

# string = input("Enter your word: ")
#
# res = string[(len(string)//2)-1:(len(string)//2)+2]
# print(res)

# -----------------------------------------------------------

# s1 = input("s1: ")
# s2 = input("s1: ")
#
# res = s1[0:len(s1)//2] + s2 + s1[(len(s1)//2):]
# print(res)

# ---------------------------------------------------------

# res_for_lower = ""
# res_for_upper = ""
#
# str1 = input("S1: ")
# for i in str1:
#     if i not in str1.upper():
#         res_for_lower += i
#     else:
#         res_for_upper += i
#
# print(res_for_lower + res_for_upper)

# ---------------------------------------------------
# making a Pascal triangle:

# def pascal_triangle(n):
#
#     triangle = []
#
#     for i in range(n):
#         row = [1] * (i+1)
#
#         for j in range(1, i):
#             row[j] = triangle[i-1][j-1] + triangle[i-1][j]
#             triangle.append(row)
#
#     for row in triangle:
#         print(' '.join(map(str, row)))
#
#
# n = int(input())
# pascal_triangle(n)

# ---------------------------------------------------------












