def sequence():
    """Prend en entré 10 entiers positifs"""

    tot = 0
    i = 0
    while i < 10:
        tot += int(input("Enter positif int : "))
        i += 1

    # calcul de la moyenne et impression
    print(tot / 10)


if __name__ == "__main__":
    sequence()
