import pandas
pliczek = pandas.read_csv("nato_phonetic_alphabet.csv")
dejta = pandas.DataFrame(pliczek)
dane = dict(dejta.values)
ask = input('provide a name').upper()
name = [elements for elements in ask]
for elements in name:
    print(dane[elements])