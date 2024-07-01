def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        number = int(i[s:s+l])
        if number > k:
            answer.append(number)
    return answer