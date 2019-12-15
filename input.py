#사용자 입력 받기
# user = input("what your name?")

# print(user)


# num1 = int(input("숫자 넣어주세요"))
# num2 = int(input("숫자 넣어주세요"))
# print(num1 + num2)



langs =  ["korea", "english"]

for i, l in enumerate(langs, start = 1):
    print("{}. {}".format(i, l))

while True:
    sel =  input("언어를 선택하세요.")
    if not sel.isnumeric():
        continue
    sel = int(sel)

    if 0 < int(sel) <3:
        break

print("사용자가 선택한 언어는 {} 입니다.".format(langs[sel-1]))

