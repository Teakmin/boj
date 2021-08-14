N = 5456
channel = 100    # 현재 채널의 위치
M = int(input())
errors = list(map(int, input().split()))
fine = 0  # fine으로 고장난 번호가 있으면 1, 없으면 0

for i in range(M):
    if str(errors[i]) in str(N):
        fine = 1
if fine == 0:
    result = 1
elif fine == 1:
    a = N
    count = 0
    while a > 0:
        a = a//10
        count += 1
    while i >= 10**(count - 1) and i < 10**count:
        for j in range(M):
            if str(errors[j]) in str(i):
                i += 1
        if N- channel > N - i:
            channel = i
print(channel)


