#반복문 while, for


num = 0 
# while True:
#     print(num)
#     num += 1
#     if num ==10:
#         break

# for i in range(1,1000):
#     print(i)
#     if i == 10:
#         break


# while num <10:
#     num += 1
#     if num == 5:
#         continue
#     print(num)
hap = 0

for i in range(1, 100):
    if i % 2 == 0:
        continue
    hap += i
    print("중간 합은{} 입니다. ".format(hap))

print("홀수의 합{} 입니다. ".format(hap))


