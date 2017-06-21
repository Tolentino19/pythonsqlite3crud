import login, User, CRUD, Person, export, sqlite3, csv, logging
from datetime import datetime

logging.basicConfig(filename='errors.log',level=logging.DEBUG)

def main():
    print('Welcome to PersonDB!\n')
    log = True
    logged = False
    while log:
        prompt = input('Type LOGIN to log in or CREATE to create a new user: ').lower()
        if prompt == 'login':
            try:
                logged = login.login()
                log = False
            except Exception as e:
                logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+
                                ' - ' +
                                str(e))
                print('An ERROR has ocurred, please contact the admin.')
        elif prompt == 'create':
            try:
                login.create()
            except Exception as e:
                logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+
                                ' - ' +
                                str(e))
                print('An ERROR has ocurred, please contact the admin.')
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
                    logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+
                                ' - ' +
                                str(e))
                    print('An ERROR has ocurred, please contact the admin.')

            elif command == 'read':
                try:
                    CRUD.read()
                    print('\n')
                except Exception as e:
                    logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+
                                ' - ' +
                                str(e))
                    print('An ERROR has ocurred, please contact the admin.')

            elif command == 'update':
                try:
                    CRUD.update()
                    print('\n')
                except Exception as e:
                    logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+
                                ' - ' +
                                str(e))
                    print('An ERROR has ocurred, please contact the admin.')

            elif command == 'delete':
                try:
                    CRUD.delete()
                    print('\n')
                except Exception as e:
                    logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+
                                ' - ' +
                                str(e))
                    print('An ERROR has ocurred, please contact the admin.')

            elif command == 'export':
                try:
                    export.export()
                    print('\n')
                except Exception as e:
                    logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+
                                ' - ' +
                                str(e))
                    print('An ERROR has ocurred, please contact the admin.')
                
            elif command == 'exit':
                run = False

            else:
                print('Wrong input.')
                prompt = input('Do you want to try again? y/n: ')
                if prompt == 'n':
                    creating = False


if __name__ == '__main__':
              main()
