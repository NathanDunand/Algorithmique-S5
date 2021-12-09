def sequence():

    tot = 0

    # Prend dix nombres
    for _ in range(10):
        tot += int(input("Enter positif int : "))

    # calcul de la moyenne et impression
    print(tot / 10)


if __name__ == "__main__":
    sequence()
