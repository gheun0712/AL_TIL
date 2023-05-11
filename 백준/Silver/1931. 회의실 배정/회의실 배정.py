n = int(input())
time = []
# 사용 가능 회의 개수
cnt = 0
# 비교해 줄 변수
temp = 0

for _ in range(n):
    time.append(list(map(int, input().split())))

# 종료 시간 기준으로 오름차순 정렬 // 종료시간이 같아면 시작시간 오름차순 정렬
time.sort(key=lambda x: (x[1], x[0]))

for i in time:
    # 앞 타임 끝나는 시간이랑 시작 시간 비교하기
    if i[0] >= temp:
        cnt += 1
        # 끝나는 시간 대입
        temp = i[1]
        
print(cnt)
