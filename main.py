# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def begin_phone_book_work():
    return
    
    
def read_phone_book(filename = ''):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            if line != '\n':
                record = dict(zip(fields, line.split('::')))
                if record['Телефон'][-1] == '\n':
                    record['Телефон'] = record['Телефон'][0:-1]
                phone_book.append(record)
    return phone_book

def show_phone_book(phone_book):
    for abonent in range(len(phone_book)):
        s = ''
        for i in phone_book[abonent].values():
            s = s + i + ' '
        print(s)
    return

def find_abonent(phone_book, key, value):
    for abonent in phone_book:
         if abonent[key] == value:
             s = ''
             for i in abonent.values():
                 s = s + i + ' '
             print(s)

def add_phone_record(phone_book):
    s = []
    fields = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    s.append(input('Введите Фамилию: ')) 
    s.append(input('Введите Имя: '))
    s.append(input('Введите Отчество: '))
    s.append(input('Введите Телефон: '))
    record = dict(zip(fields,s))
    phone_book.append(record)
    return(phone_book)

def save_phone_book(filename, phone_book):
    with open(filename,'w', encoding='utf-8') as phone_book_save:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + '::'
            phone_book_save.write(f'{s[:-2]}\n')
    return
    
    
    
# begin_phone_book_work()

# Обращение к файлу
string = read_phone_book('phon.txt') 

# Вывести данные файла
print(string)

# Вывожу справочник на экран
show_phone_book(string)

# Ищу в справочнике Человека
key = 'Фамилия'
value = 'Иванов'
find_abonent(string, key, value)

# Добавляю в справочник абонента
add_phone_record(string)
print(string)


# Сохранить телефонную книгу
save_phone_book('phon.txt', string)

