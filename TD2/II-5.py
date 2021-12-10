def draw(n):
    """n est un entier positif"""

    # on veut simplement des lignes complètes au début et à la fin donc
    # on commence par mettre une ligne complète. Ensuite on rajoute les lignes
    # avec les deux étoiles et le nombre d'espaces nécessaires puis on finit par la
    # ligne complète.
    for i in range(n):
        output = ""

        # première et dernière ligne
        if i == 0 or i == n - 1:
            output += "* " * n
        else:
            output += "* "
            output += "  " * (n - 2)
            output += "* "
        print(output)
    print("")


if __name__ == "__main__":
    draw(3)
    draw(4)
    draw(0)
    draw(16)
