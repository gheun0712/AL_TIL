# 9935_문자열_폭발
# 2022-04-26

"""
문자열에 폭발문자가 있는지 확인하고 문자 없애기!
조건만 잘 세우면 완성할 수 있는 스트링 문제인듯!
슬라이싱 이용하고 del 함수를 사용해보았음!
임시 리스트에 있는 문자들이 폭발문자일때 >>
폭탄 문자열의 크기만큼 조합해서 폭탄이랑 같으면 없애기

pypy3 => 380ms
"""

word = input()
bomb = input()
temp = []

for i in word:
    temp.append(i)
    if temp and temp[-1] == bomb[-1]:
        if ''.join(temp[-len(bomb):]) == bomb:
            del temp[-len(bomb):]

if temp:
    for j in temp:
        print(j, end='')
else:
    print('FRULA')
