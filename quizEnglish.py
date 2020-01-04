


#영어 단어 맞추기 게임
import random

word_dict = {
    '호랑이': 'tiger',
    '강아지': 'dog',
    '고양이': 'cats',
    '코끼리': 'eliphant'

}

words = []

for key in word_dict:
    words.append(key)

random.shuffle(words)

chance = 3

for i in range(0, len(words)):
    q = words[i]

    for j in range(0, chance):
        user_input = str(input('{}의 영어 단어를 입력하세요: '.format(q)))
        english = word_dict[q]


        if user_input.strip().lower() == english.lower():
            print('정답입니다.')
            break
        else:
            print('틀렸습니다')

    if user_input != english:
        print("정답은 {} 입니다.".format(english))
print('문제를 모두 풀었습니다. ')


