N = int(input())
arr = [int(input()) for _ in range(N)]
print(arr)
for i in range(1, N):
    print(i)
    now = arr[i]
    copy = 0
    for j in range(i-1, 0, -1):
        # print(i, now)
        if now < arr[j]:
            arr[j+1] = arr[j]
            copy =  1
        else:
            if copy == 1:
                arr[j+1] = now
            break
        print(arr)
