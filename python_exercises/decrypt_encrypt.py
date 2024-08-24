# while True:
#     print("Choose your option:\n\t1. Encrypt\n\t2. Decrypt\n\t3. Exit")
#     choice = input("Your choice: ")
#     if choice == "1":
#         plaintext = input("text: ")
#         encrypted_text = ""
#         for char in plaintext:
#             x = ord(char) * 2 + 5
#             encrypted_text += chr(x)
#         print("encrypted text: ", encrypted_text)
#         print("*"*40, "\n")
#
#     elif choice == "2":
#         encrypted_text = input("encrypted text: ")
#         plaintext = ""
#         for char in encrypted_text:
#             x = (ord(char)-5) // 2
#             plaintext += chr(x)
#         print("plain text: ", plaintext)
#         print("*" * 40, "\n")
#
#     elif choice == "3":
#         print("Thanks for your time")
#         break
#
#     else:
#         print("Your choice is Wrong!")

# ----------------------------------------------------------------------

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# square = list(map(lambda x: x ** 2, li))
# cube = list(map(lambda x: x ** 3, li))
#
# print(square)
# print(cube)

# ------------------------------------------------------------------
# def star(a):
#     def inner1(func):
#         def inner2(*x, **y):
#             print("*"*a)
#             func(*x, **y)
#             print("*"*a)
#         return inner2
#     return inner1
#
#
# @star(20)
# def msg(name):
#     print("I am " + name)
#
#
# msg("reza")


# x = "awesome"
#
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)


# x = frozenset({"apple", "banana", "cherry"})
# print(x)

# ----------------------------------------------------------------

# passwords = {"ali": "35548648", "aria": "51548642", "ahmad": "69835464", "neda": "5466597", "narges": "487421949"}
# black_list = {"narges", "aria"}
#
#
# def permission(func):
#     def inner1(*args, **kwargs):
#         if args[0] in black_list:
#             print("This user is blocked by server!!!")
#         else:
#             func(*args, **kwargs)
#     return inner1
#
#
# @permission
# def print_password(username):
#     print(username, ":", passwords[username])
#
#
# @permission
# def change_password(username, new_password):
#     passwords[username] = new_password
#     print(username, ":", passwords[username])
#
#
# print_password("ali")
# change_password("narges", "1234")

# -------------------------------------------------------------------

# from time import perf_counter
#
#
# def time_calculation(func):
#     def wrapper_decorator(*args, **kwargs):
#         start_time = perf_counter()
#         value = func(*args, **kwargs)
#         end_time = perf_counter()
#         performance_time = end_time - start_time
#         print("the run time for", func.__name__, "is: ", performance_time)
#         return value
#     return wrapper_decorator
#
#
# @time_calculation
# def A(y):
#     s = 0
#     for i in range(y):
#         s += i**2
#
#
# @time_calculation
# def B(x):
#     fact = 1
#     for i in range(1, x+1):
#         fact *= i
#
#
# A(10000000)
# B(100000)

# -----------------------------------------------------------------

# def list_range(start, end, step=1):
#     new_range = []
#     while start < end:
#         new_range.append(start)
#         start += step
#     return new_range


# r = list(range(10, 20, 2)) # built_in
# print(r)

# lr = list_range(10, 20, 2) # custom made
# print(list(lr))

# def my_generator(r=10):
#     for i in range(r):
#         yield i ** 2
#
#
# g = my_generator()
# # g.close()
# for i in g:
#     if i == 16:
#         g.throw(ValueError("Error!!"))
#     print(i)

# -------------------------------------------------------------------

# def my_enumerate(*args, **kwargs):
#     i = 0
#     for value in args:
#         print(map(f"i: {i}, value: {value}"))
#         i += 1
#
#
# my_enumerate({"aria": "54", "ali": "879", "nar": "654"})

# the answer :

# def my_enumerate(sequence, start=0):
#     count = start
#     for i in sequence:
#         yield count, i
#         count += 1
#
#
# lst = ["rexa", "aria"]
# for i, j in my_enumerate(lst, 5):
#     print(i, j)

# --------------------------------------------------------------------

# def my_fibonacci(n):
#     a = 0
#     b = 1
#     if n == 2:
#         yield a
#         yield b
#     else:
#         yield a
#         yield b
#         for i in range(3, n+1):
#             c = a + b
#             yield c
#             a = b
#             b = c
#
#
# print(next(my_fibonacci(3)))
# print(next(my_fibonacci(3)))
# print(next(my_fibonacci(3)))
# print(next(my_fibonacci(3)))

