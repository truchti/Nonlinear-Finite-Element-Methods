from Lecture1 import create_IEN
from Lecture1 import node_coors
from Lecture1 import plot_nodes
dim =2
m = 2
M = 1
n = 4
N = 2
q = 3
Q = 1.2
if dim == 1:
    coors = node_coors(dim,m,M)
elif dim ==2:
    coors = node_coors(dim,m,M,n,N)
elif dim == 3:
    coors = node_coors(dim,m,M,n,N,q,Q)
else:
    coors = 0


print(coors)

plot_nodes(coors)



#IEN = create_IEN(2,2,2)
#print(IEN)
#print(len(IEN))
