

def node_coors(dim, *args ):
    """ This function takes inputs of the dimension (dim) and then dim*2 of parameters in the order number of elements of dim 1, total length of dim 1, ele 2, len 2, ele 3, len 3"""
    #sorts arguments in to correct variables
    if dim == 1:
        if len(args) == 2:
            m = args[0]
            M = args[1]
        else:
            print("Warning wrong number of parameters")
        x = 0
        stepi = M/m

    elif dim == 2:
        if len(args) == 4:
            m = args[0]
            M = args[1]
            n = args[2]
            N = args[3]
        else:
            print("Warning wrong number of parameters")

        x = 0
        y = 0
        stepi = M/m
        stepj = N/n

    elif dim == 3:
        if len(args) == 6:
            m = args[0]
            M = args[1]
            n = args[2]
            N = args[3]
            q = args[4]
            Q = args[5]
        else:
            print("Warning wrong number of parameters")
        x = 0
        y = 0
        z = 0
        stepi = M/m
        stepj = N/n
        stepk = Q/q
    else:
        print("Function not equipped for more than 3 dimensional problem")


