n = int(input())
arr= [int(input()) for _ in range(n)]

for i in range(1, n):
    now = arr[i]
    j = i - 1
    while j >= 0:                #for문으로 풀어볼 것. 마지막에 0이냐 -1이냐 비교할 것,.
       if arr[j] > now:
           arr[j + 1] = arr[j]
       else:
           break
       j -= 1
    arr[j + 1] = now

for _ in arr:
    print(_)
