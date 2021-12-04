# vérifier la date
def verify_date(day, month, year):
	# on teste si l'année est bissextile, si c'est le cas février a 29 jours, 28 sinon
	febr = 28 if (year%4 and year%100!=0 or year%400==0) else 29
	
	dic = {
	1: 30,
	2: febr,
	3: 31,
	4: 30,
	5: 31,
	6: 30,
	7: 31,
	8: 31,
	9: 30,
	10: 31,
	11: 30,
	12: 31
	}

	# vérification des jours des mois et de l'année bissextile
	for key, value in dic.items():
		if month == key: # le mois qu'à rentré l'utilisateur
			if day > value:
				raise ValueError("this month does not have this day")

# on demande une date, on retourne un dictionnaire contenant la date demandée
def ask_date():
	day = int(input('Day\n'))
	month = int(input('Month\n'))
	year = int(input('Year\n'))
	return {'day': day, 'month': month, 'year': year}

# j'ai restructuré l'exercice dans quelque chose de plus modulable, j'avais des vérifications en double
try:
	for i in range(2): # j'ai fais le choix d'une boucle : moins de code
		print('What is your birthday ?')
		date = ask_date()
		verify_date(date['day'], date['month'], date['year'])
		print(f'{date["day"]}/{date["month"]}/{date["year"]}')
except ValueError as e: # interception de l'erreur
	print("Error : "+str(e))