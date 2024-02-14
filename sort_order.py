animals = ['dog', 'cat', 'alpaca', 'orangutan', 'hippo', 'iguana', 'puma', 'tyranasarus', 'horse']

sort_animals = sorted(sorted(animals), key=lambda x: len(x))
print(sort_animals)