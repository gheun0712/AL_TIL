# 5052_전화번호_목록
# 2022-04-27

""""
주어진 전화번호 n으로 시작하는 번호에 대해서 일관성이 없다고 봄
그러므로 해당 글자가 포함되어 있는지만 확인해주면 되는 문제!
스트링에서 문자 비교할때 쓰는 startswith  메서드 사용!
string. startswith('시작하는문자')
string. startswith('시작하는문자', 위치)

pypy3 => 300ms
"""
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num_lst = []
    for _ in range(n):
        num = input()
        num_lst.append(num)

    num_lst.sort()
    check = False

    for i in range(len(num_lst)-1):
        if num_lst[i+1].startswith(num_lst[i]):
            print('NO')
            check = True
            break

    if not check:
        print('YES')