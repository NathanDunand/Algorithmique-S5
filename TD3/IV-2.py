# Tri par insertion

# tableau de caractère quelconque non trié
tab = ['e', 'f', '0', 'q', '?', 'g', 'k', 'o', 'a', 'z', '|', '1', '5', '8', '&']

def insertion_sort(tab):
	# tous le tableau
	for i in range(len(tab)):
		# les éléments d'avant i sont déjà triés
		k = tab[i]
		j = i-1
		# on décalle de 1 position tq tab[j] < que l'élément courant (k)
		while j >= 0 and k < tab[j]:
			tab[j+1] = tab[j]
			j -= 1
		# on met la valeur
		tab[j+1] = k
	return tab

print(insertion_sort(tab))