import sys, Tools

need_to_change_size = True

while True:
    # change the grid size
    if need_to_change_size:
        try:
            size = int(input("Enter the side length of the square grid:\t"))
            if size < 1:
                raise Exception("")
        except:
            print("\ninvalid entry. size must be a natural number\n")
            continue
        need_to_change_size = False
    
    # Standard analyzing loop
    state = input("Please enter state to analyze:\t")
    try:
        Tools.optimal_move(state, size)
    except Exception as e:
        print("\ninvalid entry. Unrecognizable string, or incorrect size\n")
        print(e)
        sys.exit()
    
    # post-analyzation, fun visuals and useful records for the user
    while True:
        u_inp = input("Post-analyzation. Enter a number to select that option, all other entires will restart the main loop.\n"
        +"[ 1 ] See current memory\n"
        +"[ 2 ] Clear current memory\n"
        +"[ 3 ] See all p-positions found so far\n"
        +"[ 4 ] Change grid size\n"
        +"[ 5 ] Exit program\n"
        +"\nChoice:\t")
        match (u_inp):
            case "1":
                print("Flase = N-Position, True = P-Position")
                print(Tools.memo)
                print()
            case "2":
                Tools.clear_memory()
                print("\nMemory cleared!\n")
            case "3":
                cells_cnt = input("type the minimum number of cells to be in each state (default 0):\t")
                print()
                if not cells_cnt.strip():
                    cells_cnt = "0"
                # Either display binary encodings or the pictures.
                Tools.print_p_pos_cells(int(cells_cnt), input("type \'v\' to see visuals:\t")=="v")
                print()
            case "4":
                need_to_change_size = True
                break
            case "5":
                sys.exit()
            case _:
                break