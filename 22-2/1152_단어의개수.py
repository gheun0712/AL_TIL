# 2022-10-15
# 1152_단어의 개수

str = input()
str = str.strip()

if str == '':
    print(0)
else:
    print(str.count(' ')+1)