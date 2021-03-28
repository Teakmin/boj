N = int(input())
string = "*"
for i in range(N):
    txt = "*" * (i+1)
    print(txt.rjust(N))