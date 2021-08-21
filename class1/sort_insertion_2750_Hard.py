N = int(input())
arr = [int(input()) for _ in range(N)]

for i in range(1, N):
    now = arr[i]
    copy = 0
    for j in range(i-1, -1, -1):
        if now < arr[j]:
            arr[j+1] = arr[j]
            copy = 1
        else:
            arr[j+1] = now
            break
        if copy == 1 and j == 0:
            arr[0] = now
for _ in range(N):
    print(arr[_])