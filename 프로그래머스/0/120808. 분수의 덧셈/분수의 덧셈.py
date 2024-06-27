def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numer, denom):
    divisor = gcd(numer, denom)
    return numer // divisor, denom // divisor

def solution(numer1, denom1, numer2, denom2):
    answer = [0,0]
    for i in range(max(denom1, denom2), (denom1 * denom2) + 1):
        if i % denom1 == 0 and i % denom2 == 0:
            lcm = i
            break
    answer[0] = numer1 * (lcm//denom1) + numer2 * (lcm//denom2)
    answer[1] = lcm
    return simplify_fraction(answer[0], answer[1])