import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lengths = list(map(int, input().split()))
start = 1
end = max(lengths)
count = 0
max_length = 0

while start <= end:
    mid = (start + end)//2
    count = 0
    for x in lengths:
        sum += x//mid
    if sum < N:
        right = mid -1
    elif sum >= mid + 1
print(max_length)

l   m   r
199 2-- 400
199 2-- 3--
..
..
.
199 200 200
200