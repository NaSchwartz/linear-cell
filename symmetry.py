from printing import print_grid

#################################
#           Translation         # size
#################################

def translate_down(num : str, m : int, n : int) -> str :
    if num[:n] == "0"*n:
        return num[n:] + "0"*n
    else:
        return num

def translate_up(num : str, m : int, n : int) -> str :
    if num[-n:] == "0"*n:
        return "0"*n + num[:-n]
    else:
        return num

def translate_right(num : str, m : int, n : int) -> str :
    check = ""
    for i in range(m):
        check += num[i * m]
    if check == "0"*m:
        return num[1:]+num[0]
    else:
        return num

def translate_left(num : str, m : int, n : int) -> str :
    check = ""
    for i in range(m):
        check += num[i*m + m-1]
    if check == "0"*m:
        return num[-1]+num[:-1]
    else:
        return num

#################################
#           Reflection          #
#################################

def vert_reflection(num : str, m : int, n : int) -> str :
    # Split the "grid" into rows
    rows = [""]*m
    for i in range(m):
        rows[i] = num[i*n:i*n+n]
    
    # Concatenate the list in reverse order, then return
    desc = ""
    for i in range(m-1,-1,-1):
        desc += rows[i]
    return desc

# General horizontal reflection
def horz_reflection(num : str, m : int, n : int) -> str :
    # Split the "grid" into columns
    columns = [""]*n
    for i in range(n):
        for j in range(m):
            columns[i] += num[n*j + i]
    # Nest the list elements in reverse, then return
    desc = ""
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            desc += columns[j][i]
    return desc

#################################
#           Rotation            #
#################################

# WARNING: preforming a rotation with n \neq m swaps their values
# rows into columns (clockwise)
def negative_rotation(num : str, m : int, n : int) -> (str,int,int) :
    # Split the "grid" into rows
    #print(num,m,n)
    rows = [""]*m
    for i in range(m):
        rows[i] = num[i*n:i*n+n]
    # Turn rows into columns
    desc = ""
    for i in range(n):
        for j in range(m):
            desc += rows[m-j-1][i]

    return (desc,n,m)

# columns into rows (counter-clockwise)
def positive_rotation(num : str, m : int, n : int) -> (str,int,int) :
    # Split the "grid" into rows
    rows = [""]*m
    for i in range(m):
        rows[i] = num[i*n:i*n+n]
    # Turn rows into columns, but in reverse order
    desc = ""
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            desc += rows[m-j-1][i]

    return (desc,n,m)

#################################
#        Trim Reductions        #
#################################

# Helper function
def reduce_column(num:str, n:int, offset:int) -> str:
    acc : str = ""
    for i in range(len(num)):
        if i%n == offset:
            continue
        acc+= num[i]
    return acc

####################################### 

def reduce_bot_row(number, m, n): # should be fine
    for ch in range(0,n,1):
        if number[ch] == "1":
            return False
    return (number[n:],m-1,n)

def reduce_top_row(number, m, n):
    for ch in range(n*m-1,n*m-n-1,-1):
        if number[ch] == "1":
            return False
    return (number[:n*m-n],m-1,n)

def reduce_lft_col(number, m, n):
    for ch in range(0,n*m-n+n,n): #    for ch in range(0,n*m-n,n):
        if number[ch] == "1":
            return False
    return (reduce_column(number,n,0),m,n-1)

def reduce_rgt_col(number, m, n):
    for ch in range(n-1,n*m-1+n,n):
        if number[ch] == "1":
            return False
    return (reduce_column(number,n,n-1),m,n-1)

#######################################

def trim_reduction(num:str, m:int, n:int) -> (str,int,int):
    #print(f"trimming: {num,m,n}")
    while True:
        if m==0 or n==0:
            return (num,m,n)
        #print(f"bot: {num,m,n}")
        info = reduce_bot_row(num, m, n)
        if info:
            num,m,n = info
        else:
            break
    while True:
        if m==0 or n==0:
            return (num,m,n)
        #print(f"top: {num,m,n}")
        info = reduce_top_row(num, m, n)
        if info:
            num,m,n = info
        else:
            break
    while True:
        if m==0 or n==0:
            return (num,m,n)
        #print(f"right: {num,m,n}")
        info = reduce_rgt_col(num, m, n)
        if info:
            num,m,n = info
        else:
            break
    while True:
        if m==0 or n==0:
            return (num,m,n)
        #print(f"left: {num,m,n}")
        info = reduce_lft_col(num, m, n)
        if info:
            num,m,n = info
        else:
            break
    return (num,m,n)

#print(trim_reduction('000010',3,2))