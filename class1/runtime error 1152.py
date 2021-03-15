S = input()
if S[0] == " ":
    S = S[1:]
if S[-1] == " ":
    S = S[:-1]
a = S.count(" ")
print(a + 1)