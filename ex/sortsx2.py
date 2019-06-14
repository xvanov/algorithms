
def swap (arr, i, j):
    x = arr[i]; arr[i] = arr[j]; arr[j] = x;
    # Python would say: arr[i], arr[j] = arr[j], arr[i]


# ---------------------------------------------------------------------
#    S E L E C T   S O R T
# ---------------------------------------------------------------------
def selectSort (arr):
    n = len(arr)
    for i in range(n-1):
        jmin = i
        # select minimum
        for j in range(i+1, n):
            if arr[j] < arr[jmin]:
                jmin = j
        # put minimum to its place
        swap(arr, i, jmin)


# ---------------------------------------------------------------------
#    I N S E R T   S O R T
# ---------------------------------------------------------------------
def insertSort (arr):
    n = len(arr)
    for i in range(1, n):
        # find & make place for arr[i]
        insVal = arr[i]
        j = i-1
        while j >= 0 and arr[j] > insVal:
            arr[j+1] = arr[j]
            j -= 1;
        # insert arr[i] to the correct place
        arr[j+1] = insVal

# ---------------------------------------------------------------------
#    B U B L E   S O R T   (deprecated)
# ---------------------------------------------------------------------
def bubbleSort (arr):
    for lastPos in range (len(arr)-1, -1, -1):  # decreasing lastPos
        for j in range(lastPos):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)

# ---------------------------------------------------------------------
#    Q U I C K   S O R T
# ---------------------------------------------------------------------
def qSort (a, low, high):
    iL = low; iR = high;
    pivot = a[low]
    while True:
        if iL > iR: break
        while a[iL] < pivot: iL += 1
        while a[iR] > pivot: iR -= 1
        if iL < iR:
            swap(a, iL, iR)
            iL += 1; iR -= 1
        else:
            if iL == iR: iL += 1; iR -= 1

    if low < iR:  qSort(a, low, iR)
    if iL < high: qSort(a, iL, high)


# ---------------------------------------------------------------------
#    M E R G E    S O R T
# ---------------------------------------------------------------------
def merge (inArr, outArr, low, high):
    half = (low+high) // 2
    i1 = low
    i2 = half + 1
    j = low;

    # compare and merge
    while i1 <= half and i2 <= high:
        if inArr[i1] <= inArr[i2]:
            outArr[j] = inArr[i1]; i1 += 1
        else:
            outArr[j] = inArr[i2]; i2 += 1
        j += 1

    # copy the rest
    while i1 <= half:
        outArr[j] = inArr[i1]; i1 += 1; j += 1;
    while i2 <= high:
        outArr[j] = inArr[i2]; i2 += 1; j += 1;

def _mergeSort (arr, auxArr, low, high):
    if low >= high: return   # too small!
    half = (low+high) // 2

    # sort to auxArr
    _mergeSort(arr, auxArr, low, half);    # left half
    _mergeSort(arr, auxArr, half+1, high); # right half
    merge(arr, auxArr, low, high)

    # copy back from auxArr
    for i in range(low, high+1):
        arr[i] = auxArr[i]

def mergeSort (arr):
    auxArr = [0] * len(arr)
    _mergeSort(arr, auxArr, 0, len(arr)-1)


# improved usage of auxArr
def _mergeSortX (arr, auxArr, low, high, depth):
    if low >= high: return
    half = (low+high) // 2

    _mergeSortX(arr, auxArr, low, half, depth+1);
    _mergeSortX(arr, auxArr, half+1, high, depth+1);

    if depth%2 == 0: merge(auxArr, arr, low, high)
    else:            merge(arr, auxArr, low, high)


def mergeSortX (arr):
    auxArr = arr[:]  # auxArr = copy(arr)
    _mergeSort(arr, auxArr, 0, len(arr)-1)

# ---------------------------------------------------------------------
#    H E A P   S O R T
# ---------------------------------------------------------------------
# beware! array sorted is arr[0] ... arr[n-1]
# therefore the children have indices 2i+1 and 2i+2
def repairTop (arr, top, bottom):
    i = top      # arr[2*i-1] and arr[2*i]
    j = i*2+1    # are successors of arr[i]
    topVal = arr[top]
    _checks = 0

    # try to find a successor < topVal
    if j < bottom:
        if arr[j] > arr[j+1]:
            j += 1
        _checks += 1

    # while successors < topVal move successors up
    while j <= bottom and topVal > arr[j]:
        arr[i] = arr[j]
        i = j; j = j*2+1     # move to next suceessor
        if j < bottom:
            if arr[j] > arr[j+1]:
                j += 1
            _checks += 1

    # put topVal to its correct place
    arr[i] = topVal
    return _checks

