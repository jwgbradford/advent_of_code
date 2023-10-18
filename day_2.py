import regex

def get_data(file):
    with open(file) as input_file:
        input_data = input_file.read()
    data_list = input_data.split("\n")
    data_list.pop(-1) # delete last empty line in list data
    return data_list

starting_list = get_data('input_2.txt')

wrapping_paper = 0

for parcel in starting_list:
    x_pos = parcel.find("x")
    l = int(parcel[0:x_pos:1])
    x_pos_2 = parcel.find("x", x_pos + 1)
    w = int(parcel[x_pos+1:x_pos_2:1])
    h = int(parcel[x_pos_2+1:99:1])
    side_1 = l * w
    side_2 = w * h
    side_3 = h * l
    wrapping_paper = wrapping_paper + (2*side_1+ 2*side_2 + 2*side_3)
    if side_1 < side_2 and side_1 < side_3:
        wrapping_paper = wrapping_paper + side_1
    elif side_2 < side_3:
        wrapping_paper = wrapping_paper + side_2
    else:
        wrapping_paper = wrapping_paper + side_3
print(wrapping_paper)
