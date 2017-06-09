import login, User, sqlite3


def auth():
    prompt = input('Type the username to authorize: ')
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('UPDATE user SET ' +
              'authorized = "yes" WHERE uname = "{}" '.format(prompt))
    conn.commit()
    conn.close()
    print('User authorized.')




if __name__ == '__main__':
    auth()
    
