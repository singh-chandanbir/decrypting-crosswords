from flask import Flask, render_template as rt, request ,flash ,redirect
from api.db_crud import puzzle_data,blocked_cells , alreadyExit, addUser,userData, getgrid
from formClasses import signupForm, loginForm
from api.pageIncreDecre import get_all_objects
from flask_login import UserMixin, login_user,LoginManager ,login_required, logout_user ,current_user 
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)

app.config['SECRET_KEY'] = "alpha-beta-gamma-gang"


# Flask_Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(email):
    data= userData(email)
    user_object = User( username=data['userNmae'],email=data['email'], pass_hash=data['pass_hash'] )
    return user_object

class User(UserMixin):
    def __init__(self, username, email,pass_hash):
        # self.id = user_id
        self.username = username
        self.email= email
        self.pass_hash =pass_hash
        # self.is_active = is_active

    def get_id(self):
        return self.email

### all the routes
# Indexpage 
@app.route('/')
def homepage():
    return rt('index.html')
# indexpage

# veiwcrossword
@app.route('/veiw_crosswords/<int:page_number>' )
@login_required

def veiw_crossword(page_number):
    all_objects = get_all_objects() 
    start_index = (page_number - 1) * 9
    end_index = start_index + 9
    objects_to_display = all_objects[start_index:end_index]

    total_objects = len(all_objects)
    objects_per_page = 9
    total_pages, remainder = divmod(total_objects, objects_per_page)
    if remainder > 0:
        total_pages += 1
        
    return rt('veiw-crossword.html', objects=objects_to_display, page_number=page_number , total_pages =total_pages )
# veiwcrossword

# test header 
@app.route('/header')
def header():
    return rt('header-footer.html')
# test header 

# the play crossword page 
@app.route('/crossword', methods = ["POST", "GET"])
def crossword():
    if (request.method == "POST"):
        crosswordid = int(request.form.get("crossword-id"))
        clue_data=puzzle_data(crosswordid)
        blocked_cell_list = blocked_cells(clue_data)
        grid , order = getgrid(clue_data)


    return rt('crossword.html',  blocked_cell_list= blocked_cell_list ,clue_data=clue_data , grid = grid , order = order)
# the play crossword page 

# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form=loginForm()
    print(form.errors)
    if form.validate_on_submit():
        if (alreadyExit(form.email.data)):
            data = userData(form.email.data)
            if (check_password_hash(data['pass_hash'],form.password.data)):
                user_object = User( username=data['userNmae'],email=data['email'], pass_hash=data['pass_hash'] )
                login_user(user_object)
                flash("Login Succesfull!!")
                return redirect('/')
            else:
                flash('Incorrect login credentials')
        else:
            flash('user doest exist try again')
    print(form.errors)
    

    return rt('login.html' , form = form )





# signup
@app.route('/signup', methods=['GET', 'POST'])
def signin():

    form = signupForm()
    if form.validate_on_submit():
        print('form validate')

        if (alreadyExit(form.email.data)):
            flash("This email is already in use")
            return rt('signup.html', form=form)
        else:
            print("This name is already in use")
            hash_pass =  generate_password_hash(form.password.data, method='scrypt')
            addUser( form.userName.data, form.email.data , hash_pass )
            flash('Sign in Successful')
            return redirect('/login')

    return rt('signup.html' , form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	flash("You Have Been Logged Out!")
	return redirect(('/login'))

# synopsis
@app.route('/synopsis')
def synopsis():
    return rt('synopsis.html')

@app.route('/contact-us')
def contact_us():
    return rt('contact-us.html')

@app.route('/about-us')
def about_us():
    return rt('about-us.html')

@app.route('/thesecrate')
def hiddenpage():
    return rt('crossword-new.html')

@app.route('/dashbord')
@login_required
def dashbord():
    return rt('dashbord.html')


# @app.route('/test')
# def test():
#    x = get_all_users()


# all the errors goes here 
@app.errorhandler(404)
def badlink(e):
    return rt('pagenotfound.html') , 404











app.run(debug=True, host='0.0.0.0',port=8080)



