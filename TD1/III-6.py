# vérifier la date
def verify_date(day, month, year):
	# vérification générique des jours, mois et année
	if((day < 1 or day > 31) or type(day) is not int):
		raise ValueError("1<= day <=31")
	if((month < 1 or month > 12) or type(month) is not int):
		raise ValueError("1<= month <=12")
	if((year < 1900 or year > 2100) or type(year) is not int):
		raise ValueError("1<= year <=12")

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

def day_plus_one(date):
	# on essaie en cascade
	try:
		# si verify_date() lève une exception sur l'incrémentation du jour, on tente d'incrémenter le mois
		verify_date(date['day']+1, date['month'], date['year'])
		date['day'] += 1
	except:
		try:
			# on a une erreur sur l'incrémentation du jour, on met le jour à 1 et on tente d'incrémenter le mois
			date['day'] = 1
			# si verify_date() lève une exception sur l'incrémentation du mois, on tente d'incrémenter l'année
			verify_date(date['day'], date['month']+1, date['year'])
			date['month'] += 1
		except:
			try:
				# on a une erreur sur l'incrémentation du mois, on met le mois à 1 et on tente d'incrémenter sur l'année
				date['month'] = 1
				# si verify_date() lève une exception sur l'incrémentation de l'année, on
				verify_date(date['day'], date['month'], date['year']+1)
				date['year'] += 1
			except:
				raise ValueError("out of domain")
	return date

# j'ai restructuré l'exercice dans quelque chose de plus modulable, j'avais des vérifications en double
try:
	# j'ai enlevé ma boucle, pas utile pour cette consigne, on fait deux fois la demande de date en dur
	print('What is your birthday ?')
	date1 = ask_date()
	verify_date(date1['day'], date1['month'], date1['year'])
	print(f'{date1["day"]}/{date1["month"]}/{date1["year"]}')

	# on a obtient la date de demain
	date1 = day_plus_one(date1)
	print("Date de demain :")
	print(f'{date1["day"]}/{date1["month"]}/{date1["year"]}')

	# ------------------

	print('What is your second date ?')
	date2 = ask_date()
	verify_date(date2['day'], date2['month'], date2['year'])
	print(f'{date2["day"]}/{date2["month"]}/{date2["year"]}')

	# on a obtient la date de demain
	date2 = day_plus_one(date2)
	print("Date de demain :")
	print(f'{date2["day"]}/{date2["month"]}/{date2["year"]}')

	# calcule du nombre de jours entre deux dates

except ValueError as e: # interception de l'erreur
	print("Error : "+str(e))