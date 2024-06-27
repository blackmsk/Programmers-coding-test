import math
def solution(price):
    answer = 0
    if price >= 500000:
        answer = price * 0.8
    elif 300000<=price<500000:
        answer = price * 0.9
    elif 100000<=price<300000:
        answer = price * 0.95
    else:
        answer = price
    return math.floor(answer)