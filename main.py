# 반복문 for
a = [(1,2), (3,4), (5,6)]

for i in a:
    for j in i:
        print(j)

student = [{"홍길동": 100}, {"가제트":90}, {"홍길녀":60}]
for i in student:
    print(i)
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("이름 : {} 점수 : {}".format(name, value))
