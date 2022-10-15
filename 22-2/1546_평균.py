# 2022-10-15
# 1546_평균

N = int(input())
score = list(map(int, input().split()))
best = max(score)
sum = 0

for i in range(N):
    score[i] = score[i] / best * 100
    sum += score[i]

print(sum / N)
