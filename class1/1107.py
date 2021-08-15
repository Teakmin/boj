N = int(input())
channel = 100    # 현재 채널의 위치
M = int(input())
errors = list(map(int, input().split()))
fine = 0  # fine으로 고장난 번호가 있으면 1, 없으면 0

if N == 100:
    result = 1
for i in range(M):
    if str(errors[i]) in str(N):
        fine = 1
if fine == 0:
    result = len(str(N))
elif fine == 1:
    a = N
    count = 0
    while a > 0:
        a = a//10
        count += 1
    i = 10**(count - 1)
    while i >= 10**(count - 1) and i < 10**count:
        for j in range(M):                      # errors에 있는 수들이 i에 포함되면 continue
            if str(errors[j]) in str(i):
                i += 1
                continue
        if N - channel > N - i:  # N에 channel보다 i가 더 가까우면 channel에 i 대입
            if N > i:
                if channel < i:
                    channel = i
            else:
                if i - N < N - channel:
                    channel = i
                break
        i += 1
    # channel은 갈 수 있는 가장 가까운 수
    result = count + (N - channel)

# N이 100보다 크다는 가정에서 한것
