n = int(input())
arr= [int(input()) for _ in range(n)]

for i in range(n - 1):      # 0 ~ n-2
    for j in range(n - (i + 1)):  #
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

for _ in range(n):
    print(arr[_])
