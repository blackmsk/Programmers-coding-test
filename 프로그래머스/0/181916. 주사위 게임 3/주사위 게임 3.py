def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice.sort()
    abcd = dict()
    answer = 0
    
    for num in dice:
        if num not in abcd:
            abcd[num] = 1
        else:
            abcd[num] += 1
            
    abcd = sorted(abcd, key=lambda x:abcd[x])
    print (abcd)
    
    if len(abcd)==1:
        answer = 1111 * a
    elif len(abcd)==2: 
        if dice.count(abcd[0]) in [1,3]:
            answer = (10 * abcd[1] + abcd[0]) ** 2
        else:
            answer = (abcd[0] + abcd[1]) * abs(abcd[0] - abcd[1])
    elif len(abcd)==3:
        answer = abcd[0] * abcd[1]
        
    else:
        answer = min(dice)
        
    return answer