from app import socketio
from flask import request, session
from crosswords.modal import puzzle_data, blocked_cells, getgrid
from flask_login import current_user
from db.db import solved_puzzles


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
    


@socketio.on('endgame')
def handle_game_end(data):
    # push data to db
    print("\n")
    print("user:" , current_user.email)
    print(data)
    print("crosswordId",  session["crossword_id"] )
    print("\n")

    timeTaken = data["timeTaken"]
    timeTaken = timeTaken / 1000
    accuarcy = data["accuracy"]
    crossword_id = session["crossword_id"]
    words = data["words"]

    email = current_user.email
    exist = solved_puzzles.find_one({ "email": email })

    if exist:
        print("updating data")
        if crossword_id in exist["crossword_solved"]:
            print("crossword already solved")
        else:
            crossword_solved_list = exist["crossword_solved"]
            crossword_solved_list.append(crossword_id)
            averageTime = exist["averageTime"]
            averageAccuarcy = exist["averageAccuarcy"]
            total_words_pridicted = exist["total_words_pridicted"]
            total_words_pridicted += words
            averageTime = (averageTime + timeTaken) / 2
            averageAccuarcy = (averageAccuarcy + accuarcy) / 2
            averageAccuarcy =   round(averageAccuarcy, 2)

            myquery = { "email": email }
            newvalues = { "$set": { "crossword_solved": crossword_solved_list , "averageTime": averageTime , "averageAccuarcy": averageAccuarcy , "total_words_pridicted": total_words_pridicted } }
            solved_puzzles.update_one(myquery, newvalues)

    else:
        print("inserting data")
        crossword_solved_list = []
        crossword_solved_list.append(crossword_id)
        averageTime = timeTaken
        averageAccuarcy = accuarcy        
        total_words_pridicted = words
        new_data = dict( email = email , crossword_solved = crossword_solved_list , averageTime = averageTime , averageAccuarcy = averageAccuarcy , total_words_pridicted = total_words_pridicted)
        result = solved_puzzles.insert_one(new_data)


