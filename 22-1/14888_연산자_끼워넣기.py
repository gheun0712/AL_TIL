# 14888_연산자_끼워넣기
# 2022-04-06
"""
재귀함수를 이용해서 풀어보기!
몫만 구하기 위해서 //을 사용했는데 음수 몫 부분에서 값이 제대로 나오지 않는 경우가 발생
이를 해결하기 위해서 /을 사용했지만 float 문제 발생
그래서 int()로 형변환을 시켜주었다
수영장 문제와 비슷한 문제로 해당 개념을 이용해서 빨리 풀었음!
"""


def dfs(i, res, add, minus, multi, div):
    global n

    if i == n:
        ans.append(res)

    if add:
        dfs(i + 1, res + lst[i], add - 1, minus, multi, div)
    if minus:
        dfs(i + 1, res - lst[i], add, minus - 1, multi, div)
    if multi:
        dfs(i + 1, res * lst[i], add, minus, multi - 1, div)
    if div:
        dfs(i + 1, int(res / lst[i]), add, minus, multi, div - 1)


n = int(input())
lst = list(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈 연산자 가능 갯수
add, minus, multi, div = map(int, input().split())
ans = []

dfs(1, lst[0], add, minus, multi, div)

print(max(ans))
print(min(ans))
