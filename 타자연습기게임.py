# 타자게임 만들기





import random
import time


CHO = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONG = [' ','ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

"""
한글 = ((초성 * 21) + 중성) * 28 + 종성 + 4032
초성 = ((x - 44032) / 28) / 21
중성 = ((x - 44032) / 28) % 21
종성 = (x - 44032) % 28
"""

def break_korean(string):
    word_list = list(string)
    break_word = []
    for k in word_list:

        if ord(k) >= ord('가') and ord(k) <= ord('힣'):
            #유니코드상 몇번째 인지 인덱스를 구합니다.
            char_index = ord(k) -  44032

            #초성 = (인덱스/28) /21
            char1 = int((char_index /28) /21 )
            break_word.append(CHO[char1])

            #중성 =  (인덱스 /28) % 21
            char2 = int((char_index / 28 )% 21)
            break_word.append(JUNG[char2])

            #종성 = (인덱스 % 21)
            char3 = int((char_index % 21))

            if char3 > 0 :
                break_word.append(JONG[char3])

        else:
            break_word.append(k)
    return break_word


word_list = [
    "동해물과 백두산이",
    "마르고 닳도록 ",
    "하느님이 보우하사",
    "우리나라 만세",
    "무궁화 삼천리",
    "화려 강산",
    "대한사람 대한으로",
    "길이 보전하세",
    "남산 위에 저 소나무",
    "철갑을 두른듯",
    "바람서리 불변함은",
    "우리 기상일세",
    "무궁화 삼천리",
    "화려 강산",
    "대한사람 대한으로",
    "길이 보전하세",
    "가을 하늘 공활한데",
    "높고 구름 없이",
    "밝은 달은 우리 가슴",
    "일편단심일세",
    "무궁화 삼천리 화려 강산",
    "대한사람 대한으로 ",
    "길이 보전하세 ",
    "이 기상과 이 마음으로",
    "충성을 다하여",
    "괴로우나 즐거우나",
    "나라사랑하세 ",
    "무궁화 삼천리",
    "화려 강산",
    "대한사람 대한으로",
    "길이 보전하세"
    ]
random.shuffle(word_list)
#
# user_input = input('입력: ')
# word_list = list(user_input)

for q in word_list:
    start_time = time.time()
    user_input = str(input(q + '\n')).strip()
    end_time = time.time() - start_time

    src = break_korean(q)
    tar = break_korean(user_input)
    print(src)
    print(tar)



    if user_input == '/exit':
        break

    correct = 0
    for i, c in enumerate(tar):
        if i >= len(src):
            break
        if c == src[i]:
            correct += 1
    total_len = len(src)
    c = correct / total_len * 100
    e = (total_len - correct) / total_len * 100
    speed  =  (correct / end_time) * 60

    print("속도: {:0.2f} 정확도: {:0.2f} , 오타율: {:0.2f}".format(speed, c, e))








