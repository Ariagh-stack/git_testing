# n = int(input())
# w = input().split()
#
# w = list(map(int, w))
#
# dic = {}
#
# for i in range(1, n+1):
#     key = i
#     value = w[i-1]
#     dic.setdefault(key, value)
#
# lst_keys = list(dic.keys())
# lst_vals = list(dic.values())
#
# count = 1
# i = 0
#
# while i <= n:
#     if len(dic) < 3:
#         mini = min(dic.keys())
#         if dic[mini] < dic[mini+1]:
#             del dic[mini]
#         else:
#             del dic[mini+1]
#         break
#     else:
#         mini_1 = lst_keys[i]
#         mini_2 = lst_keys[i+count]
#         if dic[mini_1] < dic[mini_2]:
#             del dic[mini_1]
#             i += 1
#         else:
#             del dic[mini_2]
#
#         count += 1
#
# last_key = dic.popitem()
# print(last_key[0])
