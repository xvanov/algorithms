import sys

class magicSquare:
    def __init__(self, n, echoPeri):
        self.N = n;
        self.lineSum = n*(1+n*n) // 2
        self.square =  [[0]*n for i in range(n)]
        self.usedValue = [False] * (n*n+1) # 1..N*N possible values
        self.sumincol = [0]*n
        self.suminrow = [0]*n

        # trace calculations progress
        self.calls = 0;
        self.echoPeriod = echoPeri


    def list(self):
        for i in range(self.N):
            print(self.square[i])



    # debug/visual check display function
    def tracePrint(self):
        if self.calls % self.echoPeriod == 0:
            print("----------------- calls: ", self.calls)
            self.list()


    # ...........  S E A R C H   B A S I C   --  S L O W ............................

    def search0(self, y, x):

        # count no of calls ~~ measure effectivity
        self.calls += 1

        self.tracePrint()

        # solution found ?
        if ( y == self.N):
            if self.checkSolution() == False:
                return
            self.list()

            sys.exit(0)
            return;

        #  try to put all available values at position x, y
        # and recursively solve the rest

        for val in range( 1, self.N*self.N+1 ):

            # exclude used values
            if self.usedValue[val]:
                continue

            # put the value on the square
            self.square[y][x] = val;
            self.usedValue[val] = True

            # go to next cell
            if x < self.N-1:
                self.search0( y, x+1 )
            else:
                self.search0( y+1, 0 )

            # remove the value from the square
            self.square[y][x] = 0;
            self.usedValue[val] = False




    # ...........  S E A R C H  STANDARD  .....................................

    def search1(self, y, x):

        # count no of calls ~~ measure effectivity
        self.calls += 1

        self.tracePrint()

        # solution found ?
        if ( y == self.N):
            self.list()
            sys.exit(0)
            return


        #  try to put all available values at position x, y
        # and recursively solve the rest

        for val in range (1, self.N*self.N+1):

            if not self.acceptableMove(val, y, x):
                continue

            # with acceptable value, do the recursion

            # register changes
            self.usedValue[val] = True
            self.suminrow[y] = self.suminrow[y] + val;
            self.sumincol[x] = self.sumincol[x] + val;
            self.square[y][x] = val;

            # recursively search the rest of the square
            if x < self.N-1:
                self.search1( y, x+1)
            else:
                self.search1( y+1, 0)

            # un-register the changes
            self.square[y][x] = 0;
            self.sumincol[x] = self.sumincol[x] - val;
            self.suminrow[y] = self.suminrow[y] - val;
            self.usedValue[val] = False


       # ...........  S E A R C H   SPEEDUP .....................................

    def search2(self, y, x):
        # count no of calls ~~ measure effectivity
        self.calls += 1

        self.tracePrint()

        # solution found ?
        if y == self.N:
            self.list()
            sys.exit( 0 )
            return

        #  try to put all available values at position x, y
        # and recursively solve the rest
        # same as in standard

        for val in range( 1, self.N*self.N+1 ):

            if not self.acceptableMove(val, y, x):
                continue

            # with acceptable value, do the recursion

            # register changes
            self.usedValue[val] = True
            self.suminrow[y] = self.suminrow[y] + val
            self.sumincol[x] = self.sumincol[x] + val

            self.square[y][x] = val;

            # recursively search the rest of the square but
            # choose the next cell more cleverly so that
            # the acceptability test happens more often

            # horizontal direction
            if x >= y :
                if x < self.N-1:
                    self.search2( y, x+1 )
                else:
                    self.search2( y+1, y ) # swap direction

            # vertical direction
            if x < y :
                if y < self.N-1:
                    self.search2( y+1, x )
                else:
                    self.search2( x+1, x+1 ) # swap direction

            # un-register the changes
            self.sumincol[x] = self.sumincol[x] - val
            self.suminrow[y] = self.suminrow[y] - val
            self.usedValue[val] = False


    # ...........  C H E C K   M O V E    A C C E P T A B I L I T Y ....................

    def acceptableMove(self, val, y, x):
        # exclude used values
        if self.usedValue[val]:
            return False

        # exclude unacceptable sums horizontally
        if x == self.N-1:
            if val+self.suminrow[y] != self.lineSum:
                return False

        # exclude unacceptable sums vertically
        if y == self.N-1:
            if val+self.sumincol[x] != self.lineSum:
                return False

        # otherwise seems promising (with caution!)
        return True


    # ...........  SOLUTION CHECKS  .....................................

    def checkSolution(self):
        for xy in range(self.N):
            if self.horizSum(xy) != self.lineSum:  return False
            if self.verticSum(xy) != self.lineSum:  return False
        return True

    def horizSum(self, y):
        return sum(self.square[y])

    def verticSum(self, x):
        sum = 0
        for y in range(self.N):
            sum += self.square[y][x]
        return sum



    # ............... E N D   O F   C L A S S ...............................


# ____________________________________________________________________________
#                              M A I N
# ____________________________________________________________________________

ms = magicSquare(5, 100000)
ms.search1(0,0)
#ms.searchSlow(0,0)
'''
[1, 2, 13, 24, 25]
[3, 8, 14, 19, 21]
[16, 17, 15, 7, 10]
[22, 18, 11, 9, 5]
[23, 20, 12, 6, 4]

search2  6x6:
[1, 2, 3, 34, 35, 36]
[4, 5, 20, 23, 29, 30]
[10, 24, 26, 16, 17, 18]
[31, 25, 19, 14, 15, 7]
[32, 27, 21, 13, 6, 12]
[33, 28, 22, 11, 9, 8]
----------------- calls:  117520545

'''


