import login, User, CRUD, Person, export, sqlite3, csv, logging
from datetime import datetime

logging.basicConfig(filename='errors.log',level=logging.DEBUG)

def error_report(e):
    logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+
                    ' - ' +
                    str(e))
    print('An ERROR has ocurred, please contact the admin.')

def main():
    print('Welcome to PersonDB!\n')
    log = True
    logged = False
    while log:
        prompt = input('Type LOGIN to log in, CREATE to create a new user or EXIT to quit the program: ').lower()
        if prompt == 'login':
            try:
                logged = login.login()
                if logged:
                    log = False
            except Exception as e:
                error_report(e)
                
        elif prompt == 'create':
            try:
                login.create()
            except Exception as e:
                error_report(e)

        elif prompt == 'exit':
            log = False
            
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
                try:
                    CRUD.create()
                    print('\n')
                except Exception as e:
                    error_report(e)

            elif command == 'read':
                try:
                    CRUD.read()
                    print('\n')
                except Exception as e:
                    error_report(e)

            elif command == 'update':
                try:
                    CRUD.update()
                    print('\n')
                except Exception as e:
                    error_report(e)

            elif command == 'delete':
                try:
                    CRUD.delete()
                    print('\n')
                except Exception as e:
                    error_report(e)

            elif command == 'export':
                try:
                    export.export('a', 'exported-data.csv', '')
                    print('\n')
                except Exception as e:
                    error_report(e)
                
            elif command == 'exit':
                run = False

            else:
                print('Wrong input.')
                prompt = input('Do you want to try again? y/n: ')
                if prompt == 'n':
                    creating = False


if __name__ == '__main__':
              main()
