N, K = map(int, input().split())
d = {0: 0}

for _ in range(N):
    current_w, current_v = map(int, input().split())
    temp = {}
    for w, v in d.items():
        if current_w + w <= K and current_v + v > d.get(current_w + w, 0):
            temp[current_w + w] = current_v + v
    d.update(temp)
print(max(d.values()))