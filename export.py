import os, csv, sqlite3

folder = 'CSVFiles'

def export(dataex, filename, info):
    if dataex == 'a':
        path = os.path.join(folder, filename)
        conn = sqlite3.connect('person.db')
        c = conn.cursor()
        data = c.execute('SELECT * FROM person')
                
        with open(path, 'w+', newline='') as f:
            w = csv.writer(f)
            w.writerow([i[0] for i in c.description])
            w.writerows(data)
                    
        conn.close()

        print('File created with success.')

    elif dataex == 'd':
        path = os.path.join(folder, filename)
        with open(path, 'a', newline='') as f:
                    f.write('{};{};{};{};{}\n'.format(
                        info.name,
                        info.pid,
                        info.birthdate,
                        info.phone,
                        info.address))
