S = input()
count = 0
S = S.upper()
S.replace(" ", "")
list = list(S)
for i in range(len(list)):
    fre = list.count(list[i])
    if fre > count:
        count = fre
        res = list[i]
        notOne = 0
    elif fre == count:
        if res == list[i]:
            pass
        else:
            notOne += 1

if notOne == 0:
    print(res)
else:
    print("?")