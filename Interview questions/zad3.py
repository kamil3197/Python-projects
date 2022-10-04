# zad3
dane = "aabcded"
lista = []

#Rozwiązanie szybkie do napisania
'''
lista = set(dane)
zmienna = list(lista)
wynik = sorted(zmienna)
print(''.join(wynik))
'''

#Rozwiązanie łatwe do wyjaśnienia
'''
def stringfix(dane, lista):
    for element in dane:
        if element in lista:
            continue
        lista.append(element)
    wynik = "".join(lista)
    print(wynik)

stringfix(dane,lista)
'''
