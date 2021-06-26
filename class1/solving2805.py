N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
for x in range(max(arr), min(arr), -1):
    for i in range(N):
        if arr[i] > x:
            sum += arr[i]-x
            if i == N-1:
                if sum == M:
                    print(x)
                    break
                else:
                    sum = 0