def draw(n):
    """n est un entier positif"""

    # Le n correspond à la hauteur du losange
    # Cet algo fonctionne comme le II-3 simplement on divise le n par 2
    # et on implemente l'algo de manière inversé pour faire la partie inférieur
    # du losange

    g = int(n / 2 if n % 2 == 0 else n / 2 + 1)

    # partie supérieure
    for i in range(g):
        output = "  " * (n - i - 1)
        output += "* " * (2 * i + 1)
        print(output)
    # partie inférieure
    for i in range(n - g, 0, -1):
        output = "  " * (n - i)
        output += "* " * (2 * i - 1)
        print(output)


if __name__ == "__main__":
    draw(5)
    draw(16)
