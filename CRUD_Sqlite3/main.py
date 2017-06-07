import CRUD, Person, sqlite3

def main():
    print('Welcome to PersonDB!\n')
    run = True
    while run:
        print('Type CREATE to create a new entry\n'+
              'Type READ to search the database\n'+
              'Type UPDATE to update a entry\n'+
              'Type DELETE to remove a entry\n'+
              'Type EXIT to exit')

        command = input("Command: ").lower()
        print('\n')

        if command == 'create' or command == 'c':
          CRUD.create()
          print('\n')

        elif command == 'read' or command == 'r':
          CRUD.read()
          print('\n')

        elif command == 'update' or command == 'u':
          CRUD.update()
          print('\n')

        elif command == 'delete' or command == 'd':
          CRUD.delete()
          print('\n')

        elif command == 'exit' or command == 'e':
          run = False

        else:
            print('ERROR: Try again')


if __name__ == '__main__':
              main()
