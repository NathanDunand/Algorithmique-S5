def draw(n):
    """n est un entier positif"""

    # Le n correspond à la hauteur de la pyramide
    # le but c'est d'enlever petit à petit le nombre d'espace et d'augmenter
    # petit à petit le nombre d'étoile de chaque côté pour construire la pyramide
    for i in range(n):
        output = "  " * (n - i - 1)
        output += "* " * (2 * i + 1)
        print(output)
    print()


if __name__ == "__main__":
    draw(3)
    draw(4)
    draw(0)
    draw(16)
