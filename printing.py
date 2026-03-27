from math import sqrt

def print_grid(num : str, include_string: bool = True):
    size = sqrt(len(num))
    cells = ["\u00B7", "\u25A1"]
    desc = ""
    counter = 0

    for i in range(len(num)-1,-1,-1):
        desc += cells[int(num[i])] + " "
        counter += 1
        if counter%size == 0 and counter !=size**2:
            desc+= "\n"
    if include_string:
        print(num)
    else:
        print()
    print(desc)

def print_moves(move_list):
    for i in move_list:
        print(i)