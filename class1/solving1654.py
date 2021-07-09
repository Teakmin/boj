import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lengths = list(map(int, input().split()))
start = 0
end = max(lengths)
count = 0
max_length = 0

while start <= end:
    mid = (start + end)//2
    count = 0
        if tree - mid < 0:
            continue
        while tree-mid > 0:
            tree = tree-mid
            count+= 1
    if N == count:
        if mid > max_length:
            max_length = mid
    elif N < count:
        end = mid -1
    else:
        if max_length < mid:
            max_length = mid
        start = mid + 1
print(max_length)
