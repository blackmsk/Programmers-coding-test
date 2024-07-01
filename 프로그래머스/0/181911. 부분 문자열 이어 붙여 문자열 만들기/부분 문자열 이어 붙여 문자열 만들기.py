def solution(my_strings, parts):
    answer = ''
    index = 0   
    for i, j in parts:
        answer += my_strings[index][i:j+1]   
        index += 1         
    return answer