# The answer :

# def my_fibonacci():
#     f1 = 0
#     yield f1
#     f2 = 1
#     yield f2
#     while True:
#         f3 = f1 + f2
#         yield f3
#         f1 = f2
#         f2 = f3
#
#
# fib = my_fibonacci()
# for _ in range(50):
#     print(next(fib))

# -------------------------------------------------------------------------

# def gen_list(lst):
#     for i in lst:
#         for j in range(0, i+1):
#             s = 0
#             s += j
#             yield s
#
#
# print(next(gen_list([1, 2, 3, 4, 5])))
# print(next(gen_list([1, 2, 3, 4, 5])))
# print(next(gen_list([1, 2, 3, 4, 5])))

# The answer :

# def sum_gen(lst):
#     s = 0
#     for i in lst:
#         s += i
#         yield s
#
#
# sg = sum_gen([1, 2, 3, 4, 5])
# for i in sg: print(i)

# -----------------------------------------------------------

# def str_gen(s: str):
#     sl = list(s)
#     for i in range(len(sl)):
#         yield sl[-1:i]
#
#
# print(next(str_gen("hello")))
# print(next(str_gen("hello")))
# print(next(str_gen("hello")))
# print(next(str_gen("hello")))

# The answer :

# def rev_str(s):
#     l = len(s)
#     for i in range(l-1, -1, -1):
#         yield s[i]
#
#
# sg = rev_str("reza dolati")
# for ch in sg:
#     print(ch)

# ------------------------------------------------------------------------

# def my_gen(even_or_odd="e"):
#     count = 0
#     if even_or_odd.lower() == "o":
#         count = 1
#     while True:
#         yield count
#         count += 2
#
#
# eo = my_gen("e")
# for _ in range(10):
#     print(next(eo))

# --------------------------------------------------------------

# def num_gen():
#     c = 1
#     while True:
#         s = ""
#         for i in range(1, c+1):
#             s += f"{c}\t"
#         yield s
#         c += 1
#
#
# n = num_gen()
# for j in range(20):
#     print(next(n))

# -------------------------------------------------------------------------

# from functools import wraps
#
#
# def coroutine(func):
#     @wraps(func)
#     def start(*args, **kwargs):
#         gn = func()
#         print(next(gn))
#         return gn
#     return start
#
#
# @coroutine
# def my_gen():
#     print("start")
#     for i in range(5):
#         name = yield
#         print("my name is:", name)
#
#
# g = my_gen()
# print(g.send("john"))
# print(g.send("neda"))

# -------------------------------------------------------------------

# a generator for censoring words
# def cen_gen(words):
#     w = None
#     while True:
#         word = yield w
#         if word not in words:
#             w = word
#         else:
#             w = "*" * len(word)
#
#
# g = cen_gen(["khar", "gav", "meymoon"])
# next(g)
# print(g.send("reza"))
# print(g.send("khar"))
# print(g.send("meymoon"))
# print(g.send("reza"))
# print(g.send("aria"))
# print(g.send("neda"))
# print(g.send("zeinab"))
# print(g.send("gav"))

# -------------------------------------------------------------------

# reverse timer
# from time import sleep
#
# def reverse(n):
#     if n <= 0:
#         return
#     sleep(1)
#     print(n)
#     return reverse(n-1)
#
#
# reverse(5)

# -------------------------------------------------------------------------

# multiplication of numbers bigger than 5 in another number
# def mul_5(n):
#     if n == 0:
#         return 1
#     elif n % 10 < 5:
#         return mul_5(n // 10)
#     else:
#         return n % 10 * mul_5(n // 10)
#
#
# print(mul_5(65984867))

# -----------------------------------------------------------------------

# fibonacci with recursive function

# def rec_fib(n):
#     if n == 0 or n == 1:
#         return n
#     return rec_fib(n-1) + rec_fib(n-2)
#
#
# print(rec_fib(2))

# ------------------------------------------------------------------

# def sum_lst(lst):
#     if len(lst) == 0:
#         return 0
#     # elif len(lst) == 1:
#     #     return lst[0]
#     else:
#         return lst[0] + sum_lst(lst[1:])
#
#
# print(sum_lst([1, 4, 7, 9, 11]))

# ----------------------------------------------------------------------

