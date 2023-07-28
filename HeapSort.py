def heap_sort_max(arr):
    build_max_heap(arr)
    n = len(arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)


def heap_sort_min(arr):
    build_min_heap(arr)
    n = len(arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heapify(arr, i, 0)


def build_max_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def build_min_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)


def max_heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def min_heapify(arr, n, i):
    smallest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child

    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


# Test the Heap Sort implementation
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)

    heap_sort_max(arr)
    print("Heap Sort using Maximum Heap (Ascending order):", arr)

    heap_sort_min(arr)
    print("Heap Sort using Minimum Heap (Descending order):", arr)
