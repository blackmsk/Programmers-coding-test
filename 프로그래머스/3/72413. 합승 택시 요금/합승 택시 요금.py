def solution(n, s, a, b, fares):
    answer = 100001 * n #값 초기화
    M = 100001 * n #값 초기화
    
    table = [[M for x in range(n+1)] for x in range(n+1)] #2차원 table 정의
    for i,j,fare in fares: #table 정의, 값은 요금: fare 변수 설정
        table[i][j] = fare
        table[j][i] = fare
    
    #table 정의, 자기자신은 0, 그 자리이기 때문에 요금 x
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                table[i][j] = 0
                
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if table[i][j] > table[i][k]+table[k][j]:   #새로운 추가 경로가 비용이 더 저렴하다면,
                    table[i][j] = table[i][k]+table[k][j]   #table update
                    
    for i in range(1,n+1):
        answer = min(answer,table[i][s]+table[i][a]+table[i][b]) #합승요금 vs 각자 요금 계산, 합승요금이 저렴하다면, 합승요금 적용
    
    return answer