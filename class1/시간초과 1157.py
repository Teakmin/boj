S = input()
S = S.upper()
alpha = [0] * 26
for i in S:
    alpha[ord(i)-65] += 1
max=max(alpha)
if alpha.count(max) > 1:
    print("?")
else:
    print(chr(alpha.index(max) + 65))
