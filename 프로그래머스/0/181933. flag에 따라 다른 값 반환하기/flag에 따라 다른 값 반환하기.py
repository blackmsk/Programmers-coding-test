def solution(a, b, flag):
    answer = 0
    if str(flag)=="True":
        answer = int(a)+int (b)
    elif str(flag)=='False':
        answer = int(a)-int(b)
    return answer