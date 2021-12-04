print("Draw programm")


def draw(n):
    """n est un entier positif"""

    # On effectu un décalage plus grand à chaque tour puis on rajoute juste 2 étoiles
    for i in range(n):
        output = "  " * i
        output += "* " * 2
        print(output)
    print()


if __name__ == "__main__":
    draw(3)
    draw(4)
    draw(0)
    draw(16)
