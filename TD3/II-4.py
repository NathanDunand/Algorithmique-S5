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


def string_search(s1, s2):
    """s1 est la string dans laquelle s2 est recherchée"""
    if len(s2) > len(s1):
        return False

    for i in range(len(s1) - len(s2) + 1):
        print(s1[i : i + len(s2)])
        if s1[i : i + len(s2)] == s2:
            return True
    return False


if __name__ == "__main__":
    print(string_search("Bonjour je suis ici à l'ENSIBS", "je"))
    print(string_search("Bonjour je suis ici à l'ENSIBS", "Bonjour"))
    print(string_search("Bonjour je suis ici à l'ENSIBS", "ENSIBS"))
    print(string_search("Bonjour je suis ici à l'ENSIBS", "SUIS"))
