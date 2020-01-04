
import random

# 한글동물을 영어로 입력하는 게임

words_dict = {'호랑이': 'tiger',
    '강아지': 'dog',
    '고양이': 'cats',
    '코끼리': 'eliphant'}

words = []

for word in  words_dict:
    words.append(word)

random.shuffle(words)

chance = 3

for i in range(0,len(words)):
    q = words[i]
    for j in range(0,chance):
        user_input = str(input('{} 의 영단어를 입력하세요. :'.format(q)))
        english = words_dict[q]

        if user_input.lower().strip() == english.lower():
            print('정답입니다.')
            break
        else:
            print('오답입니다.')
    if user_input != english:
        print('정답은 {} 입니다. '.format(english))

print('완료했습니다. 다시 도전 하세요')







# while j < 3:
#     random.shuffle(words)
#     print(words)
#     j += 1
# for k in range(0,4):
#     print(words[k])
#     q = words[k]
#     print(words_dict[q])
#
#
