def solution(arr, queries):
    answer = []    
    for x in queries:
        s = x[0]
        e = x[1]
        k = x[2]
        new_arr=[]
        for i in range(s,e+1):
            new_arr.append(arr[i])
        new_arr2 = [j for j in new_arr if j>k]
        if new_arr2==[]:
            answer.append(-1)
        else:
            answer.append(min(new_arr2))

    return answer