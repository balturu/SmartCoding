names = ["Peter", "Mary", "Jane", "Mark"]
locations = ["Stockholm", "Gothenburg", "Helsingborg", "Umea"]
phones = [46701111111, 46702222222, 46703333333, 46704444444]

#for n, l, p in zip(names, locations, phones):
    #print('{0}, {1}, {2}'.format(n, l, p))

phoneBook = {}
count = 0
for name in names:
    phoneBook[name] = {'location': locations[count], 'phone': phones[count]}
    count = count + 1
print(phoneBook.items())
