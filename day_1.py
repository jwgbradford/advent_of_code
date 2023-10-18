def get_data(file):
    with open(file) as input_file:
        input_data = input_file.read()
    return input_data

starting_list = get_data('input_1.txt')
floor = 0
for char_count, change_floor in enumerate(starting_list):
    if change_floor == '(':
        floor += 1
    if change_floor == ')':
        floor -= 1
    if floor < 0:
        print(char_count + 1) # enumerate counts from 0
        break
print(floor)