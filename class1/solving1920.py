# runtime에러가 납니다.

N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
B = int(input())
arr_B = list(map(int, input().split()))

def binary_search(arr, start, end, target):
    mid = (start+end)//2
    if start <= end and mid < N or mid < 0:                        # start가 mid보다 커지면 out 그리고, mid가 N 같아지면 out of range
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            return binary_search(arr, start, mid, target)
        elif arr[mid] < target:
            return binary_search(arr, mid+1, end, target)
    else:
        return 0

for i in range(B):
    print(binary_search(arr, 0, N, arr_B[i]))