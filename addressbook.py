import sqlite3

base = sqlite3.connect('addressbook.db')
cur = base.cursor()

base.execute(
    'CREATE TABLE IF NOT EXISTS {}'
    '(id PRIMARY KEY, name text, lastname text, surname text, mail text, phone text, address text)'.format(
        'addbook'))
base.commit()


def addContact():
    id = input('\nВведiть id: \n')

    name = input('\nВведiть iмя: \n')
    lastName = input('\nВведiть призвище: \n')
    subName = input('\nВведiть по батькові: \n')
    email = input('\nВведiть пошту: \n')
    phoneNum = input('\nВведiть номер телефону: \n')
    address = input('\nВведiть адрес: \n')

    cur.execute('INSERT INTO addbook VALUES(?, ?, ?, ?, ?, ?, ?)',
                (id, name, lastName, subName, email, phoneNum, address))
    base.commit()

    print('\nСтворення контакту успішно виконена!\n')


def watchContacts():
    print(cur.execute('SELECT * FROM addbook').fetchall())


def watchContact():
    id = input('Введіть id: \n')
    print(cur.execute('SELECT * FROM addbook WHERE id == ?', (id,)).fetchall())


def editContact():
    id = input('\nВведiть id контакту якого хочете замінити: \n')

    newName = input('\nВведiть нове iмя: \n')
    newLastName = input('\nВведiть нове призвище: \n')
    newSubName = input('\nВведiть по батькові: \n')
    newEmail = input('\nВведiть нову пошту: \n')
    newPhonNum = input('\nВведiть новий номер телефону: \n')
    newAddress = input('\nВведiть новий адрес: \n')

    cur.execute(
        'UPDATE addbook SET name == ?, lastname == ?, surname == ?, mail == ?, phone == ?, address == ?  WHERE id == ?',
        (newName, newLastName, newSubName, newEmail, newPhonNum, newAdres, id))
    base.commit()

    print('\nЗміна контакту успішно виконена!\n')


def deleteContact():
    id = input('\nВведiть id контакту якого хочете видалити: \n')

    cur.execute('DELETE FROM addbook WHERE id == ?', (id,))
    base.commit()

    print('\nВидалення контакту успішно виконано!\n')

def printNoValidVariant():
    print('\nНе валідний варіант\n')


while True:
    v = int(input('Яку операцюю бажаєте виконати? \n '
                  '1. Додати контакт; \n '
                  '2. Подивитися контат/контакти; \n '
                  '3. Оновити контакт; \n '
                  '4. Видалити контакт;\n '
                  '5. Вийти з програми.\n\n'))

    if v == 1:
        addContact()

    elif v == 2:
        q = int(input('Ви бажаєте глянути всі контакти чи тільки один рядок? \n 1. Всі контакти; \n 2. Один контакт. \n'))
        if q == 1:
            watchContacts()
        elif q == 2:
            watchContact()
        else:
            printNoValidVariant()

    elif v == 3:
        editContact()

    elif v == 4:
        deleteContact()

    elif v == 5:
        break

    else:
        printNoValidVariant()
