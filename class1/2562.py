Numbers = []
for i in range(9):
    N = int(input())
    Numbers.append(N)
max = max(Numbers)
location = Numbers.index(max)
print(max)
print(location + 1)