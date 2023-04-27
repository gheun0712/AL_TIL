import math

def solution(numer1, denom1, numer2, denom2):
    bottom = denom1 * denom2
    top = denom1 * numer2 + denom2 * numer1
    
    common = math.gcd(bottom, top)
    
    answer = [top/common, bottom/common]
    return answer