import json
from flask import Flask, render_template as rt, request


from api.readdata import blocked_cells, read_clue_data
from api.pageIncreDecre import get_all_objects

app=Flask(__name__)

@app.route('/')
def homepage():
    return rt('index.html')
@app.route('/veiw_crosswords/<int:page_number>' )
def veiw_crossword(page_number):

    all_objects = get_all_objects()  # Replace with your list of 100 objects
    start_index = (page_number - 1) * 9
    end_index = start_index + 9
    objects_to_display = all_objects[start_index:end_index]


    total_objects = len(all_objects)
    objects_per_page = 9
    total_pages, remainder = divmod(total_objects, objects_per_page)
    if remainder > 0:
        total_pages += 1


   
    # current_list=[10746,10764,1]
    return rt('veiw-crossword.html', objects=objects_to_display,page_number=page_number , total_pages =total_pages )

@app.route('/header')
def header():
    return rt('header-footer.html')

@app.route('/crossword', methods = ["POST", "GET"])
def crossword():
    if (request.method == "POST"):
        crosswordid = request.form.get("crossword-id")
        blocked_cell_list = blocked_cells(crosswordid)
        clue_data=read_clue_data(crosswordid)

    return rt('crossword.html',  blocked_cell_list= blocked_cell_list ,clue_data=clue_data)


@app.route('/pagenotfound')
def badlink():
    return rt('pagenotfound.html')

app.run( debug=True ,port=8080)