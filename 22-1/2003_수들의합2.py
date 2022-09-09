# 2003_수들의합2
# 2022-06-06

"""
투포인터를 적용해서 풀어야 시간초과 x
정해진 구간의 합이 m보다 작을 경우 end를 1 증가시켜 구간을 늘여준다
m과 같으면 찾았으니 카운트 갯수 올려준다
m보다 커지면 start값을 줄여 구간을 옮겨준다
PyPy3 => 124ms
"""

n, m = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
x = 0
end = 0

for start in range(n):
    while x < m and end < n:
        x += lst[end]
        end += 1

    if x == m:
        cnt += 1
    x -= lst[start]

print(cnt)