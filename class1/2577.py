A = int(input())
B = int(input())
C = int(input())
S = [0] * 10
mul = str(A*B*C)
for i in range(len(mul)):
    S[int(mul[i])] += 1
for i in range(len(S)):
    print(S[i])