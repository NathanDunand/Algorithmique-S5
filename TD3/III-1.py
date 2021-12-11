def pyramid_game():
    """Jeux de la pyramide, retour le numéro du joueur gagnant : 1 pour le joueur 1 et 2 pour le joueur 2"""

    # On récupère la liste de mots valides (liste non-exhaustive)
    fi = open("TD3/III-dico.txt", "r")
    words = []
    for word in fi.readlines():
        words.append(word[:-1].lower())

    # False : le premier joueur, True l'autre
    p_playing = False
    word_exists = True
    previous_word = None
    # Une boucle pour le jeu
    # Entre deux mots il y a une différence de 1 en longeur mot1 - mot2 = 1
    while word_exists:
        if previous_word == None:
            previous_word = input(f"P{int(p_playing)+1}- Enter the first french word: ")
            p_word = previous_word
        else:
            p_word = input(f"P{int(p_playing)+1}- Enter a french word: ")
            if not is_correct_word(previous_word, p_word):
                return int(not p_playing) + 1

        word_exists = False
        for w in words:
            if p_word == w:
                word_exists = True
                break

        p_playing = not p_playing
        previous_word = p_word
    return int(p_playing) + 1


def is_correct_word(word1, word2):
    # On soustrait le premier mot au deuxième se qui permet de récupérer la/les
    # lettre(s) différentes. Si le nombre de lettres différentes n'est pas égal
    # à 1 alors c'est que le deuxième mot ne correspond à un mot valide pour le
    # jeu de la pyramide
    word1, word2 = word1.lower(), word2.lower()
    for i in word1:
        for j in range(len(word2)):
            if word2[j] == i:
                if j == 0:
                    word2 = word2[j + 1 :]
                elif j == len(word2) - 1:
                    word2 = word2[:j]
                else:
                    word2 = word2[0:j] + word2[j + 1 :]
                break
    return True if len(word2) == 1 else False


if __name__ == "__main__":
    print(f"Gagnant = P{pyramid_game()}")
