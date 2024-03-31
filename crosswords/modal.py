from db.db import puzzles




### puzzles data and all its funtions


##returns the whole puzzle file
def puzzle_data(crosswordid):
    data = puzzles.find_one({"number": crosswordid })
    return data



##returns list of id off all the open (not disable) cell
def open_cells(data):
    # data = puzzle_data(crosswordid)
    list=[]
    inputId_clueId = {}
    
    j=0
    for i in data['entries']:
        temp = []
        direction = i['direction']
        length = i['length']
        position =i['position']
        id_name= "input" + str(position['x']) + '-' +  str(position['y'])
        temp.append(id_name)
        if id_name not in list:
            list.append(id_name)

        j += 1

        if direction == "across" :
            next_x_val=position['x']
            for _ in range(length-1):
                next_x_val  = next_x_val+1
                next_id_name= "input" + str(next_x_val) + '-' +str(position['y'])
                temp.append(next_id_name)
                if next_id_name not in list:
                    list.append(next_id_name)

        if direction == 'down'  :
            next_y_val=position['y']
            for _ in range(length-1):
                next_y_val  = next_y_val + 1
                next_id_name= "input" +  str(position['x']) + '-' +str(next_y_val)
                temp.append(next_id_name)
                if next_id_name not in list:
                    list.append(next_id_name)


        inputId_clueId[i['id']] = temp

        
    return list ,inputId_clueId



def all_cells(dimensions):

    all_ids=[]
    for i in range(int(dimensions['rows'])):
        for j in range(int(dimensions['cols'])):
            temp_id='input' + str(i) + '-' + str(j)
            if temp_id not in all_ids:
                all_ids.append(temp_id)

    return all_ids


def  blocked_cells(data):

    all_ids=all_cells(data['dimensions'])
    not_blocked , inputId_clueId = open_cells(data)

    blocked_cell_list =[]

    for i in all_ids:
        if i not in not_blocked:
            blocked_cell_list.append(i)

    return blocked_cell_list , inputId_clueId


def getgrid(clue_data):
    grid =[["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""],
       ["","","","","","","","","","","","",""]]
    
    order = []

    for clue in clue_data['entries']:
        if clue["direction"] == "across":
            x=clue["position"]["x"] 
            y=clue["position"]["y"]
            for i in range(clue["length"]):
                    positon = [x,y]
                    order.append(positon)
                    grid[x][y]=clue["solution"][i]
                    x+=1
        if clue["direction"] == "down":
            x=clue["position"]["x"] 
            y=clue["position"]["y"]
            for i in range(clue["length"]):
                    positon = [x,y]
                    order.append(positon)
                    grid[x][y]=clue["solution"][i]
                    y+=1
    

    return  grid , order

# grid , order = grid(puzzle_data(10746))
# print(grid)
# print(order)






# class SignupForm(FlaskForm):
#     userName = StringField("User Name", validators=[DataRequired()])
#     email = EmailField("Your Email", validators=[DataRequired()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     conPassword = PasswordField('Confirm Password', validators=[DataRequired()])
#     submit = SubmitField("Submit")

# user = mydb["users"]






# def addUser( userName , email, pass_hash):

#     user_data = dict(userNmae = userName, email = email, pass_hash = pass_hash)
#     result = user.insert_one(user_data)
#     print(result)


# def alreadyExit(email):
#         data = user.find_one({ "email": email })
#         if data:
#             return True
#         else:
#             return False


# def userData(email):
#     data = user.find_one({ "email": email })
#     return data






