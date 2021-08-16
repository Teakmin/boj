N = int(input())
M = int(input())
errors = list(map(int, input().split()))
channel = 100    # 현재 채널의 위치
fine = 0  # fine으로 고장난 번호가 있으면 1, 없으면 0
count = 0  # count는 N의 자릿수를 세기 위한 것

if N == 100:
    result = 0
else:
    for i in range(0, M):
        if str(errors[i]) in str(N):
            fine = 1
            break
    if fine == 0:
        result = len(str(N))
    elif fine == 1:
        a = N
        while a > 0:
            a = a//10
            count += 1
        i = 10**(count - 1)
        while i >= 10**(count - 1) and i < 10**count:
            for j in range(M):                                                              # 40000번 대에서 4를 못거르고 계속 함. 0 2 4 .. 이 순으로 거르는게 문제인 것 같음......
                if str(errors[j]) in str(i):        #error가 error가 들어있는 i는 패스
                    i += 1
                    break
            if abs(N - channel) > N - i:     # N에 channel보다 i가 더 가까우면 channel에 i 대입
                if N > i:
                    if channel < i:
                        channel = i
                else:
                    if i - N < N - channel:
                        channel = i
                    break
            i += 1
            print(channel)
        result = count + (N - channel)
print(result)
