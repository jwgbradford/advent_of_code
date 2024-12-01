
def get_data(file):
    with open(file) as input_file:
        input_data = input_file.read()
    data_list = input_data.split("\n")
    #data_list.pop(-1) # delete last empty line in list data
    return data_list

def update_pos(move, pos):
    x = pos[0]
    y = pos[1]
    if move == '^':
        y += 1
    elif move == 'v':
        y += -1
    elif move == '>':
        x += 1
    elif move == '<':
        x += -1
    else:
        print ('input error')
    return (x,y)

def update_house_dict(pos, house_dict):
    if  pos in house_dict.keys():
        house_dict[pos] += 1
    else:
        house_dict[pos] = 1
    return house_dict

def track_cells(route_list):
    santa_pos = (0,0)
    robo_pos = (0,0)
    santa_houses = {
            santa_pos : 1
        }
    robo_houses = {
            robo_pos : 1
        }
    for count, route in enumerate(route_list):
        for move in route:
            if count % 2 == 1:
                santa_pos = update_pos(move, santa_pos)
                santa_houses = update_house_dict(santa_pos, santa_houses)
                print(santa_houses)
            else:
                robo_pos = update_pos(move, robo_pos)
                robo_houses = update_house_dict(robo_pos, robo_houses)
                print(robo_houses)
    houses = len(santa_houses) + len(robo_houses)
    return houses

data_in_list = get_data('input_3_test.txt')
houses = track_cells(data_in_list)
print(houses)