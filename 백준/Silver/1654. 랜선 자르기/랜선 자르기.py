import sys

input = sys.stdin.readline


# 만들 수 있는 랜선의 수
def lst_length(n):
    cnt = 0
    for item in lst:
        cnt += item // n
    return cnt


def binarySearch(start, end, N):
    if start > end:
        return end

    mid = (start + end) // 2
    length = lst_length(mid)
    
    # 만들어야 하는 랜선의 수보다 같거나 크면 최대 길이 찾기 위해서 mid 올려주고 뒷범위에서 찾기
    if length >= N:
        return binarySearch(mid + 1, end, N)
    # 만들어야 하는 랜선의 수보다 작으면 최대 길이 찾기 위해 mid 낮추고 앞범위에서 찾기
    else:
        return binarySearch(start, mid - 1, N)


k, n = map(int, input().split())
lst = []

for _ in range(k):
    lst.append(int(input()))

lst_end = max(lst)

print(binarySearch(1, lst_end, n))
