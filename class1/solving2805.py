#시간초과 (googling하고 고친건데도 시간초과)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 9
end = max(trees)
maxcut = 0

while start <= end:
    mid = (start + end)//2
    sum = 0

    for tree in trees:
        if tree-mid < 0:
            continue
        sum += tree-mid

    if sum == M:
        print(mid)
        sys.exit()
    elif sum > M:
        if maxcut < mid:
            maxcut = mid
        start = mid + 1
    else:
        end = mid - 1
print(maxcut)
