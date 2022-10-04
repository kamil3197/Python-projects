# zad2
suma = input("podaj liczbę")
n = len(suma)
wynik = 0


#Rozwiązanie szybkie do napisania
'''
wynik = [True for number in suma if int(suma) % int(number) == 0]
if n == len(wynik):
    print('liczba jest samopodzielnia')
else:
    print('liczba nie jest samopodzielna')
'''

#Rozwiązanie szybkie do wytłumaczenia
'''
for number in suma:
    if int(suma) % int(number) == 0:
        wynik +=1
    else:
        wynik -=1

#jeśli wynik jest równy ilości liczb sprawdzanych = True
if wynik == len(suma):
    print('Jest samopodzielna')
else:
    print('Nie jest samopodzielna')
'''