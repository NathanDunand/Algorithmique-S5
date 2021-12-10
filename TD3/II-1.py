def sequential_search(arr, n):
    """arr est un tableau d'entier et n est la valeur recherchée"""

    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1


if __name__ == "__main__":
    arr = [12, 4, 59, 12, 52, 13, 93, 0, 5, 12, 4, 12, 53, 994, 124, 24, 50]
    print(sequential_search(arr, 12))
    print(sequential_search(arr, 5))
    print(sequential_search(arr, 50))
    print(sequential_search(arr, 666))
