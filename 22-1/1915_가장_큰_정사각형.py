# 1915_가장_큰_정사각형
# 2022-05-16

"""
전체 크기가 n*m인 직사각형
1인 곳을 찾아서 정사각형 완성하기
DP 사용하기!
기준 인덱스 기준으로 좌,우,좌우가 1이면 정사각형임
기준 인덱스 제외한 나머지 3개 인덱스의 min값을 구해주기

PyPy3 => 204ms
Python3 => 1344ms
"""

n, m = map(int, input().split())
arr = []
res = 0

for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and arr[i][j] != 0:
            arr[i][j] += min(arr[i-1][j-1], arr[i][j-1], arr[i-1][j])
        res = max(res, arr[i][j])

print(res * res)