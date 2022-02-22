# 2559_수열
# 2022-02-22

N, K = map(int, input().split())
Temp = list(map(int, input().split()))
lst = [0] * (N + 1)

# 누적합을 구해줌
for i in range(1, N + 1):
    lst[i] = lst[i - 1] + Temp[i - 1]

# 최저점으로 잡아줘야 최고값 비교 가능
max_temp = (-100 * K) - 1

# 누적합에서 필요한 구간합 가져오기 위해서 필요한 구간 남기고 뺴줌
for j in range(N - K + 1):
    max_temp = max(max_temp, lst[j + K] - lst[j])

print(max_temp)