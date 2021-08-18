n = int(input())
arr= [int(input()) for _ in range(n)]

for i in range(n -1):      # 0 ~ n-2
    min_idx = i
    for j in range(i, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

for _ in range(n):
    print(arr[_])
