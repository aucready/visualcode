#for 반복문 

student = [{'홍길동': 100}, {'감우성': 200}, {'한길이': 300}, {'진중권': 400}]




for s, i in enumerate(student, start=1):
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]

    print('{} name: {} score: {}'.format(s,name,value))


student = [{'홍길동': 100}, {'감우성': 200}, {'한길이': 300}, {'진중권': 400}]



msg = "python programing"

for d, j in enumerate(msg, start=1):
    print(d,j)








