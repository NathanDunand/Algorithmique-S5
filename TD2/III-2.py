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


def prime_nb(n):
    """n est un entier"""

    # Les nombres premiers commencent à 2 donc on enlève tout ce qui précède 2
    if n < 2:
        return f"{n} n'est pas un nombre premier"
    else:
        # on regarde si le nombre n est divisible par un des nombres compris dans l'intervalle [2;n-1]
        for i in range(n - 1, 1, -1):
            if n % i == 0:
                return f"{n} n'est pas un nombre premier"
    return f"{n} est un nombre premier"


if __name__ == "__main__":
    print(prime_nb(5))
    print(prime_nb(12))
    print(prime_nb(-12))
    print(prime_nb(11))
