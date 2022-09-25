import csv
from random import randrange
file = []
tags = []
with open('books.csv', 'r', newline='', encoding='windows-1251') as csvfile:
    rows = csv.reader(csvfile, delimiter=';', quotechar='"')
    long_names = 0
    count = 0
    book_tags = []
    for row in list(rows)[1:]:
        file.append(row)
        count = count +1
        book_tags = row[len(row)-1].split('# ')
        tags += book_tags
        if len(row[1])>30:
            long_names=long_names+1
    print('длинных имен: ' +    str(long_names))

print('tags: ')
print(set(tags))
print('записей: ' + str(len(file)))

start = randrange(len(file)-20)
f = open('text.txt', 'w')
j = 1
for i in range(start, start+20):
    f.write(str(j) + '. ' + file[i][3] + '. ' + file[i][1] + ' - ' + file[i][6] + '\n')
    j = j+1

def get_issues(el):
    return el[8]

by_popular = file.copy()
by_popular.sort(reverse=True, key = get_issues)
for i in range(0, 19):
    print(by_popular[i])

search = input('введите поисковый запрос')

def checkBook(book):
    return search.lower() in book[3].lower() and float(book[7].replace(',', '.'))>200

print(list(filter(checkBook, file)))

