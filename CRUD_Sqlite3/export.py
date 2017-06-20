import csv, sqlite3

def export():
    filename = input('Input the file name and destination (.csv): ')
    conn = sqlite3.connect('person.db')
    c = conn.cursor()
    data = c.execute('SELECT * FROM person')

    with open(filename, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow([i[0] for i in c.description])
        w.writerows(data)

    conn.close()
    print('File created with success.')
