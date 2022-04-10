# 14891_톱니바퀴
# 2022-04-11
'''

'''
status = [list(map(int, input().split()))for _ in range(4)]
k = int(input())
lst = [list(map(int, input().split())) for _ in range(k)]

for num, direction in lst:
    print(num, direction)

