N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []
for i in range(N):
    if X > A[i]:
        result.append(A[i])
print(*result)