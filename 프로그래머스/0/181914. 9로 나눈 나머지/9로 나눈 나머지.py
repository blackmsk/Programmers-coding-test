def solution(number):
    a = int(number)
    dec = 0
    while a>0:
        dec += a%10
        a = a//10
    answer = dec%9
    return answer