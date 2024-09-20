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


if __name__ == "__main__":
    main()
