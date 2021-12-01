# vérifier la date
def verify_date(day, month, year):
	# on teste si l'année est bissextile, si c'est le cas février a 29 jours, 28 sinon
	febr = 28 if (year%4 and year%100!=0 or year%400==0) else 29
	day = str(day).zfill(2)
	print(day)
	dic = {
	'january': 30,
	'february': febr,
	'march': 31,
	'april': 30,
	'may': 31,
	'june': 30,
	'july': 31,
	'august': 31,
	'september': 30,
	'october': 31,
	'november': 30,
	'december': 31
	}

print('What is your birthday ?')

# j'ai fait le choix de tester avec des try/except, on test les bornes et le type et on affiche un message d'erreur au besoin
try:
	day = int(input('Day\n'))
	if((day < 1 or day > 31) or type(day) is not int):
		raise ValueError("1<= day <=31")

	month = int(input('Month\n'))
	if((month < 1 or month > 12) or type(month) is not int):
		raise ValueError("1<= month <=12")

	year = int(input('Year\n'))
	if((year < 1900 or year > 2100) or type(year) is not int):
		raise ValueError("1<= month <=12")

	print(f'{day}/{month}/{year}')
	verify_date(day, month, year)
except ValueError as e: # interception de l'erreur
	print("Error : "+str(e))