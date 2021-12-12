# Tri par fusion

# tableau de caractère quelconque non trié
tab = ['e', 'f', '0', 'q', '?', 'g', 'k', 'o', 'a', 'z', '|', '1', '5', '8', '&']

def merge_sort(tab):
	# condition d'arrêt du récursif
	if len(tab) > 1:
		# on coupe le tableau en 2
		m = len(tab) // 2
		l = tab[:m]
		r = tab[m:]
		# appel récursif, on tris sur les deux parties
		merge_sort(l)
		merge_sort(r)

		# left iterator right iterator et itérateur global
		li = ri = k = 0
 		# ici on a des tableaux composés d'un seul élément
		while li < len(l) and ri < len(r):
			# tri avec la condition, on bouge l'itérateur ensuite
			if l[li] < r[ri]:
				# tri
				tab[k] = l[li]
				li += 1
			else:
				# tri
				tab[k] = r[ri]
				ri += 1
			# on avance dans l'algo
			k += 1
		
		# valeurs restantes
		while li < len(l):
			tab[k] = l[li]
			li += 1
			k += 1
 
		while ri < len(r):
			tab[k]=r[ri]
			ri += 1
			k += 1
	return tab

print(merge_sort(tab))