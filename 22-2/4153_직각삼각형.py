# 2022-10-22
# 4153_직각삼각형

while True:

    tri = sorted(list(map(int, input().split())))

    if tri[0] == 0 & tri[1] == 0 & tri[2] == 0:
        break

    elif tri[2] * tri[2] == tri[0] * tri[0] + tri[1] * tri[1]:
        print("right")

    else:
        print("wrong")
