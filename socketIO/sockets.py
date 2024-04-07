from app import socketio
from flask import request, session
from crosswords.modal import puzzle_data, blocked_cells, getgrid
from flask_login import current_user



@socketio.on('revealed')
def handle_time(data):


    # push data to db
    print("\n")
    print("user:" , current_user.email)
    print(data)
    print("crosswordId",  session["crossword_id"] )
    print("\n")


@socketio.on('connect')
def handle_connect():
    crossword_id = session['crossword_id']
    clue_data=puzzle_data(crossword_id)
    blocked_cell_list , inputId_clueId = blocked_cells(clue_data)
    grid , order = getgrid(clue_data)
    client_sid = request.sid

    socketio.emit( "gameData", {
        'order':order,
        "inputId_clueId": inputId_clueId,
        'grid': grid,
        } ,room = client_sid)