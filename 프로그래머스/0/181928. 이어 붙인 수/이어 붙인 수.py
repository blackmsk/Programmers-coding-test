def solution(num_list):
    num_odd, num_even = "",""
    for num in num_list:
        if num%2==1:
            num_odd+=str(num)
        else:
            num_even+=str(num)
    return int (num_odd) + int (num_even)