def heap_sort(array):
    n = len(array) - 1
    for i in range(N//2, 0, -1):
        heapify(array, i, n)
        print(array)
        for i in range(n - 1, 0, -1):
            array[1], array[i + 1] = array[i +1], array[1]
            heapify(array, 1, i)
            print(array)

def heapify(array, start, end):
    v = array[start]
    i = 2*start
    while i < end:
        if i < end and array[i] < array[i + 1]:
            i += 1
            if v>= array[i]:
                break
            else:
                array[i//2] = array[i]
            i *= 2
        array[i//2] = v

a = [-1, 4, ,8,5,6,1,3,7,2]
heap_sort(a)
