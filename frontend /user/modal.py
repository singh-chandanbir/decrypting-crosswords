from db.db import db
from flask_login import UserMixin, login_user
from werkzeug.security import generate_password_hash, check_password_hash

user = db["users"]

class User(UserMixin):
    def __init__(self,userData):
        self.name = userData['name']
        self.email = userData['email']
        self.password_hash = userData['password_hash']
        self.averagetime = userData['averagetime']
        self.globalrank = userData['globalrank']
        self.crossword_solved = userData['crossword_solved']
        # self.is_authenticated = userData['is_authenticated']
        # self.is_active = userData['is_active']

        
    def get_id(self):
        return self.email


    def alreadyExists(email):
        data = user.find_one({ "email": email })
        if data:
            return True
        else:
            return False
      
    def userData(email):
        data = user.find_one({ "email": email})
        return data

    
    def signup(form):
        if (User.alreadyExists(form.email.data)):
            return "This email is already in use", False    
        else:
            hash_pass =  generate_password_hash(form.password.data, method='scrypt')
            new_user = dict( name = form.name.data, email = form.email.data, password_hash = hash_pass , averagetime = 0, globalrank = 10000, crossword_solved = 0)
            result = user.insert_one(new_user)
            print("User Added: "+str(result))
            login_user(User(new_user))
            return "Sign in Successful", True 

    def login(form):
        if (User.alreadyExists(form.email.data)):
                    userData = User.userData(form.email.data)
                    if (check_password_hash(userData['password_hash'],form.password.data)):
                        print(str(userData['email'])+": Logged in")
                        userObject = User(userData)
                        login_user(userObject)
                        responce = "Login Succesfull!!"
                        status = True
                    else:
                        responce = 'Incorrect login credentials'
                        status = False
        else:
            responce = 'User doest exist!! try again'
            status = False

        return responce , status
                