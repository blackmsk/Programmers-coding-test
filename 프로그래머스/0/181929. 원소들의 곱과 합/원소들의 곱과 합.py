def multiply(num_list):
    result = 1
    for num in num_list:
        result *= num
    return result

def solution(num_list):
    if multiply(num_list)<sum(num_list)**2:
        return 1
    else: return 0