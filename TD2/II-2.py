def draw(n):
    """n est un entier positif"""

    # simple triangle : premier for pour les lignes et deuxième for pour les colones de la ligne
    # *
    # * *
    # * * *
    # On remarque que le nombre de colones correspond au numéro de la ligne (en commençant par 1)
    for i in range(n):
        output = ""
        for j in range(i + 1):
            output += "* "
        print(output)
    print("")


if __name__ == "__main__":
    draw(3)
    draw(4)
    draw(0)
    draw(16)
