Try = int(input())
for i in range(Try):
    solving = input()
    c = 0
    sum = 0
    for j in range(len(solving)):
        if solving[j]=="O":
            score = c + 1
            c = score
        else:
            score = 0
            c = score
        sum += score
    print(sum)
