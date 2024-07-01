def solution(arr, queries):
    answer = []
    # dictionary = {int : x for x,int in enumerate(arr)}
    for temp in queries:
        i = arr[temp[0]]
        j = arr[temp[1]]
        arr[temp[0]]=j
        arr[temp[1]]=i
        answer = arr 
             
    return answer