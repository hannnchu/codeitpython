# 번호 뽑기
from random import randint
def generate_numbers(n):
    numbers = list()
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers

# 당첨 번호
def draw_winning_numbers():
    win = generate_numbers(7)
    return sorted(win[:6]) + win[6:]

# 일치하는 번호 개수
def count_matching_numbers(numbers, winning_numbers):
    cnt = 0
    for i in winning_numbers:
        if i in numbers:
            cnt += 1

    return cnt

# 당첨금
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 100000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
