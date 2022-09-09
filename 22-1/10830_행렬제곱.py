# 10830_행렬제곱
# 2022-05-19

import sys


def mulmatrix(m1, m2):
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += m1[i][k] * m2[k][j]  # 행렬의 곱셈
                result[i][j] %= 1000

    return result


def devide(b, matrix):
    if b == 1:
        return matrix

    else:  # 제곱 수가 2로 나누어 떨어진다면 반으로 가를 수 있다
        if b % 2 == 0:
            matrix = devide(b // 2, matrix)
            return mulmatrix(matrix, matrix)

        else:  # 제곱 수가 2로 나누어 떨어지지 않는다면 1 을 빼준 다음에 반으로 가를 수 있게 만듬
            matrix = devide(b - 1, matrix)
            return mulmatrix(first_matrix, matrix)


N, B = map(int, sys.stdin.readline().split())
first_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for col in range(N):
    for row in range(N):
        # 1000 보다 큰 수가 입력될 경우를 방지하기 위해 한번 더 거름
        print(devide(B, first_matrix)[col][row] % 1000, end=" ")
    print()

