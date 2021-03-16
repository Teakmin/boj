N = int(input())
M = 0
sum = 0
score = list(map(int, input().split()))
for i in range(len(score)):
    if M < score[i]:
        M = score[i]
for i in range(len(score)):
    Newscore = (score[i]/M) * 100
    sum += Newscore
    Newscore = 0
print(sum/N)