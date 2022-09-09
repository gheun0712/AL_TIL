# 5582_공통_부분_문자열
# 2022-04-28

"""
주어진 두 문자열의 교집합 문자열 중 가장 긴 문자의 길이를 찾아내는 문제

1. 겹치는 문자열 찾아내기
2. 문자열 길이 비교하기
=> for 문 돌려서 두 문자가 같아지는 경우 저장시켜주기
=> 첫글자인지 파악하는 부분도 포함시켜줘야함
3. 문자열 없는 경우도 포함

pypy3 => 440ms
"""
s1 = input()
s2 = input()
check = [[0] * len(s2) for _ in range(len(s1))]
ans = 0

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            if i == 0 or j == 0:
                check[i][j] = 1
            else:
                check[i][j] = check[i-1][j-1]+1
            ans = max(ans, check[i][j])

print(ans)
