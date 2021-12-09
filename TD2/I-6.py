def sequence():
    """Prend en entré n entiers positifs, -1 étant le marqueur de fin"""

    tot = 0
    tot_number = 0
    min_value, max_value = None, None
    finish = False
    occurency = None
    previous_one = None
    while not finish:
        input_value = int(input("Enter positif int or -1 to stop: "))
        if input_value == -1:
            # condition de fin
            finish = True
        else:
            # Premier tour de boucle
            if min_value == None:
                min_value, max_value = input_value, input_value
                occurency = [input_value, 0]
                previous_one = [input_value, 0]
            # Si l'input est le nouveau min
            elif input_value < min_value:
                min_value = input_value
            # Si l'input est le nouveau max
            elif input_value > max_value:
                max_value = input_value

            # Nombre d'occurence de la première valeur rentrée
            if input_value == occurency[0]:
                occurency[1] += 1

            tot += input_value
            tot_number += 1

        # Nombre de suite strictement croissante
        if previous_one != None:
            if previous_one[0] >= input_value:
                previous_one[1] += 1
            previous_one[0] = input_value

    # calcul de la moyenne et impression
    print(
        f"average : {tot / tot_number}\nmin : {min_value}\nmax : {max_value}\n{occurency[0]} occurency : {occurency[1]}\nsub-sequence : {previous_one[1]}"
    )


if __name__ == "__main__":
    sequence()
