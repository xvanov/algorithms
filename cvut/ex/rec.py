# ---------------------------------------------------------------------
#    M I N
# ---------------------------------------------------------------------

# no recursion
def myMin0( arr ):
    min = arr[0]
    for i in range( 1, len(arr) ):
        if arr[i] < min: min = arr[i]
    return min


# recursion - one call
def myMin1( arr, iFrom ):
    # stop recursion? just a single element?
    if iFrom == len(arr) - 1: return arr[iFrom]

    # more elements
    rightMin = myMin1( arr, iFrom+1 )
    if arr[iFrom] < rightMin: return arr[iFrom]
    else:                     return rightMin


# recursion - two calls
def myMin2( arr, iFrom, iTo ):
     # stop recursion? just a single element?
    if iFrom == iTo: return arr[iFrom]

    # more elements
    iMid = (iFrom + iTo) // 2  # index of middle element
    # recursive calls
    leftMin  = myMin2( arr, iFrom, iMid )
    rightMin = myMin2( arr, iMid+1, iTo )
    # compute return value
    if   leftMin < rightMin: return leftMin
    else:                    return rightMin

# ---------------------------------------------------------------------
#    O D D
# ---------------------------------------------------------------------

# no recursion
def noOfOdd0( arr ):
    noOfOdd = 0
    for i in range( 0, len(arr) ):
        if arr[i] % 2 == 1: noOfOdd += 1
    return noOfOdd

# no recursion
def noOfOdd0a( arr ):
    noOfOdd = 0
    for i in range( 0, len(arr) ): noOfOdd += (arr[i] % 2)
    return noOfOdd


# recursion - one call
def noOfOdd1( arr, iFrom ):
    # stop recursion? just a single element?
    if iFrom == len(arr): return 0

    # more elements
    rightNoOfOdd = noOfOdd1( arr, iFrom + 1  )
    if arr[iFrom] % 2 == 1: return 1 + rightNoOfOdd
    else:                   return 0 + rightNoOfOdd

# recursion - one call
def noOfOdd1a( arr, iFrom ):
    if iFrom == len(arr): return 0
    return arr[iFrom] % 2 + noOfOdd1a( arr, iFrom + 1 )


# recursion - two calls
def noOfOdd2( arr, iFrom, iTo ):
     # stop recursion? just a single element?
    if iFrom == iTo:
         if arr[iFrom] % 2 == 1: return 1
         else:                   return 0

    # more elements
    iMid = (iFrom + iTo) // 2  # index of middle element
    # recursive calls
    leftNoOfOdd  = noOfOdd2( arr, iFrom, iMid )
    rightNoOfOdd = noOfOdd2( arr, iMid+1, iTo )
    # compute return value
    return leftNoOfOdd + rightNoOfOdd

# recursion - two calls
def noOfOdd2a( arr, iFrom, iTo ):
    if iFrom == iTo: return arr[iFrom] % 2
    iMid = (iFrom + iTo) // 2
    return noOfOdd2a( arr, iFrom, iMid ) + noOfOdd2a( arr, iMid+1, iTo )


# recursion - five calls
def noOfOdd5a( arr, iFrom, iTo ):
    if iFrom > iTo: return 0 # be careful
    if iFrom == iTo: return arr[iFrom] % 2

    iFifth1 = iFrom + 1*(iTo-iFrom) // 5
    iFifth2 = iFrom + 2*(iTo-iFrom) // 5
    iFifth3 = iFrom + 3*(iTo-iFrom) // 5
    iFifth4 = iFrom + 4*(iTo-iFrom) // 5

    return   noOfOdd5a( arr, iFrom, iFifth1 ) \
           + noOfOdd5a( arr, iFifth1+1, iFifth2 ) \
           + noOfOdd5a( arr, iFifth2+1, iFifth3 ) \
           + noOfOdd5a( arr, iFifth3+1, iFifth4 ) \
           + noOfOdd5a( arr, iFifth4+1, iTo )

# ---------------------------------------------------------------------
#    M A I N
# ---------------------------------------------------------------------

arr = [8, 13, 7, 15, 4, 6, 10, 5, 22, 11,]

print( arr )
print()
print( myMin0( arr ))
print( myMin1( arr, 0 ))
print( myMin2( arr, 0, len(arr)-1 ))
print()

print( noOfOdd0 ( arr ))
print( noOfOdd0a( arr ))
print( noOfOdd1 ( arr, 0 ))
print( noOfOdd1a( arr, 0 ))
print( noOfOdd2 ( arr, 0, len(arr)-1 ))
print( noOfOdd2a( arr, 0, len(arr)-1 ))
print( noOfOdd5a( arr, 0, len(arr)-1 ))


