def sequence():
    """Prend en entré 10 entiers positifs"""

    tot = 0
    i = 0
    while i < 10:
        tot += int(input("Enter positive int : "))
        i += 1

    # calcul de la moyenne
    return tot / 10


if __name__ == "__main__":
    print(sequence())
