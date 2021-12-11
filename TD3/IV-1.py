# Tri par sélection

# tableau de caractère quelconque non trié
tab = ['e', 'f', '0', 'q', '?', 'g', 'k', 'o', 'a', 'z', '|', '1', '5', '8', '&']

def selection_sort(tab):
	for i in range(len(tab)):
		# rechercher l'index du plus petit élément
		index_mini = i
		mini = tab[i]
		for j in range(i, len(tab)):
			# on cherche le plus petit élément dans ce qui reste du tableau
			if mini > tab[j]:
				index_mini = j
				mini = tab[j]

		# échange entre l'élément courant et le min
		a = tab[index_mini]
		tab[index_mini] = tab[i]
		tab[i] = a
	return tab

print('raw data')
print(tab)
print('sorted data with selection sort algorithm')
print(selection_sort(tab))