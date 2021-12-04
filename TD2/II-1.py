print("Draw programm")


def draw(n):
    """n est un entier positif"""

    # simple carré : premier for pour les lignes et deuxième for pour les colones de la ligne
    for i in range(n):
        output = ""
        for j in range(n):
            output += "* "
        print(output)
    print("")


if __name__ == "__main__":
    draw(3)
    draw(4)
    draw(0)
    draw(16)
