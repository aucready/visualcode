result = []
# for num in range(1,6):
#    result.append(num + 5)
#    print(result)

# result = [num + 5 for num in range(1,6)]
# print(result)

# result = [num * 3 for num in range(1,100) if num % 2 == 0]
# print(result)

# for num in range(1,99):
#     if num % 2 ==0:
#         result.append(num * 3)
# print(result)

# for i in range(2,10):
#     for j in range(1,10):
#         result = i * j
#         print("{} x {} = {}".format(i, j, result))

gugudan  = ["{} x {} = {}".format(i, j, i * j) for i in range(2,10) for j in range(1,10) ]

print(gugudan)
