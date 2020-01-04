import random
import os


def input_check(msg, casting = int):
    while True:
        try:
            input_num = casting(input('input number'))
            return input_num
        except:
            continue






print('1-99사이의 임의의 숫자를 10번안에 맞춰보세요!')

number = random.randint(1,99)


i = 1
while i < 10:
    i += 1
    input_num = input_check('.......')
    if input_num == number:
        print('{} 정답입니다. '.format(input_num))
        break
    elif input_num < number:
        print('{} 보다 큰 숫자입니다.'.format(input_num))
    elif input_num > number:
        print('{} 보다 작은 숫자입니다.'.format(input_num))
    else:
        print('숫자가 아닙니다.')

if input_num == number:
    print('{} 정답입니다. '.format(input_num))
else:
    print('정답은 {} 입니다.'.format(number))

