from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
# print(nums)
_max = 0
for x in combinations(nums, 3):
    _sum = sum(x)
    if M >= _sum > _max:_max = _sum
print(_max)
