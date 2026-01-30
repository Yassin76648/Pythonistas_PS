import sqlite3

massage = """
Choose an Option : 
1. s ==> Show All Skills
2. a ==> Add Skill
3. u ==> Update Progress
4. d ==> Delete Skill
5. q ==> Quit App
"""

def show_skills(cr):
    result = cr.execute("SELECT * from skills")
    for i, name, progress in result:
        print(f"Name: {name} ==> Progress : {progress} ")

def add_skill(cr, id):
    name = input("Skill Name: ")
    progress = input("Progress From 10: ")
    cr.execute(f"INSERT INTO skills values({id}, '{name}', {progress})")
    print("Skill Added Succesfull...")

def update_progress(cr):
    name = input("Skill Name: ")    
    progress = input("New Progress from 10: ")
    cr.execute(f"UPDATE skills SET skill_progress = {progress} WHERE skill_name = '{name}'")
    print("Skill Updated Succesfully")

def delete_skill(cr):
    name = input("Skill Name to Delete: ")
    cr.execute(f"DELETE FROM skills WHERE skill_name = '{name}'")
    print("Skill Deleted Succesfull")

choices = ['s', 'a', 'u', 'd', 'q']

count = 1
choice = input(f"{massage}Letter : " ).strip().lower()

    
if choice in choices:

    db = sqlite3.connect("skills.db")
    cr = db.cursor()
    cr.execute("CREATE TABLE if not exists skills(skill_id INTEGER, skill_name TEXT, skill_progress INTEGER)")

    while choice != 'q':

        if choice == 's':
            show_skills(cr)

        elif choice =='a':
            id = count
            add_skill(cr, id)
            count +=1
        elif choice == 'u':
            update_progress(cr)

        elif choice == 'd':
            delete_skill(cr)

        else :
            print("App Closed.")
            cr.close()
            break

        db.commit()
        print(massage)
        choice = input("Letter: ")

