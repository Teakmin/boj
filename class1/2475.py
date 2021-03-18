Num = list(map(int, input().split()))
sum = 0
for i in range(len(Num)):
    sum += (Num[i])**2
result = sum%10
print(result)