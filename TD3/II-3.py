def sequential_search(arr, n):
    """arr est un tableau d'entier et n est la valeur recherchée"""

    # on parcourt tout le tableau jusqu'à trouver ou non la valeur recherchée
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1


def binary_search(arr, n, left, right):
    """arr est un tableau d'entier trié et n est la valeur recherchée"""
    middle = (left + right) // 2

    if left == right:
        return -1

    # le tableau est trié donc à chaque tour de recursivité on divise par deux le nombre de valeur possible
    if arr[middle] > n:
        return binary_search(arr, n, left, middle)
    elif arr[middle] < n:
        return binary_search(arr, n, middle + 1, right)
    else:
        return middle


def binary_search_init(arr, n):
    """arr est un tableau d'entier trié et n est la valeur recherchée"""
    return binary_search(arr, n, 0, len(arr))


if __name__ == "__main__":
    arr = [0, 4, 4, 5, 12, 12, 12, 12, 13, 24, 50, 52, 53, 59, 93, 124, 994]
    print(binary_search_init(arr, 12))
    print(binary_search_init(arr, 5))
    print(binary_search_init(arr, 50))
    print(binary_search_init(arr, 666))
