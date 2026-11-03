from printing import print_grid

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

#################################
#        Trim Reductions        #
#################################

# Helper function
def reduce_column(num:str, size:(int,int), offset:int) -> str:
    n : int = size[1]
    acc : str = ""
    for i in range(len(num)):
        if i%n == offset:
            continue
        acc+= num[i]
    return acc

####################################### 

def reduce_bot_row(number, size):
    m : int = size[0]
    n : int = size[1]
    for ch in range(0,n,1):
        if number[ch] == "1":
            return False
    return (number[n:],(m-1,n))

def reduce_top_row(number,size):
    m : int = size[0]
    n : int = size[1]
    for ch in range(n*m-1,n*m-n,-1): #-1???
        if number[ch] == "1":
            return False
    return (number[:n*m-n],(m-1,n))

def reduce_lft_col(number,size):
    m : int = size[0]
    n : int = size[1]
    for ch in range(0,n*m-n,n):
        if number[ch] == "1":
            return False
    return (reduce_column(number,(m,n),0),(m,n-1))

def reduce_rgt_col(number,size):
    m : int = size[0]
    n : int = size[1]
    for ch in range(n-1,n*m-1,n):
        if number[ch] == "1":
            return False
    return (reduce_column(number,(m,n),n-1),(m,n-1))

#######################################

def trim_reduction(num:str, size:(int,int)) -> (str,(int,int)):
    m : int = size[0]
    n : int = size[1]
    while True:
        info = reduce_bot_row(num,(m,n))
        if info:
            num = info[0]
            m = info[1][0]
            n = info[1][1]
        else:
            break
    while True:
        info = reduce_top_row(num,(m,n))
        if info:
            num = info[0]
            m = info[1][0]
            n = info[1][1]
        else:
            break
    while True:
        info = reduce_rgt_col(num,(m,n))
        if info:
            num = info[0]
            m = info[1][0]
            n = info[1][1]
        else:
            break
    while True:
        info = reduce_lft_col(num,(m,n))
        if info:
            num = info[0]
            m = info[1][0]
            n = info[1][1]
        else:
            break
    return (num,(m,n))

#number = "0000000100011100010000000"
#size = (5,5)
#info = trim_reduction(number,size)
#print(info)