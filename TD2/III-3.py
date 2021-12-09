print("Int manipulation programm")


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

    if n < 2:
        return f"{n} n'est pas un nombre premier"
    else:
        # on regarde si le nombre n est divisible par un des nombres compris dans l'intervalle [2;n-1]
        for i in range(n - 1, 1, -1):
            if n % i == 0:
                return f"{n} n'est pas un nombre premier"
    return f"{n} est un nombre premier"


def decomposition(n):
    """n est un entier"""

    if n >= 2:
        ret = f"les facteurs de {n} sont "
        numbers = []
        # le premier nombre premier est 2
        i = 2
        while n > 1:
            while n % i == 0:
                numbers.append(str(i))
                n = n / i
            i += 1
        return ret + ", ".join(numbers)
    else:
        return f"{n} ne peut pas être décomposer en nombre premier ({n} < 2)"


if __name__ == "__main__":
    print(decomposition(5))
    print(decomposition(12))
    print(decomposition(1))
    print(decomposition(27))
