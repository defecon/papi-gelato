particulier='y'
zakelijk='y'
bakjestellen='.'
toppingeidelijk=0
aantalhorentjes=0
aantalbakjes=0
aantaleindelijk=0
def vraagbolljes():
	while True:
		aantal = int(input(f"Hoeveel {bolletjesOfliters} wilt u? "))
		if bolletjesOfliters=='bolletje':
			if aantal <= 3:
				return aantal
			elif aantal == 4 or aantal == 5 or aantal == 6 or aantal == 7 or aantal == 8:
				print(f'Dan krijgt u van mij een bakje met {aantal} {bolletjesOfliters}')
				return aantal
			elif aantal > 8:
				print("Sorry, zulke grote bakken hebben we niet")
			else:
				print("Sorry dat is geen optie die we aanbieden...")
		elif bolletjesOfliters=='liter':
			if aantal >= 1:
				return aantal
			else:
				print("Sorry dat is geen optie die we aanbieden...")
def smaakkiezen():
	Nbolletje = 1
	while Nbolletje <= aantal:
		smaak = input(f'Welke smaak wilt u voor {bolletjesOfliters} nummer {Nbolletje}? A) Aardbei, C) Chocolade, V) Vanille?').lower()
		if smaak=='a' or smaak=='c' or smaak=='v':
			Nbolletje+=1
		else:
			print('Sorry dat is geen optie die we aanbieden...')

def bakjeofhoorntje():
	while True:
		bakje = input(f'Wilt u deze {aantal} bolletje(s) in A) een hoorntje of B) een bakje?').lower()
		if bakje=='a':
			global aantalhorentjes
			bakje = 'Hoorntje'
			aantalhorentjes+=1
			return bakje
		elif bakje=='b':
			global aantalbakjes
			bakje = 'Bakje'
			aantalbakjes+=1
			return bakje
		else:
			print("Sorry dat is geen optie die we aanbieden...")

def topping():
	while True:
		toppingkeuze=input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?').lower()
		if toppingkeuze=='a':
			toppingkeuze=0
			return toppingkeuze
		elif toppingkeuze=='b':
			toppingkeuze=0.5
			return toppingkeuze
		elif toppingkeuze=='c':
			toppingkeuze=0.3
			return toppingkeuze
		elif toppingkeuze=='d':
			if bakje=='Hoorntje':
				toppingkeuze=0.6
				return toppingkeuze
			elif bakje=='Bakje':
				toppingkeuze=0.9
				return toppingkeuze
		else:
			print('Sorry dat is geen optie die we aanbieden...')

def again():
	while True:
		particulier = input(f'Hier is uw {bakje} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N) : ').lower()
		if particulier == 'y':
			return particulier
		elif particulier =='n':
			print('Bedankt en tot ziens!')
			return particulier
		else:
			print('Sorry dat is geen optie die we aanbieden...')
def bonnnetje():
	if particulier=='y'and zakelijk=='n':
		if aantalbakjes>=1:
			totalbakje=f'Bakje     {aantalbakjes} x €0,75 = €{round(aantalbakjes*0.75, 2)}'
		else:
			totalbakje=''
		if aantalhorentjes>=1:
			totalhoorntje=f'hoorntje  {aantalhorentjes} x €1,25 = €{round(aantalhorentjes*1.25, 2)}'
		else:
			totalhoorntje=''
		if toppingeidelijk>=0.1:
			totaltopping=f'topping    1 x €{toppingeidelijk} = €{toppingeidelijk}'
		else:
			totaltopping=''
		totalbolletjes=f'Bolletjes {aantaleindelijk} x €1,10 = €{round(aantaleindelijk*0.95, 2)}'
		totaalmoney=f'Totaal                €{round(aantalbakjes*0.75, 2)+round(aantaleindelijk*0.95, 2)+round(aantalhorentjes*1.25, 2)+round(toppingeidelijk, 2)}'
		print(f"""---------["Papi Gelato"]---------
	        {totalbolletjes}
	        {totalhoorntje}
	        {totalbakje}
	        {totaltopping}
	                              ------+
	        {totaalmoney}""")
	elif zakelijk=='y'and particulier=='n':
		totalbolletjes=f'Liter     {aantaleindelijk} x €9,80 = €{round(aantaleindelijk*9.80, 2)}'
		totaalmoney=f'Totaal              = €{round(aantaleindelijk*9.80, 2)}'
		totalbtw=f'BTW (9%)            = €{round(aantaleindelijk*9.80/100*6, 2)}'
		print(f"""---------["Papi Gelato"]---------
	        {totalbolletjes}
	                              ------+
	        {totaalmoney}
	        {totalbtw}""")
#--------------------------------------------------------------------------------#
print("Welkom bij Papi Gelato")
vraagzakelijk = int(input('Bent u 1) particulier of 2) zakelijk? : '))
while True:
	if vraagzakelijk==1:
		particulier='y'
		zakelijk='n'
		bolletjesOfliters='bolletje'
		break
	elif vraagzakelijk==2:
		particulier='n'
		zakelijk='y'
		bolletjesOfliters='liter'
		break	
	else:
		print('Sorry dat is geen optie die we aanbieden...')
if particulier=='y'and zakelijk=='n':
	while particulier=='y'and zakelijk=='n':
		while particulier=='y':
			aantal = vraagbolljes()
			smaakkiezen()
			bakje = bakjeofhoorntje()
			toppingkeuze=topping()
			particulier = again()
			toppingeidelijk+=toppingkeuze
			aantaleindelijk+=aantal
	bonnnetje()
else:
	aantal = vraagbolljes()
	smaakkiezen()
	aantaleindelijk+=aantal
	bonnnetje()
input("press enter to exit this menu")