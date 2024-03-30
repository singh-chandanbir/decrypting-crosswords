from app import app
from flask import render_template as rt, request
from flask_login import login_required
from api.db_crud import puzzle_data,blocked_cells,getgrid
from api.pageIncreDecre import get_all_objects
from app import socketio



     

##### .......................................... Crossword Routes  .............................................#####



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




@app.route('/crossword', methods = ["POST", "GET"])
def crossword():

    
    if (request.method == "POST"):
        crosswordid = int(request.form.get("crossword-id"))
        clue_data=puzzle_data(crosswordid)
        blocked_cell_list = blocked_cells(clue_data)
        grid , order = getgrid(clue_data)

        @socketio.on('connect')
        def handle_connect():
            client_sid = request.sid
            socketio.emit( "gameData", {
                'order':order,
                'grid':grid,
                "blocked_cell_list": blocked_cell_list
    
        } ,room = client_sid)
            


    return rt('crossword.html',  clue_data=clue_data  )
