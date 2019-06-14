import random

# ............................................................................
#                                 N O D E
# ............................................................................

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val  # key

    @staticmethod # Binary tree calls this method
    def rndTree( depth):
        if (depth <= 0 or random.randrange(10) > 7) :
            return None
        newnode = Node(10+random.randrange(90))
        newnode.left = Node.rndTree(depth-1)
        newnode.right = Node.rndTree(depth-1)
        return newnode

    def print(self):
        print("["+str(self.value)+"]", end = "")

# ............................................................................
#                         B I N A R Y   T R E E
# ............................................................................

class BinaryTree:
    def __init__(self):
        self.root = None

    def randomTree(self, depth):
        random.seed(2300102)
        self.root = Node.rndTree(depth)

    def listInOrdert(self):
        self.listInOrder(self.root)
        print()

    def listInOrder(self, node):
        if (node == None): return
        self.listInOrder(node.left)
        print(node.value, end = " ")
        self.listInOrder(node.right)

    def listPreOrdert(self):
        self.listPreOrder(self.root)
        print()

    def listPreOrder(self, node):
        if (node == None): return
        print(node.value, end = " ")
        self.listPreOrder(node.left)
        self.listPreOrder(node.right)

    def listPostOrdert(self):
        self.listPostOrder(self.root)
        print()

    def listPostOrder(self, node):
        if (node == None): return
        self.listPostOrder(node.left)
        self.listPostOrder(node.right)
        print(node.value, end = " ")


    def count(self, node):
        if (node == None): return 0
        return 1 + self.count(node.left) + self.count(node.right)

    def depth (self, node):
        if (node == None): return -1
        return 1 + max(self.depth(node.left), self.depth(node.right))

# ............................................................................
#                 S T A C K   R E P L A C E S   R E C U R S I O N
# ............................................................................

class StackEl:
    def __init__(self, val, vis):
        self.value = val
        self.visits = vis

class Stack:
  def __init__(self):
    self.storage = []

  def isEmpty(self):
    return len(self.storage) == 0

  def push(self, x, y):
    self.storage.append(StackEl(x, y))

  def pop(self):
    return self.storage.pop()

  def top(self):
    return self.storage[-1]

# ............................................................................
#             R U L E R    W I T H     R E C U R S I O N
# ............................................................................

def ruler (val):
    if (val < 1): return
    ruler(val-1)
    print(val, end = ' ')
    ruler(val-1)

# ............................................................................
#             R U L E R S   W I T H O U T    R E C U R S I O N
# ............................................................................

def rulerNoRec(N):
    stack = Stack()
    stack.push(N,  0)  # 0 == no. of visits to the root
    while(not stack.isEmpty()):
        if (stack.top().value == 0): stack.pop()
        if (stack.top().visits == 0):
            stack.top().visits += 1
            stack.push(stack.top().value-1, 0)
        elif (stack.top().visits == 1):
            print(stack.top().value, end = ' ')
            stack.top().visits += 1
            stack.push(stack.top().value-1, 0)
        elif (stack.top().visits == 2):
            stack.pop()


def rulerWithArrays(N):
    max = 100                        # fixed, for simplicity
    stackVal = [0] * max                # stack Value field
    stackVis = [0] * max                # stack Visits field
    SP = 0                                  # stack pointer
    stackVis[SP] = 0; stackVal[SP] = N
    while (SP >= 0):                         # while unempty
        if (stackVal[SP] == 0): SP -= 1      # pop: in leaf
        if (stackVis[SP] == 0):              # first visit
            stackVis[SP] += 1; SP += 1
            stackVal[SP] = stackVal[SP-1] - 1 # go left
            stackVis[SP] = 0;
        elif (stackVis[SP] == 1):             # second visit
            print(stackVal[SP], end = ' ')    # process the node
            stackVis[SP] += 1;  SP += 1;
            stackVal[SP] = stackVal[SP-1] - 1 # go right
            stackVis[SP] = 0;
        elif (stackVis[SP] == 2): SP -= 1;    # pop: node done


def rulerWithArrays2(N):
    stackVal = [0] * 100;  stackVis = [0] * 100
    SP = 0; stackVis[SP] = 0; stackVal[SP] = N
    while (SP >= 0):                         # while unempty
        if (stackVal[SP] == 0): SP -= 1      # pop: in leaf
        if (stackVis[SP] == 2): SP -= 1      # pop: node done
        else:
            if(stackVis[SP] == 1):             # if second visit
                print(stackVal[SP], end = ' ') # process the node
            stackVis[SP] += 1; SP += 1         # and
            stackVal[SP] = stackVal[SP-1] - 1  # go deeper
            stackVis[SP] = 0


# ............................................................................
#             8   Q U E E N S   P U Z Z L E
# ............................................................................

queenCol = [[0 for x in range(8)] for x in range(8)]
NQ = 8 # number of queens

def positionOK(r, c):                          # r: row, c: column
    for i in range(0, r):                      #same column or
        if (queenCol[i] == c  or \
            abs(r - i) == abs(queenCol[i]-c)): # same diagonal
            return False
    return True


def putQueen(row, col):
    queenCol[row] = col;                # put a queen there
    if row == NQ-1 :                    # if solved
        print(str(queenCol))            # output solution
    else:
        for c in range(0, NQ):          # test all columns
            if (positionOK(row+1, c)):  # if free
                putQueen(row+1, c)      # next row recursion

# ____________________________________________________________________________
# ............................................................................
#                              M A I N
# ____________________________________________________________________________




tree1 = BinaryTree()
tree1.randomTree(4)
tree1.listPreOrdert()
tree1.listInOrdert()
tree1.listPostOrdert()
print("count: ", tree1.count(tree1.root))
print("depth: ", tree1.depth(tree1.root))
print("-----------")

ruler(4); print()
rulerNoRec(4); print()
rulerWithArrays(4); print()
rulerWithArrays2(4); print()
print("-----------")

for col in range(NQ): putQueen(0, col)

