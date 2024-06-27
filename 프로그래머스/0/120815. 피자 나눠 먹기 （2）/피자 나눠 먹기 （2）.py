def solution(n):
    if n%6 == 0: return n//6
    else:
        for i in range(max(6, n), (6 * n) + 1):
            if i % 6 == 0 and i % n == 0:
                return i//6