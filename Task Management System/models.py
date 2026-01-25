# User Model
import datetime
class User():

    is_active = None
    created_at = None
    def __init__(self, id, fname, lname, email, password_hash, role):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password_hash = password_hash
        self.role = role


def new_user():
    fname  = input("First Name : ")
    lname = input("Last Name : ")
    email = input("Email : ")
    password_hash = input("Password : ")
    role = input("Your Role (Admin, Manager, Member): ")
    created_at = datetime.datetime.now()
    is_active = True
    
    return User(fname, lname, email, password_hash, role, created_at, is_active)


class Project():
    def __init__(self, id, title, description, status, owner_id, created_at):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.owner_id = owner_id
        self.created_at = created_at

# Task Model
class Task():
    def __init__(self, id, title, description, project_id, periority, status, assigned_by_user_id, assigned_to_user_id, deadline, created_at, updated_at ):
        self.id = id
        self.title = title
        self.description = description
        self.project_id = project_id
        self.periority = periority
        self.status = status
        self.assigned_by_user_id = assigned_by_user_id
        self.assigned_to_user_id = assigned_to_user_id
        self.deadline = deadline
        self.created_at = created_at
        self.updated_at = updated_at


# import User
Tasks = []
projects =[]
managers =[]
admins = []
member = []

def register():
    user = new_user()


register()