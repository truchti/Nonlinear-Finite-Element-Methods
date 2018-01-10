


def node_coors(dim, *args ):
    """ This function takes inputs of the dimension (dim) and then dim*2 of parameters in the order number of elements of dim 1, total length of dim 1, ele 2, len 2, ele 3, len 3"""

    if dim == 1:
        if len(args) == 2:
            m = args[0]
            M = args[1]
            x = 0
            stepi = M/m
            node = [0 for i in range(m + 1)]
            for i in range(0,m+1):
                x = i*stepi
                node[i] = x
            return node
        else:
            print("Warning wrong number of parameters")
            return 'Error'

    elif dim == 2:
        if len(args) == 4:
            m = args[0]
            M = args[1]
            n = args[2]
            N = args[3]
            x = 0
            y = 0
            stepi = M/m
            stepj = N/n
            node = [0 for i in range((m+1)*(n+1))]
            for j in range(0,n+1):
                y = j*stepj
                for i in range(0,m+1):
                    x = i*stepi
                    node[(j*(m+1)+i)] = [x,y]
            return node
        else:
            print("Warning wrong number of parameters")
            return 'Error'

    elif dim == 3:
        if len(args) == 6:
            m = args[0]
            M = args[1]
            n = args[2]
            N = args[3]
            q = args[4]
            Q = args[5]
            x = 0
            y = 0
            z = 0
            stepi = M/m
            stepj = N/n
            stepk = Q/q
            node = [0 for i in range((m + 1) * (n + 1)*(q+1))]
            for k in range(0,q+1):
                z = k * stepk
                for j in range(0, n + 1):
                    y = j * stepj
                    for i in range(0, m + 1):
                        x = i * stepi
                        node[(k*(m+1)*(n+1)+j * (m + 1) + i)] = [x, y, z]

            return node
        else:
            print("Warning wrong number of parameters")
            return 'Error'

    else:
        print("Function not equipped for more than 3 dimensional problem")
        return 'Error'


def create_IEN(x_eles, *args):
    if len(args) == 0:
        nele = x_eles
        dim = 1
    elif len(args) == 1:
        y_eles = args[0]
        nele = y_eles*x_eles
        dim = 2
    elif len(args) == 2:
        y_eles = args[0]
        z_eles = args[1]
        nele = y_eles*x_eles*z_eles
        dim = 3
    else:
        print('Invalid number of arguments')
        return 'Error'
    if dim == 1:
        # pre allocate size of IEN array as IEN(nele,element_nodes)
        element_nodes = 2
        size = 2
        IEN = [[0 for j in range(element_nodes)] for i in range(nele)]
        for e in range(0,nele):
            for a in range(0,element_nodes):
                A = e+a
                IEN[e][a] = A
        return IEN

    elif dim == 2:


        m = x_eles
        element_nodes = 4
        size = 2
        IEN = [[0 for j in range(element_nodes)] for i in range(nele)]
        for e in range(0,nele):
            ill = e%m
            jll = e//m
            for j in range(0,size):
                jc = jll+j
                for i in range(0,size):
                    ic = ill + i
                    A = jc*(m+1)+ic
                    a = j*size+i
                    IEN[e][a] = A
        return IEN

    elif dim == 3:

        m = x_eles
        n = args[0]
        print(m)
        print(n)
        element_nodes = 8
        size = 2
        IEN = [[0 for j in range(element_nodes)] for i in range(nele)]
        for e in range(0,nele):
            ill = (e%m)
            jll = (e//m)%n
            kll = (e//m)//n
            print(['Element', e])
            print([ill,jll, kll])
            for k in range(0,size):
                kc = kll+k
                for j in range(0,size):
                    jc = jll+j
                    for i in range(0,size):
                        ic = ill+i
                        #print([ic, jc, kc])
                        A = kc*(m+1)*(n+1)+jc*(m+1)+ic
                        print(["A =", A])
                        a =i+j*size+k*size*size
                        IEN[e][a] = A
        return IEN
    else:
        print('dimensions not accessible')
        return 'Error'

