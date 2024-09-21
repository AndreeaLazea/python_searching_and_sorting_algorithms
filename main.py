def sequential_search(arr: list, target: float):
    """
    algorithm for sequential search.
    Sequential search is a simple searching algorithm that goes through all elements of the array, searching for
    the target.
    It's average time complexity is O(n), worst time complexity is also O(n), and at best it's O(1), if the first number
    is the one we search for
    :param arr: the list in which we search for the number
    :param target: the number we search for
    :return: the position of the number in the array, if found,and -1 if not found
    """
    size = len(arr)
    for i in range(size):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr: list, target: int):
    """
    algorithm for binary search.
    Binary search can only be used on a sorted array.
    It repeatedly divides the search interval in half.
    The average time complexity is O(log n), the worst one is O(log n) and the best one is O(1).
    It can only be O(1) if the number searched for is in the middle of the array.
    :param arr: the list in which we search for the number
    :param target: the number we search for
    :return: the position of the number in the array if found, and -1 if not found
    """
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def selection_sort(arr: list):
    """
    Selection sort algorithm sorts an array by repeatedly selecting the smallest element from the array and placing it
    in the correct order.
    The average, best and worst time complexity is O(n2)
    :param arr: the array that needs sorting
    :return: the sorted array
    """
    size = len(arr)
    for i in range(size):
        min_indx = i
        for j in range(i+1, size):
            if arr[j] < arr[min_indx]:
                min_indx = j
        aux = arr[i]
        arr[i] = arr[min_indx]
        arr[min_indx] = aux
    return arr

def bubble_sort(arr: list):
   size = len(arr)
   for i in range(size - 1):
       for j in range(0, size - i - 1):
           if arr[j] > arr[j+1]:
               aux = arr[j]
               arr[j] = arr[j+1]
               arr[j+1] = aux
   return arr


def quick_sort(arr: list, low: int, high: int):
    pass




def main():
    arr = [10, -4, 5, 6, 23, 400]
    target = 23

    print("Sequential search: ")
    sequential_returned_value = sequential_search(arr, target)
    if sequential_returned_value == -1:
        print("We couldn't find " + str(target) + "in the array")
    else:
        print(str(target) + " can be found at the " + str(sequential_returned_value) + " position in the array.")

    print("Binary Search: ")
    binary_returned_value = binary_search(arr, target)
    if binary_returned_value == -1:
        print("We couldn't find " + str(target) + "in the array")
    else:
        print(str(target) + " can be found at the " + str(binary_returned_value) + " position in the array.")

    print("Selection Sort: ")
    arr_unsorted = [65, -3, 45, 0.7, 7, 12233]
    print("The unsorted array: ")
    print(arr_unsorted)
    arr_sorted = selection_sort(arr_unsorted)
    print("The sorted array: ")
    print(arr_sorted)

    print("Bubble Sort: ")
    arr_unsorted = [65, -3, 45, 0.7, 7, 12233]
    print("The unsorted array: ")
    print(arr_unsorted)
    arr_sorted = bubble_sort(arr_unsorted)
    print("The sorted array: ")
    print(arr_sorted)


if __name__ == "__main__":
    main()
