import sys

#function for minimum one of the variable in list is true
def minimumOne(List):
    n_Value = ""
    for list_a in List:
        n_Value = n_Value + " " +str(list_a)
    n_Value = n_Value + " 0\n"
    return n_Value

#function for maximum one of the variable in list is true
def maximumOne(List) :
    n_Value = ""
    for list_a in List :
        for list_b in List[List.index(list_a ) + 1 :] :
            n_Value = n_Value + " -" + str(list_a) + " -" + str(list_b) + " 0\n"
    return n_Value

#function to map position of r and c in an NxN matrix
#position when the grid is stored linearly by rows
def varmap(row,column,size):
    return row * size + column + 1

#funciton for precisely one variable in list is true
def preciselyOne(List):
    n_Value = ""
    n_Value = n_Value + minimumOne(List)
    n_Value = n_Value + maximumOne(List)
    return n_Value

#Read Input as arguments from termial or shell script 
if len(sys.argv) > 1:
    size = int(sys.argv[1])
else: # assigning a default value as 4 as it will unsatisfiable for 1, 2, 3
    size = 4

#Checking Input if N < -1 then termiate the program 
if size < 1:
    print("Error size<1")
    sys.exit(0)

#Start Solver
print("c SAT Expression for size = " + str(size))
grid = size * size
print("c Board has " + str(grid) + " positions")
#Precisely 1 queen per row
n_Value = ""
for row in range(0,size):
    List = []
    for column in range(0,size):
        position = varmap(row,column,size)
        List.append(position)
    n_Value = n_Value + preciselyOne(List)
#Minimum 1 queen per column
for column in range(0,size):
    List = []
    for row in range(0,size):
        position = varmap(row,column,size)
        List.append(position)
    n_Value = n_Value + preciselyOne(List)

#Maximum 1 queen per negative diagonal from left
for row in range(size-1,-1,-1):
    List = []
    for x in range(0,size-row):
        List.append(varmap(row+x,x,size))
    n_Value = n_Value + maximumOne(List)
#Maximum 1 queen per negative diagonal from top
for column in range(1,size):
    List = []
    for x in range(0,size-column):
        List.append(varmap(x,column+x,size))
    n_Value = n_Value + maximumOne(List)
#Maximum 1 queen per positive diagonal from right
for row in range(size-1,-1,-1):
    List = []
    for x in range(0,size-row):
        List.append(varmap(row+x,size-1-x,size))
    n_Value = n_Value + maximumOne(List)
#Maximum 1 queen per positive diagonal from top
for column in range(size-2,-1,-1):
    List = []
    for x in range(0,column+1):
        List.append(varmap(x,column-x,size))
    n_Value = n_Value + maximumOne(List)


print('p cnf ' + str(size*size) + ' ' + str(n_Value.count('\n')), file=open('input.cnf', 'w'))
print(n_Value, file=open('input.cnf', 'a'))