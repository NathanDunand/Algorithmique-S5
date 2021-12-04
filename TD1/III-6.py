# vérifier la date
def verify_date(day, month, year):
	# vérification générique des jours, mois et année
	if((day < 1 or day > 31) or type(day) is not int):
		raise ValueError("1<= day <=31")
	if((month < 1 or month > 12) or type(month) is not int):
		raise ValueError("1<= month <=12")
	if((year < 1900 or year > 2100) or type(year) is not int):
		raise ValueError("1900<= year <=2100")

	# vérification que le nombre de jour est bien le bon
	if day > get_number_day_by_month(month, year):
		raise ValueError("this month does not have this day")

# booléen si l'année est bissextile
def is_bissextile(year):
	return year%4 and year%100!=0 or year%400==0 and year != 2000

# retourne le nombre de jours d'un mois et d'une année
def get_number_day_by_month(month, year):
	if month == 2:
		# 28 ou 29 selon si l'année est bissextile ou non
		return 28 if(is_bissextile(year)) else 29
	else:
		# 30 ou 31 selon le mois
		return 30 if(month == 4 or month == 6 or month == 9 or month == 11) else 31


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

# retourne True si date1 == date2 False sinon
def is_equal(date1, date2):
	return ((date1['day'] == date2['day']) and (date1['month'] == date2['month']) and (date1['year'] == date2['year']))

# date1 >= date2
def minus(date1, date2):
	days = 0
	# on remonte les années jusqu'à l'année de date1
	current_year = date2['year']
	while current_year != date1['year']:
		days_year = 365 if (is_bissextile(current_year)) else 366
		days += days_year
		current_year += 1

	# on remonte les mois date1['month']->date2['month']
	sous = 0
	if date1['month'] < date2['month']:
		# on calcule le nombre de jours entre ces deux dates et on le soustrait au nombre de jour dans l'année
		current_month = date1['month']
		while current_month != date2['month']:
			sous += get_number_day_by_month(current_month, current_year)
			current_month += 1
		# on soustrait car ce sont des jours qu'on a compté en trop puisque mois2>mois1 et que date1>date2
		days -= sous
	else:
		# on est sur la même année, maintenant on remonte les mois de date2['month']->date1['month']
		current_month = date2['month']
		# on remonte les mois jusqu'au mois de date1
		while current_month != date1['month']:
			days += get_number_day_by_month(current_month, current_year)
			current_month += 1

	return days+(date1['day']-date2['day'])

try:
	# ZONE DE TEST POUR LE CALCULATEUR DE JOURS
	if(minus({'day': 14, 'month': 8, 'year': 2021}, {'day': 10, 'month': 7, 'year': 2001}) != 7340):
		raise ValueError("ERROR1")
	if(minus({'day': 14, 'month': 10, 'year': 2021}, {'day': 10, 'month': 12, 'year': 2001} )!= 7248):
		raise ValueError("ERROR2")
	if(minus({'day': 30, 'month': 10, 'year': 2021}, {'day': 27, 'month': 2, 'year': 2001} )!= 7550):
		raise ValueError("ERROR3")
	if(minus({'day': 30, 'month': 10, 'year': 2021}, {'day': 27, 'month': 2, 'year': 1998} )!= 8646):
		raise ValueError("ERROR4")
	# -----------------

	print('What is your birthday ?')
	date1 = ask_date()
	verify_date(date1['day'], date1['month'], date1['year'])
	print(f'{date1["day"]}/{date1["month"]}/{date1["year"]}')

	# on a obtient la date de demain
	date1_plus = day_plus_one(date1)
	print("Date de demain :")
	print(f'{date1_plus["day"]}/{date1_plus["month"]}/{date1_plus["year"]}')

	print('What is your second date ?')
	date2 = ask_date()
	verify_date(date2['day'], date2['month'], date2['year'])
	print(f'{date2["day"]}/{date2["month"]}/{date2["year"]}')

	# on a obtient la date de demain
	date2_plus = day_plus_one(date2)
	print("Date de demain :")
	print(f'{date2_plus["day"]}/{date2_plus["month"]}/{date2_plus["year"]}')

	delta = minus(date1, date2)
	print(f'Nombre de jour(s) entre les deux dates : {delta} jour(s).')

except ValueError as e: # interception de l'erreur
	print("Error : "+str(e))