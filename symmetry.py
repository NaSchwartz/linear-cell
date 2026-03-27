from printing import print_grid, set_size

#################################
#           Translation         # size
#################################

def translate_down(num : str, size : int) -> str :
    if num[:size] == "0"*size:
        return num[size:] + "0"*size
    else:
        return num

def translate_up(num : str, size : int) -> str :
    if num[-size:] == "0"*size:
        return "0"*size + num[:-size]
    else:
        return num

def translate_right(num : str, size : int) -> str :
    check = ""
    for i in range(size):
        check += num[i * size]
    if check == "0"*size:
        return num[1:]+num[0]
    else:
        return num

def translate_left(num : str, size : int) -> str :
    check = ""
    for i in range(size):
        check += num[i*size + size-1]
    if check == "0"*size:
        return num[-1]+num[:-1]
    else:
        return num

#size = 4
#print_grid("0000011001100000")
#print_grid(translate_left("0000011001100000"))
#print_grid(translate_right("0000011001100000"))
#print_grid(translate_down("0000011001100000"))
#print_grid(translate_up("0000011001100000"))


#################################
#           Reflection          #
#################################

# 3x3 example
def vert_reflection3x3(num : str, size : int) -> str :
    return num[-size:] + num[size:-size] + num[:size]
# 3x3 example
def horz_reflection3x3(num : str, size : int) -> str :
    left = ""
    right = ""
    center = ""
    for i in range(size):
        left += num[i*size + size-1]
        center += num[i*size + size-2]
        right += num[i * size]

    desc = ""
    for i in range(size):
        desc += left[i] + center[i] + right[i]
    return desc


# General vertical reflection
def vert_reflection(num : str, size : int) -> str :
    # Split the "grid" into rows
    rows = [""]*size
    for i in range(size):
        rows[i] = num[i*size:i*size+size]
    
    # Concatenate the list in reverse order, then return
    desc = ""
    for i in range(size):
        desc += rows[size-i-1]
    return desc

# General horizontal reflection
def horz_reflection(num : str, size : int) -> str :
    # Split the "grid" into columns
    columns = [""]*size
    for i in range(size):
        for j in range(size):
            columns[i] += num[size*j + i]
    
    # Nest the list elements in reverse, then return
    desc = ""
    for i in range(size):
        for j in range(size):
            desc += columns[size-j-1][i]
    return desc

#size = 4
#print_grid("0111110101011100")
#print_grid(vert_reflection("0111110101011100"))
#print_grid(horz_reflection("0111110101011100"))


#################################
#           Rotation            #
#################################

# columns into rows (counter-clockwise)
def positive_rotation(num : str, size : int) -> str :
    # Split the "grid" into columns
    columns = [""]*size
    for i in range(size):
        for j in range(size):
            columns[i] += num[size*j + i]

    # Turn the columns into rows
    desc = ""
    for i in range(size):
        desc += columns[size-i-1]
    return desc

# rows into columns (clockwise)
def negative_rotation(num : str, size : int) -> str :
    # Split the "grid" into rows
    rows = [""]*size
    for i in range(size):
        rows[i] = num[i*size:i*size+size]
    
    # Turn rows into columns
    desc = ""
    for i in range(size):
        for j in range(size):
            desc += rows[size-j-1][i]
    return desc

#size = 4
#Tools.print_grid("1110101011001000")
#Tools.print_grid(positive_rotation("1110101011001000"))
#Tools.print_grid(negative_rotation("1110101011001000"))


#################################
#           Normal Form         #
#################################

def normal_forms(num : str, size : int):
    forms = ["","","",""]
    curr = num
    for i in range(len(forms)):
        forms[i] = curr
        forms[i] = move_to_bot_right(forms[i], size)
        curr = positive_rotation(curr, size)
    return forms

def move_to_bot_right(num : str, size : int) -> str :
    prev = num
    curr = translate_down(num, size)
    while True:
        if prev == curr:
            break
        else:
            prev = curr
            curr = translate_down(curr, size)
    
    prev = curr
    curr = translate_right(curr, size)
    while True:
        if prev == curr:
            break
        else:
            prev = curr
            curr = translate_right(curr, size)
    
    return curr

#print_grid("0000000000000001")
#print_grid(move_to_bot_right("0000000000000001"))

#for i in normal_forms("101101000"):
    #print_grid(i)
