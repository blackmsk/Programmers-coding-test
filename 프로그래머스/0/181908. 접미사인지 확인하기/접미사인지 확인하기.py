def solution(my_string, is_suffix):
    answer = 0
    strings = [my_string[i:] for i in range(len(my_string))]
    if is_suffix in strings:
        return 1
    else:
        return 0