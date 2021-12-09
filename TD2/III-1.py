def inverse_nb(n):
    """n est un entier"""
    reverse = 0
    factor = 1

    # Si le nombre est négatif on calcule sa valeur absolue et on
    # garde le facteur -1
    if n < 0:
        n = -1 * n
        factor = -1
    while n > 0:
        remaind = n % 10
        reverse = (reverse * 10) + remaind
        n = int(n / 10)
    return reverse * factor


if __name__ == "__main__":
    print(inverse_nb(5))
    print(inverse_nb(12))
    print(inverse_nb(-12))
    print(inverse_nb(1234567))
