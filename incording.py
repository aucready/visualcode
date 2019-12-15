#유니코드와 인코딩

# c = 10

# def add(a, b):
#     global c
#     c = a + b
#     return c

# d = add(3,4)
# print(c, d)




def get_input_user(msg, casting = int):
    while True:
        try:
            user = casting(input(msg))
            return user
        except:
            continue

user = get_input_user("사용자 이름을 입력 하세요", str)
age = get_input_user("나이를 이름을 입력 하세요")

print(user, age)




