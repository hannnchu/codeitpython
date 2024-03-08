# 단어장 생성
with open('vocabulary.txt', 'w') as f:
    while True:
        english_word = input('영어 단어를 입력하세요: ')
        if english_word == 'q':
            break

        korean_word = input('한국어 뜻을 입력하세요: ')
        if korean_word == 'q':
            break

        f.write('{}: {}\n'.format(english_word, korean_word))

# 순서대로 단어퀴즈
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]

        # 유저 입력값 받기
        guess = input("{}: ".format(korean_word))

        # 정답 확인하기
        if guess == english_word:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))

# 랜덤으로 단어퀴즈
import random

vocab = {}
with open("vocabulary.txt","r") as f:
    for line in f:
        data = line.strip().split(": ")
        eng, kor = data[0], data[1]
        vocab[eng] = kor

keys = list(vocab.keys())
while True:
    index = random.randint(0, len(keys)-1)
    eng = keys[index]
    kor = vocab[eng]
    chat = input("{}: ".format(kor))
    if chat == eng:
        print("맞았습니다!\n")
    elif chat == "q":
        break
    else:
        print("틀렸습니다. 정답은 {}입니다.".format(eng))