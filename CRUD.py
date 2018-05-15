import Person, export
import sqlite3
import pyperclip as clip

def create():
    creating = True
    while creating:
        name = input('Type the name: ').lower()
        pid = input('Type the PID: ')
        birthdate = input('Type the birthdate: ')
        phone = input('Type the phone: ')
        address = input('Type the address: ').lower()

        conn = sqlite3.connect('person.db')
        c = conn.cursor()
        c.execute('SELECT * FROM person WHERE name = "{}" OR pid = "{}"'.format(name, pid))
        p = c.fetchone()
        conn.close()

        if not p:
            p = Person.Person(name, pid, birthdate, phone, address)
            print('Please confirm the data before commiting:')
            print('\n')
            print(p)
            print('\n')
            prompt = input('Confirm? y/n:').lower()

            if prompt == 'y':
                conn = sqlite3.connect('person.db')
                c = conn.cursor()

                c.execute('INSERT INTO person VALUES ' +
                          '("{}", "{}", "{}", "{}", "{}")'.format(p.name,
                                                                  p.pid,
                                                                  p.birthdate,
                                                                  p.phone,
                                                                  p.address))
                conn.commit()
                conn.close()

                print('Entry created with success.')
                creating = False

        else:
            print('Entry already exists.')
            prompt = input('Do you want to try again? y/n: ')
            if prompt == 'n':
                creating = False


def read():
    reading = True
    while reading:
        query = input('Search for NAME or PID: ').lower()
        if query == 'name' or query == 'pid':
            uinput = input('Type the {}: '.format(query)).lower()
            conn = sqlite3.connect('person.db')
            c = conn.cursor()
            c.execute('SELECT * FROM person WHERE {} = "{}"'.format(query, uinput))
            p = c.fetchone()

            if p:
                print('\n')
                person = Person.Person(p[0], p[1], p[2], p[3], p[4])
                print(person)

                #clip.copy(str(person))
                
                conn.close()
                reading = False

            else:
                print('Entry not found in database')
                prompt = input('Do you want to try again? y/n: ')
                if prompt == 'n':
                    reading = False

        
        else:
            print('You should type NAME or PID.')
            prompt = input('Do you want to try again? y/n: ')
            if prompt == 'n':
                reading = False


def update():
    up = True
    while up:
        query = input('Search for NAME or PID: ').lower()
        if query == 'name' or query == 'pid':
            uinput = input('Type the {}: '.format(query)).lower()
            conn = sqlite3.connect('person.db')
            c = conn.cursor()
            c.execute('SELECT * FROM person WHERE {} = "{}"'.format(query, uinput))
            check = c.fetchone()
            conn.close()

            if check:
                info = input('What do you want to update'+
                             '(ALL, NAME, PID, BIRTHDATE, PHONE or ADDRESS): ').lower()

                if info == 'all' or info == 'a':
                    updating = True
                    while updating:
                        name_ = input('Type the name: ').lower()
                        pid = input('Type the PID: ')
                        birthdate = input('Type the birthdate: ')
                        phone = input('Type the phone: ')
                        address = input('Type the address: ').lower()

                        p = Person.Person(name_, pid, birthdate, phone, address)

                        print('Please confirm the data before commiting:')
                        print(p)
                        prompt = input('Confirm? y/n:').lower()

                        if prompt == 'y':
                            conn = sqlite3.connect('person.db')
                            c = conn.cursor()

                            c.execute('UPDATE person SET '+
                                      'name = "{}", pid = "{}", '+
                                      'birthdate = "{}", phone = "{}", '+
                                      'address = "{}" WHERE {} = "{}"'.format(p.name,
                                                                                p.pid,
                                                                                p.birthdate,
                                                                                p.phone,
                                                                                p.address,
                                                                                query,
                                                                                uinput))
                            conn.commit()
                            conn.close()

                            print('Entry updated with success.')
                            updating = False
                            up = False

                elif info == 'name' or info == 'pid' or info == 'birthdate' or info == 'phone' or info == 'address':
                    updating = True
                    while updating:
                        change = input('Type the {}: '.format(info)).lower()
                        print('Please confirm the data before commiting:')
                        print('{}: '.format(info.title()), change)
                        prompt = input('Confirm? y/n:').lower()

                        if prompt == 'y':
                            conn = sqlite3.connect('person.db')
                            c = conn.cursor()

                            c.execute('UPDATE person SET '+
                                      '{} = "{}" WHERE {} = "{}"'.format(info, change, query, uinput))
                            conn.commit()
                            conn.close()

                            print('Entry updated with success.')
                            prompt = input('Update something else? y/n: ')
                            if prompt == 'n':
                                updating = False
                                up = False
                            else:
                                updating = False

                
                            
                else:
                    print('You should type: ALL, NAME, PID, BIRTHDATE, PHONE or ADDRESS.')
                    prompt = input('Do you want to try again? y/n: ')
                    if prompt == 'n':
                        up = False

            else:
                print('Entry not found in database')
                prompt = input('Do you want to try again? y/n: ')
                if prompt == 'n':
                    up = False

        else:
            print('You should type NAME or PID.')
            prompt = input('Do you want to try again? y/n: ')
            if prompt == 'n':
                up = False
                    

def delete():
    deleting = True
    while deleting:
        query = input('Search for NAME or PID: ').lower()
        if query == 'name' or query == 'pid':
            uinput = input('Type the {}: '.format(query)).lower()
            conn = sqlite3.connect('person.db')
            c = conn.cursor()
            c.execute('SELECT * FROM person WHERE {} = "{}"'.format(query,
                                                                    uinput))
            p = c.fetchone()
            conn.close()

            if p:
                person = Person.Person(p[0], p[1], p[2], p[3], p[4])
                print('Please confirm if you want to delete this entry:')
                print('\n')
                print(person)
                print('\n')
                prompt = input('Confirm? y/n: ').lower()
                
                if prompt == 'y':
                    export.export('d', 'deleted-data.csv', person)
                        
                    conn = sqlite3.connect('person.db')
                    c = conn.cursor()
                    c.execute('DELETE FROM person WHERE {} = "{}"'.format(query,
                                                                          uinput))
                    conn.commit()
                    conn.close()
                    print('Entry deleted with success.')
                    deleting = False

            else:
                print('Entry not found in database.')
                prompt = input('Do you want to try again? y/n: ')
                if prompt != 'y':
                    deleting = False
