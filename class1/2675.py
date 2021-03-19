T = int(input())
testcase = 0
for j in range(T):
    R, S = input().split()
    res = ""
    for i in range(len(S)):
        New = S[i] * int(R)
        res += New
    print(res)