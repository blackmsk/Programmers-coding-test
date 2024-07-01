def digit_length(n):
    ans = 0
    while n:
        n //= 10
        ans += 1
    return ans

def solution(l, r):
    answer = []
    for i in range(2**(digit_length(l)-1),2**(digit_length(r))):
        a = format (i, 'b')
        b = a.replace('1','5')
        if int(b)<=r:
            if int(b)>=l:
                answer.append(int(b))
        else:
            break
    if answer==[]:
        answer.append(-1)
    return answer
