import json




base_path='../../data/puzzles/json/quick'


 
def open_cells(crosswordid):

    file= base_path + str(crosswordid) +'.json'

    clue_file = open(file)
    data = json.load(clue_file)

    list=[]
    j=0
    for i in data['entries']:
 
        direction = data['entries'][j]['direction']
        length = data['entries'][j]['length']
        position =data['entries'][j]['position']
        id_name= "input" + str(position['x']) + '-' +  str(position['y'])
        if id_name not in list:
            list.append(id_name)
        j += 1

        if direction == "across" :
            next_x_val=position['x']
            for i in range(length-1):
                next_x_val  = next_x_val+1
                next_id_name= "input" + str(next_x_val) + '-' +str(position['y'])
                if next_id_name not in list:
                    list.append(next_id_name)

        if direction == 'down'  :
            next_y_val=position['y']
            for i in range(length-1):
                next_y_val  = next_y_val + 1
                next_id_name= "input" +  str(position['x']) + '-' +str(next_y_val)
                if next_id_name not in list:
                    list.append(next_id_name)
       

    clue_file.close()



    return list



def all_cells():

    all_ids=[]
    for i in range(13):
        for j in range(13):
            temp_id='input' + str(i) + '-' + str(j)
            if temp_id not in all_ids:
                all_ids.append(temp_id)

    return all_ids


def  blocked_cells(crosswordid):

    all_ids=all_cells()
    not_blocked=open_cells(crosswordid)

    blocked_cell_list =[]

    for i in all_ids:
        if i not in not_blocked:
            blocked_cell_list.append(i)


    return blocked_cell_list




def read_clue_data(crosswordid):
    file=base_path+ str(crosswordid) +'.json'


    clue_file = open(file)
    clue_data = json.load(clue_file)
    clue_file.close()

    return clue_data


