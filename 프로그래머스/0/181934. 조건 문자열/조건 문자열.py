def solution(ineq, eq, n, m):
    answer = 0
    if eq=="=" and ineq==">":
        answer = int(bool(n==m or n>m))
    elif eq=="=" and ineq=="<":
        answer = int(bool(n==m or n<m))
    elif eq=="!" and ineq==">":
        answer = int(bool(n>m))
    elif eq=="!" and ineq=="<":
        answer = int(bool(n<m)) 
    return answer