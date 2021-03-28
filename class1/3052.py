Numbers = []
result = []
for i in range(0,10):
    Number = int(input())
    Numbers.append(Number)
for i in range(len(Numbers)):
    j = Numbers[i] % 42
    if j not in result:
        result.append(j)
print(len(result))