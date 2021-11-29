print("Sequence Programme")


def Sequence():

    tot = 0

    # Prend dix nombres
    for i in range(10):
        tot += int(input("Enter positif int : "))

    # calcul de la moyenne et impression
    print(tot / 10)


if __name__ == "__main__":
    Sequence()
