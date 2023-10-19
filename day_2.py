import regex

def get_data(file):
    with open(file) as input_file:
        input_data = input_file.read()
    data_list = input_data.split("\n")
    data_list.pop(-1) # delete last empty line in list data
    return data_list

def add_wrapping(current_wrap, x, y, z):
    side_1 = x * y
    side_2 = y * z
    side_3 = z * x
    current_wrap += (2*side_1+ 2*side_2 + 2*side_3)
    if side_1 < side_2 and side_1 < side_3:
        current_wrap += side_1
    elif side_2 < side_3:
        current_wrap += side_2
    else:
        current_wrap += side_3
    return current_wrap

def add_ribbon(current_length, x, y, z):
    if x < y or x < z:
        current_length += (2 * x)
    if y < x or y < z:
        current_length += (2 * y)
    if z < x or z < y:
        current_length += (2 * z)
    if x == y and y == z: # if they're all the same length
        current_length += (4 * x)
    if (x < y and y == z): # two equal long sides
        current_length += (2 * y)
    elif (
        (y < x and x == z)
        or
        (z < x and x == y)
        ):
        current_length += (2 * x)
    current_length += (l * h * w)
    return current_length

data_in_list = get_data('input_2.txt')

wrapping_paper = 0
ribbon_length = 0

for parcel in data_in_list:
    x_pos_1 = parcel.find("x")
    x_pos_2 = parcel.find("x", x_pos_1 + 1)

    l = int(parcel[0:x_pos_1:1])
    w = int(parcel[x_pos_1 + 1:x_pos_2:1])
    h = int(parcel[x_pos_2 + 1:99:1])
    #ribbon_length = 0
    ribbon_length = add_ribbon(ribbon_length, l, w, h)

    #print(ribbon_length)
    # wrapping_paper = add_wrapping(wrapping_paper, l, w, h)

print(ribbon_length) # still wrong
#print(wrapping_paper)
