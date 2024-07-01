def solution(n, control):
    for index in control:
        if index =="w":
            n+=1
        elif index=="s":
            n-=1
        elif index=="d":
            n+=10
        elif index=="a":
            n-=10
    return n
