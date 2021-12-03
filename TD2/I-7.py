print("Sequence Programme")


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

        # Nombre de suite croissante
        if previous_one != None and input_value != -1:
            if previous_one[0] >= input_value:
                previous_one[1] += 1
            previous_one[0] = input_value

    # interface utilisateur / menu
    stop = False
    while not stop:
        print(
            f"a. afficher la moyenne\nb. afficher le minimum\nc. afficher le maximum\nd. afficher le nombre d’occurrences du 1er entier\ne. afficher le nombre de monotonies\nq. quitter"
        )

        user_choice = input("Choix : ")

        if user_choice == "a":
            print(f"average : {tot / tot_number}")
        elif user_choice == "b":
            print(f"min : {min_value}")
        elif user_choice == "c":
            print(f"max : {max_value}")
        elif user_choice == "d":
            print(f"{occurency[0]} occurency : {occurency[1]}")
        elif user_choice == "e":
            print(f"sub-sequence : {previous_one[1]}")
        elif user_choice == "q":
            stop = True
        else:
            print(f"not a valid option")


if __name__ == "__main__":
    sequence()
