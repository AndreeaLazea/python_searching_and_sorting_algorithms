def sequential_search(arr: list, target: float):
    """
    algorithm for sequential search.
    Sequential search is a simple searching algorithm that goes through all elements of the array, searching for
    the target.
    It's average time complexity is O(n), worst time complexity is also O(n), and at best it's O(1), if the first number
    is the one we search for
    :param arr: the list in which we search for the number
    :param target: the number we search for
    :return: the position of the number in the array, if found,a nd -1 if not found
    """
    size = len(arr)
    for i in range(size):
        if arr[i] == target:
            return i
    return -1

def main():
    arr = [10, -4, 5, 6, 23, 400]
    target = 23
    returned_value = sequential_search(arr, target)
    if returned_value == -1:
        print("We couldn't find " + str(target) + "in the array")
    else:
        print(str(target) + " can be found at the " + str(returned_value) + " position in the array.")

if __name__ == "__main__":
    main()