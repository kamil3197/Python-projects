import pandas
file = pandas.read_csv("nato_phonetic_alphabet.csv")
data = dict(file.values)
ask = input('provide a name').upper()
name = [elements for elements in ask]
for elements in name:
    print(data[elements])