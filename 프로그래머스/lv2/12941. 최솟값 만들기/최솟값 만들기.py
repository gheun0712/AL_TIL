#최소값 * 최대값일때 최솟값 나옴
def solution(A,B):
    ans = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        ans += A[i]*B[i]
    return ans