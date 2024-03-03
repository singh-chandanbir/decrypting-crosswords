from flask import Flask, render_template as rt, request ,flash ,redirect
from api.db_crud import puzzle_data,blocked_cells,getgrid
from user.userforms  import signupForm, loginForm
from api.pageIncreDecre import get_all_objects
from flask_login import LoginManager,login_required, logout_user
from os import getenv


app=Flask(__name__)

app.config['SECRET_KEY'] = getenv("SECRET_KEY")




from user.modal import User

# Flask_Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(email):
    data= User.userData(email)
    return User(data)



### all the routes
# Indexpage 
@app.route('/')
def homepage():
    return rt('index.html')


# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form=loginForm()
    # print(form.errors)
    if form.validate_on_submit():
        res , status =User.login(form)
        if status:
            flash(res)
            return redirect('/dashboard')
        else:
            flash(res)
            return redirect('/login')
    return rt('login.html' , form = form )


# Signup
@app.route('/signup', methods=['GET', 'POST'])
def signin():
    form = signupForm()
    if form.validate_on_submit():
        response, status = User.signup(form)
        flash(response)
        if (status):
            return redirect('/dashbord')
        else:
            return redirect('/signup')
    return rt('signup.html' , form=form)

# Logout
@app.route('/logout', methods=['GET'])
@login_required
def logout():
	logout_user()
	flash("You Have Been Logged Out!")
	return redirect(('/login'))


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






# all static pages
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

@app.route('/dashboard')
@login_required
def dashboard():
    return rt('dashbord.html')




# all the errors goes here 
@app.errorhandler(404)
def badlink(e):
    return rt('pagenotfound.html') , 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' ,port=8080)



