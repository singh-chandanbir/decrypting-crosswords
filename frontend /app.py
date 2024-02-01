
from flask import Flask, render_template as rt, request
from api.db_crud import puzzle_data,blocked_cells
from api.pageIncreDecre import get_all_objects

app=Flask(__name__)




### all the routes
# Indexpage 
@app.route('/')
def homepage():
    return rt('index.html')
# indexpage

# veiwcrossword
@app.route('/veiw_crosswords/<int:page_number>' )
def veiw_crossword(page_number):
    all_objects = get_all_objects()  # Replace with your list of 100 objects
    # print(all_objects)
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

    return rt('crossword.html',  blocked_cell_list= blocked_cell_list ,clue_data=clue_data)
# the play crossword page 

# login
@app.route('/login')
def login():
    return rt('login.html')

# signup
@app.route('/signup')
def signin():
    return rt('signup.html')
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





# all the errors goes here 
@app.errorhandler(404)
def badlink(e):
    return rt('pagenotfound.html') , 404








app.run( debug=True ,port=8080)