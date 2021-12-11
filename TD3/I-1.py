import sys

# multiplie deux matrices et retourne la matrice résultante
def product(m1, m2):
	# création en compréhension de la matrice résultat
	r = [[ 0 for x in range(len(m1))] for y in range(len(m2[0]))]
	# multiplication des deux matrices
	for i in range(len(m1)):
		for j in range(len(m2[0])):
			for k in range(len(m2)):
				# 2 opérations ici une multiplication et une addition
				r[i][j] += m1[i][k]*m2[k][j]
	return r

# affiche une matrice "proprement"
def printm(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			# sys.stdout pour afficher sans retour à la ligne
			sys.stdout.write(str(matrix[i][j])+'\t')
		sys.stdout.write('\n')

m1 = [[1, 2, 0], [4, 3, -1]]
m2 = [[5, 1], [2, 3], [3, 4]]
printm(m1)
print()
printm(m2)
print()
printm(product(m1, m2))