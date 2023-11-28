def quick_sort(self, arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr)//2
    pivot = arr[meio]
    left = [x for x in arr[:meio] + arr[meio+1:] if x <= pivot]
    right = [x for x in arr[:meio] + arr[meio+1:] if x > pivot]

    return self.quick_sort(self, left) + [pivot] + self.quick_sort(self, right)