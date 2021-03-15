N = int(input())
score = list(map(int, input().split(' ')))
M = max(score)
sum = 0
for i in range(N):
    S = int(score[i]/M * 100)
    sum += S
result = sum/N
print(result)