# def power(sub, exp):
#     if exp == 0:
#         return 1
#     if exp == 1:
#         return sub
#     return sub * power(sub, exp-1)
#
#
# print(power(-1, 2))

# ----------------------------------------------------------------------

# def rev_rec(string):
#     if len(string) == 0:
#         return string
#     else:
#         return rev_rec(string[1:]) + string[0]
#
#
# print(rev_rec("aria"))

# ----------------------------------------------------------

# def repeat_rec(lst, element):
#     if len(lst) == 0:
#         return 0
#     else:
#         if lst[0] == element:
#             return repeat_rec(lst[1:], element) + 1
#         else:
#             return repeat_rec(lst[1:], element)
#
#
# print(repeat_rec([1, 5, 6, 1, 5, 1, 44, 87], 1))

# --------------------------------------------------------------
# recursive decorator :
# from time import sleep
#
#
# def dec(func):
#     def wrapper(*args, **kwargs):
#         print("*" * 40)
#         value = func(*args, **kwargs)
#         print("-" * 40)
#         return value
#     return wrapper
#
#
# @dec
# def rev(n):
#     if n <= 0:
#         return
#     sleep(1)
#     print(n)
#     rev(n-1)
#
#
# rev(10)

# ---------------------------------------------------------------------------

#1

# if len((s := input())) >= 10:
#     print(s)
# else:
#     print("the condition wasn't satisfied!")

# -------------------------------------------------------------------------

#2

# if len(lst := [1, 2, 3, 4, 5, 6]) > 5:
#     print(sum(lst[0:2]))
# else:
#     print("The list has less than 5 elements!")

# ----------------------------------------------------------------------------

#3

# numbers = []
# while True:
#     if (user_input := input("Enter a number (Press Enter to calculate the sum): ")) == "":
#         break
#     numbers.append(int(user_input))
#
# total = sum(numbers)
# print("Sum:", total)

# ----------------------------------------------------------------------------

#4

# nums = [1, 2, 3, 4, 8, 7, 5, 6, 5]
# if n := 5 in nums:
#     print(nums.index(5))

# ----------------------------------------------------------------------

#5

# from random import randint
# numbers = []
# while (n := randint(1, 100)) <= 80:
#     numbers.append(n)
#
# print(numbers)
# print("The number of these numbers:", len(numbers))

# ----------------------------------------------------------------

#6

# while (s := input()).lower() != "q":
#     print(s.count(" ")+1)

# ----------------------------------------------------------------------

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# t = []
# for i in range(len(matrix)):
#     t_row = []
#     for row in matrix:
#         t_row.append(row[i])
#     t.append(t_row)
#
# for i in t:
#     print(i)

# ---------------------------------------------------------

# from random import randrange
# def func():
#     return randrange(50, 150)
#
# x = [s for _ in range(10) if (s := func()) > 100 ]
# print(x)

# ----------------------------------------------------------------------

# text = "World, Hello!"
# encoded_text = text.encode('utf-8')
# print(encoded_text)

# encoded_bytes = b'My name is M\xc3\xb6bius'
# decoded_string = encoded_bytes.decode('utf-8')
# print(decoded_string)

# char_list = ['A', 'B', 'C', 'D', 'E']
# ascii_list = [ord(char) for char in char_list]
# print(ascii_list)

# sentence = input("Enter a sentence: ")
# ascii_sum = sum(ord(char) for char in sentence)
# print("Sum of ASCII values of all characters:", ascii_sum)

# unicode_list = [1024, 5678, 234, 987]
# encoded_bytes = [chr(code).encode('utf-16') for code in unicode_list]
# print(encoded_bytes)

# encoded_bytes = b'\xff\xfeM\x00y\x00 \x00N\x00a\x00m\x00e\x00'
# decoded_string = encoded_bytes.decode('utf-16')
# print(decoded_string)

# def utf8_encode_hex(input_string):
#     # Encode the input string using UTF-8 encoding
#     encoded_bytes = input_string.encode('utf-8')
#
#     # Convert the encoded bytes to hexadecimal representation
#     hex_representation = encoded_bytes.hex()
#
#     return hex_representation
#
# # Test the function
# input_string = "Hello, 你好"
# result = utf8_encode_hex(input_string)
# print(result)


hex_string = "1a2b3c"  # Replace with your desired hexadecimal string
my_bytearray = bytearray.fromhex(hex_string)
print(my_bytearray)









