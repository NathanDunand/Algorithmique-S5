def sequence():

    tot = 0
    for _ in range(10):
        tot += int(input("Enter positive int : "))

    # calcul de la moyenne
    return tot / 10


if __name__ == "__main__":
    print(sequence())
