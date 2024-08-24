# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
#     print("Success")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
#     y = int(input("y:"))
#     print(x/y)
#     print("Success")

# ----------------------------------------------

# x = "Name Is James"
# print('**'.join(x.split()))
#
# print("Name", "Is", "James", sep="**")

# ----------------------------------------------

# num = int(input("n: "))
#
# print('%o' % num)

# ---------------------------------------------

# with open("test1.txt", "r") as f1:
#     lines = f1.readlines()
#
# with open("test2.txt", "w") as f2:
#     count = 0
#     for line in lines:
#         if count == 4:
#             count += 1
#             continue
#         else:
#             f2.write(line)
#
#         count += 1

# --------------------------------------------------

# totalMoney = 1000
# quantity = 3
# price = 450
# statement = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars.".format(quantity, totalMoney, price)
# print(statement)

# ----------------------------------------------------

# import os
#
# size = os.stat("test1.txt").st_size
# if size == 0:
#     print('file is empty')
# else:
#     print('the file is not empty!')

# ---------------------------------------------------

with open("test1.txt", "r") as f:
    # count = 0
    # for line in f.readlines():
    #     if count == 3:
    #         print(line)
    #     count += 1
    lines = f.readlines()
    print(lines[3])



