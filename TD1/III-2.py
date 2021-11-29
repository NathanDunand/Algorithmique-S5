print('What is your birthday ?')

# j'ai fait le choix de tester avec des try/except, on test les bornes et le type et on affiche un message d'erreur au besoin
try:
	day = int(input('Day\n'))
	if((day < 1 or day > 31) or type(day) is not int): # test
		raise ValueError("1<= day <=31")

	month = int(input('Month\n'))
	if((month < 1 or month > 12) or type(month) is not int):
		raise ValueError("1<= month <=12")

	year = int(input('Year\n'))
	if((year < 1900 or year > 2100) or type(year) is not int):
		raise ValueError("1<= month <=12")

	print(f'{day}/{month}/{year}')
except ValueError as e: # interception de l'erreur
	print("Error : "+str(e))