 N = int(input())
 M = int(input())
 arr = list(map(int,input().split()))
 arr = sorted(arr)
 min = min(arr)
 max = max(arr)

 mid = (max + min)//2
 sum = 0
 while result != 1:
     for i in range(N):
         if arr[i] > mid:
             sum += arr[i] - mid
             if i == N-1:
                 if sum == M:
                     result = 1    #while문  문제가 생김
                 else:
                     result = 0
    if sum < M:
        mid = (arr[])