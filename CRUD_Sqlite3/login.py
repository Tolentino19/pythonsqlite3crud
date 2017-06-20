import User, sqlite3, getpass

def create():
    creating = True
    while creating:
        uname = input('Type your username: ').lower()
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('SELECT * FROM user WHERE uname = "{}"'.format(uname))
        p = c.fetchone()
        conn.close()

        if p == None:
            email = input('Type your e-mail: ').lower()
            password = input('Type your password: ')
            check_pass = input('Type your password again: ')
            if password == check_pass:
                u = User.User(uname, email, password)
                print('Please confirm the data before commiting:')
                print('\n')
                print(u)
                print('\n')
                prompt = input('Confirm? y/n:').lower()

                if prompt == 'y':
                    conn = sqlite3.connect('user.db')
                    c = conn.cursor()

                    c.execute('INSERT INTO user VALUES ' +
                              '("{}", "{}", "{}", "no")'.format(u.uname,
                                                          u.email,
                                                          u.password))
                    conn.commit()
                    conn.close()

                    print('User created with success.')
                    creating = False
            else:
                print('Passwords does not match.')

        else:
            print('User already exists.')
            prompt = input('Do you want to try again? y/n: ')
            if prompt == 'n':
                creating = False


def login():
    loging = True
    while loging:
        uname = input('Username: ').lower()
        password = getpass.getpass()
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('SELECT * FROM user WHERE uname = "{}" AND password = "{}"'.format(uname,
                                                                                     password))
        u = c.fetchone()
        conn.close()
        if u != None:
            if u[3] == 'yes':
                print('Logged in with successs.')
                return True
            else:
                print('User not authorized.')
                prompt = input('Do you want to try again? y/n: ')
                if prompt == 'n':
                    loging = False
        else:
            print('Username or password wrong, or already exists.')
            prompt = input('Do you want to try again? y/n: ')
            if prompt == 'n':
                loging = False
            
            
