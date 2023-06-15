s = str(input())
s = list(s)
temp = []
n = int(input())

for _ in range(n):
    editor = str(input())
    if editor[0] == 'P':
        s.append(editor[2])
    elif editor[0] == 'L' and s != []:
        temp.append(s.pop())
    elif editor[0] == 'D' and temp != []:
        s.append(temp.pop())
    elif editor[0] == 'B' and s != []:
        s.pop()

print("".join(s + list(reversed(temp))))