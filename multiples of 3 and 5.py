
input_num = 1000
multi_num = []
multi_count = 0
for i in range(1,input_num):
    if i % 3 == 0 or i % 5 == 0:
        multi_num.append(i)
        multi_count += i
print("{}미만의 자연수에서 3과 5의 배수의 합은 {}이다.".format(input_num, multi_count))


