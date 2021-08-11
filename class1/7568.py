N = int(input())
body = [list(map(int, input().split())) for _ in range(N)]
counts = [1] * N

for i, (xw, xh) in enumerate(body):
    # print(i, xw, xh)
    for j, (yw, yh) in enumerate(body):
        if i == j: continue
        if xw < yw and xh < yh: counts[i] += 1
for x in counts:
    print(x, end = " ")