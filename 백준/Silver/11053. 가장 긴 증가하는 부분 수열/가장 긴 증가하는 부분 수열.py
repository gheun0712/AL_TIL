N = int(input())
lst = list(map(int, input().split()))
# DP 돌려서 체크할 리스트 만들어주기
check = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        # 기준 인덱스보다 앞 인덱스들 값 비교해주기
        # 앞 인덱스보다 기준 인덱스의 값이 크면 조건 성립
        if lst[i] > lst[j]:
            # 가장 큰값을 비교해서 체크리스트에 저장해야 함
            check[i] = max(check[i], check[j] + 1)

print(max(check))