def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#================================================================================

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr)//2
    pivot = arr[meio]
    left = [x for x in arr[:meio] + arr[meio+1:] if x <= pivot]
    right = [x for x in arr[:meio] + arr[meio+1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)