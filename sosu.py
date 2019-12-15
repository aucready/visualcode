#입력한 숫자가 소수인지
while True:
    num = input("2이상의 숫자를 입력하세요.")
    if not num.isnumeric():
        continue
    num = int(num)
    if num < 2:
        continue
    break

isprime = True
for n in range(2, num):
    if num % n == 0:
        isprime = False
        break

if isprime:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")

