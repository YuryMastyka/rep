list_number = []
list_words = []
for i in range(5):
    list_number.append(input('произвольное число:'))

for i in range(5):
    list_words.append(input('произвольная строка:'))

print(list_number)
print(list_words)
list = list_number + list_words

print(list)
for i in list:
    print(id(i))

print(set(list))

print('--------------------------')

for i in set(list):
    print(id(i))

print('--------------------------')

y = 0
for i in list_number:
    y += int(i)
print(y)

print(list_words, sep=', ')