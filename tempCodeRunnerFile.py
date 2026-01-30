my_list = ['Ahmed', 'Ali', 'Osman', 'Kalid', 'Omar', 'Amar', 'Awab']

for i, name in enumerate(my_list):
    cr.execute(f"INSERT INTO students(id, name) values({i}, '{name}')")
