from math import sqrt

def print_grid(num : str, m:int, n:int, include_string:bool = True):
    cells = ["\u00B7", "\u25A1"]
    desc = ""
    counter = 0

    for i in range(len(num)-1,-1,-1):
        desc += cells[int(num[i])] + " "
        counter += 1
        if counter%n == 0 and counter !=m*n:
            desc+= "\n"
    if include_string:
        print()
        print(num)
    else:
        print()
    print(desc)

def print_moves(move_list):
    for i in move_list:
        print(i)