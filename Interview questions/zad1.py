#zad1

tablica = [1,3,3,5,6,8]
output = []


#Rozwiązanie szybkie do napisania
'''
output = [i + j for i, j in zip(tablica[::2], tablica [1:] [::2])]
print(output)
'''

#Rozwiązanie łatwe do wytłumaczenia
'''
def suma(tablica,output):
    stop = len(tablica)
    for n in range(0,stop -1,2):
        if n == stop:
            break
        else:
            output.append(tablica[n] + tablica[n+1])
    print(output)

suma(tablica,output)
'''