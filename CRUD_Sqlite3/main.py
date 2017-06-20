import login, User, CRUD, Person, export, sqlite3, csv

def main():
    print('Welcome to PersonDB!\n')
    log = True
    logged = False
    while log:
        prompt = input("Type LOGIN to log in or CREATE to create a new user: ").lower()
        if prompt == 'login':
            logged = login.login()
            log = False
        elif prompt == 'create':
            login.create()
        else:
            print('Wrong input.')

    if logged:    
        run = True
        while run:
            print('Type CREATE to create a new entry\n'+
                  'Type READ to search the database\n'+
                  'Type UPDATE to update a entry\n'+
                  'Type DELETE to remove a entry\n'+
                  'Type EXPORT to export the db to a csv file\n'+
                  'Type EXIT to exit')

            command = input("Command: ").lower()
            print('\n')

            if command == 'create':
                CRUD.create()
                print('\n')

            elif command == 'read':
                CRUD.read()
                print('\n')

            elif command == 'update':
                CRUD.update()
                print('\n')

            elif command == 'delete':
                CRUD.delete()
                print('\n')

            elif command == 'export':
                export.export()
                print('\n')
                
            elif command == 'exit':
                run = False

            else:
                print('Wrong input.')
                prompt = input('Do you want to try again? y/n: ')
                if prompt == 'n':
                    creating = False


if __name__ == '__main__':
              main()
