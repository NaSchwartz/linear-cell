# Grid size
size = 3

import Tools

#################################
#           Translation         #
#################################

def translate_down(num : str) -> str :
    if num[:size] == "0"*size:
        return num[size:] + "0"*size
    else:
        return num

def translate_up(num : str) -> str :
    if num[-size:] == "0"*size:
        return "0"*size + num[:-size]
    else:
        return num

def translate_right(num : str) -> str :
    check = ""
    for i in range(size):
        check += num[i * size]
    if check == "0"*size:
        return num[1:]+num[0]
    else:
        return num

def translate_left(num : str) -> str :
    check = ""
    for i in range(size):
        check += num[i*size + size-1]
    if check == "0"*size:
        return num[-1]+num[:-1]
    else:
        return num

#Tools.print_grid("000010000")
#Tools.print_grid(translate_left("000010000"))
#Tools.print_grid(translate_right("000010000"))
#Tools.print_grid(translate_down("000010000"))
#Tools.print_grid(translate_up("000010000"))

#################################
#           Reflection          #
#################################

# only size 3 for now
def vert_reflection(num : str) -> str :
    return num[-size:] + num[size:-size] + num[:size]
# only size 3 for now
def horz_reflection(num : str) -> str :
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

Tools.print_grid("011110101")
# horz_reflection("011110101")
Tools.print_grid(horz_reflection("011110101"))


#################################
#           Rotation            #
#################################