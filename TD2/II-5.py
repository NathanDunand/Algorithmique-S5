def draw(n):
    """n est un entier positif"""

    # simple carré : premier for pour les lignes et deuxième for pour les colones de la ligne
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
