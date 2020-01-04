#타이핑게임 만들기

import time
import random
import os




word_list = [
    '동해물과 백두산이 마르고 닳도록', 
    '하느님이 보우하사 우리나라 만세', 
    '무궁화 삼천리 화려 강산 대한사람 대한으로 길이 보전하세', 
    '남산 위에 저 소나무 철갑을 두른듯 바람서리 불변함은 우리 기상일세', 
    '무궁화 삼천리 화려 강산 대한사람 대한으로 길이 보전하세',
    '가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세 ', 
    '무궁화 삼천리 화려 강산 대한사람 대한으로 길이 보전하세 ', 
    '이 기상과 이 마음으로 충성을 다하여', 
    '괴로우나 즐거우나 나라사랑하세 무궁화 삼천리', 
    '화려 강산 대한사람 대한으로 길이 보전하세'
]

random.shuffle(word_list)
#print(word_list)


for q in word_list:
    start_time = time.time()
    user_input = str(input(q + '\n').strip())
    end_time = time.time() - start_time
    
    if user_input == '/exit':
        break



    correct = 0
    for i, c in enumerate(user_input):
        if i >= len(q):
            break
        if c == q[i]:
            correct += 1

    tot_len = len(q)

    c = correct / tot_len * 100
    e = (tot_len - correct ) / tot_len * 100
    speed = (correct / end_time) * 60

    print('속도:{:0.2f} 정확도:{:0.2f} 오타율:{:0.2f}'.format(speed, c, e))