# beware!  array sorted is arr[0] ... arr[n-1]
# slides explain case arr[1] ... arr[n]
def heapSort (arr):
    n = len(arr)-1

    checks = 0

    # create a heap
    for i in range(n//2, -1, -1): # progress backwards!
        checks += repairTop(arr, i, n)

    for i in range(n, 0, -1): # progress backwards!
        swap(arr, 0, i)
        checks += repairTop(arr, 0, i-1)
    print(checks)



# beware!  array is arr[1] ... arr[n]
# bottom == ndx of last elem
def heapInsert(arr, x, bottom):
    bottom += 1   # expand the heap space
    j = bottom
    i = j/2      #parent index

    while i > 0 and arr[i] > x:
        arr[j] = arr[i]       # move elem down the heap
        j = i; i /= 2         # move indices up the heap

    arr[i] = x            # put inserted elem to its place
    return bottom



# ---------------------------------------------------------------------
#    C O U N T I N G   S O R T
# ---------------------------------------------------------------------

def countingSort(arr, maxval):
    supparr = [0]*(maxval+1) # support array : frequencies and positions
    # fill support - frequencies array
    for x in arr:
        supparr[x] += 1
    # turn frequencies into output positions
    supparr[0] -= 1          # easy fix for 0-based arrays
    for i in range(1, len(supparr)):
        supparr[i] += supparr[i-1]
    # produce output
    output = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])
        output[supparr[arr[i]]] = arr[i]
        supparr[arr[i]] -= 1
    return output

# ---------------------------------------------------------------------
#    R A D I X   S O R T
# ---------------------------------------------------------------------

def radixInit(A, S, E, D):
    pos = len(A[0]) - 1   #  last char in string
    for i in range(len(S)):
        S[i], E[i] = -1, -1
    for i in range(len(A)):
        c = ord(A[i][pos])  # char to index
        if S[c] == -1:
            S[c], E[c] = i, i  # start new list
        else:              # extend existing list
            D[E[c]],  E[c] = i, i


def radixStep(A, pos, S, E, D, S1, E1, D1):
    for i in range(len(S)):
        S1[i], E1[i] = -1, -1   # init arrays

    for i in range(len(S)):
        if S[i] != -1:    # unempty list
            j = S[i]      # traverse old list
            while True:
                c = ord(A[j][pos])
                if S1[c] == -1:
                    S1[c], E1[c] = j, j # start new list
                else:       # extend existing list
                    D1[E1[c]], E1[c] = j, j
                if j == E[i]:
                    break
                j = D[j]    # next string index

def radixSort(A):
    alphabetsize = 128    # 2^16 in unicode
    S = [0] * alphabetsize
    E = [0] * alphabetsize
    D = [0] * alphabetsize
    S1 = [0] * alphabetsize
    E1 = [0] * alphabetsize
    D1 = [0] * alphabetsize

    radixInit(A, S ,E, D)  # 1st pass with last char

    for p in range(len(A[0])-2, -1, -1):
        radixStep(A, p, S, E, D, S1, E1, D1)
        S, S1 = S1, S  # just swap arrays
        E, E1 = E1, E  #  ditto
        D, D1 = D1, D  #  ditto

    radixOutput(A, S, E, D)  # print sorted A


def radixOutput(A, S, E, D):
    for i in range(len(S)):
        if S[i] != -1:    # unempty list
            j = S[i]      # traverse the list
            while True:
                print(A[j])
                if j == E[i]: break
                j = D[j]    # next string index


# =====================================================================
#   M A I N
# =====================================================================


#arr = [5,4,3,2,9,8,7,6]
arr = [999, 23,29,27,4,28,17,1,24,6,30]
#arr = [x for x in range(0,1000)]
#bubbleSort(arr)
#selectSort(arr)
#insertSort(arr)
#qSort(arr, 0, len(arr)-1)
#mergeSort(arr)
mergeSortX(arr)
#heapSort(arr)
# arr = countingSort(arr, 20)
print(arr)

#arr = ["ron", "mel", "dee", "pat", "bob"]
#radixSort(arr)