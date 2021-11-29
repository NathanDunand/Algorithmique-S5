print("Sequence Programme")

# Prend en entré 10 entiers positifs
def Sequence():
    """Prend en entré n entiers positifs, -1 étant le marqueur de fin"""

    tot = 0
    tot_number = 0
    finish = False
    while not finish:
        input_value = int(input("Enter positif int or -1 to stop: "))
        if input_value == -1:
            finish = True
        else:
            tot += input_value
            tot_number += 1

    # calcul de la moyenne et impression
    print(tot / tot_number)


if __name__ == "__main__":
    Sequence()
