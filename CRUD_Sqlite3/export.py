import os, csv, sqlite3

folder = 'CSVFiles'

def export():
    filename = input('Input the file name: ') + '.csv'
    conn = sqlite3.connect('person.db')
    c = conn.cursor()
    data = c.execute('SELECT * FROM person')

    with open(os.path.join(folder, filename), 'w+', newline='') as f:
        w = csv.writer(f)
        w.writerow([i[0] for i in c.description])
        w.writerows(data)

    conn.close()
    print('File created with success.')
    print('Path: {}'.format(os.path.join(folder, filename)))
