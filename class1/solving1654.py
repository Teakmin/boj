import sys
input = sys.stdin.readline

K, M = map(int, input().split())
lengths = list(map(int, input().split()))
start = 0
end = max(lengths)

while start <= end:
    mid = (start + end)//2
    for tree in lengths:
        while tree >0:
            if tree-mid>0:
                result+= 1
            tree = tree-mid
    if result==N:
        print(mid)
        sys.exit()
    elif result > N:
        if max_length < mid:
            max_length= mid
        start = mid + 1
    else:
        end = mid -1
print(max_length)S