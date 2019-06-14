# ALG - HW - 1
# Collecting samples
# See ALG_HW_1.html for explanation of problem
# Kalin Ivanov
# 21.03.19

import timeit


def parse_input():
    '''
    Reads input from BRUTE system stdin and converts it into lists accepted into algorithm
    return dims = dimensions (x, y)
    dat = dimensions of field with with toxic squares counted as -1
    new_dat = dimensions of field with toxic squares counted as -2 
    Example input
    4 4
    1 0 1 2
    2 0 2 1
    1 2 1 0
    0 1 2 0
    Example outputs:
    dims = [4, 4]
    dat = [[1, 0, 1, -1], [-1, 0, -1, 1], [1, -1, 1, 0], [0, 1, -1, 0]]
    new_dat = [[1, 0, 1, -2], [-2, 0, -2, 1], [1, -2, 1, 0], [0, 1, -2, 0]]
    '''
    dims = list(map(int, input().split()))
     
    dat = []
    for i in range(dims[0]):
        raw_dat = input()
        line = [int(j) for j in raw_dat.split()]
        for i in range(len(line)):
            if line[i] == 2:
                line[i] = (0,1)
            elif line[i] == 1:
                 line[i] = (1,0)
            else:
                line[i] = (0,0)
        dat.append(line)
    
    return dims, dat

def read_input(fin):
    '''
    Reads input file and converts it to lists accepted into algorithm
    param fin = input file 
    return dims = dimensions (x, y)
    dat = dimensions of field with with toxic squares counted as -1
    new_dat = dimensions of field with toxic squares counted as -2 
    Example contents of fin:
    4 4
    1 0 1 2
    2 0 2 1
    1 2 1 0
    0 1 2 0
    Example outputs:
    dims = [4, 4]
    dat = [[1, 0, 1, -1], [-1, 0, -1, 1], [1, -1, 1, 0], [0, 1, -1, 0]]
    new_dat = [[1, 0, 1, -2], [-2, 0, -2, 1], [1, -2, 1, 0], [0, 1, -2, 0]]
    '''
    with open(fin) as f:
        # first line of file
        dims = f.readline()
        dims = dims.split(' ')
        dims = list(map(int, dims))
        
        # set up to lists dat will have -2 for 2 (toxic square)
        #             new_dat will have -1 for 2 (toxic square)
        dat = []
        for line in f.readlines():
            line = line.split(' ') # create list of chars
            line = list(map(int, line)) # convert each entry in line to int
            for i in range(len(line)):
                if line[i] == 2:
                    line[i] = (0,1)
                elif line[i] == 1:
                    line[i] = (1,0)
                else:
                    line[i] = (0,0)
            dat.append(line)
    return dims, dat

def read_output(fout):
    '''
    Reads output file (solution of input file) and converts it to int
    param fout = output file 
    return res = result
    Example contents of fout (solution of example of fin):
    2
    Example outputs:
    res = 2
    '''
    with open(fout) as f:
        res = f.readline()
        res = int(res)
    return res
    
# def brute(dims, dat, new_dat):
#     '''
#     Solves collecting samples by brute force
#     param dims = x, y dimensions of field
#     param dat = field with -1 for toxic quadrants
#     param new_dat = field with -2 for toxic quadrants
#     return res = greatest number of minerals collected
#     '''
#     small = min(dims)
#     res = 0
#     for i in range(1,small):
#         for x in range(len(dat)-1): # don't go to last row and last column
#             for y in range(len(dat[0])-1): #
#                 tmp = square(dat,x,y,i)
#                 trk = square(new_dat,x,y,i)
#                 if trk < 0: # tests 2*minerals < toxics
#                     continue
#                 score = 2*tmp - trk # 2*(M-T) - (M-2*T) = M
#                 if score > res:
#                     res = score
#     return res
    
# def square(dat,x,y,sz):
#     '''
#     Goes in square pattern of specified size
#     param dat = field with toxic and mineral quadrants
#     param x = x coordinate
#     param y = y coordinate
#     sz = size of square pattern
#     return res = sum of values in square pattern 
#     '''
#     res = dat[x][y] # add first corner to result
#     try: 
#         res += dat[x+sz][y+sz] + dat[x+sz][y] + dat[x][y+sz] # add remaining corners to result
#         for i in range(1,sz):
#             res += dat[x][y+i] + dat[x+i][y] + dat[x+sz][y+i] + dat[x+i][y+sz] # add edges to result
#     except:
#         res = -1
#     return res
    
    
    
    
############################## NOT BRUTE FORCE ###################
    
# def not_brute(dims, dat):
#     small = min(dims)
#     all_row = dat
#     all_col = dat
#     res = 0
#     for i in range(1,small+1):
#         # print(all_row)
#         # print(all_col)
#         rows = []
#         cols = []
#         for x in range(dims[0]):
#             row = []
#             col = []
#             for y in range(dims[1]):
#                 if y+i < dims[1]:
#                     row.append((dat[x][y+i][0] + all_row[x][y][0], dat[x][y+i][1] + all_row[x][y][1]))
                    
#                 if x+i < dims[0]:
#                     col.append((dat[x+i][y][0] + all_col[x][y][0], dat[x+i][y][1] + all_col[x][y][1]))
                
#                 if i > 1:
#                     try:
#                         sub = (dat[x][y][0] + dat[x+i-1][y+i-1][0] + dat[x+i-1][y][0] + dat[x][y+i-1][0], dat[x][y][1] + dat[x+i-1][y+i-1][1] + dat[x+i-1][y][1] + dat[x][y+i-1][1])
#                         tmp = (all_row[x][y][0] + all_col[x][y][0] + all_row[x+i-1][y][0] + all_col[x][y+i-1][0] - sub[0], all_row[x][y][1] + all_col[x][y][1] + all_row[x+i-1][y][1] + all_col[x][y+i-1][1] - sub[1])
#                     except:
#                         tmp = (0,0)
                        
#                     if tmp[0] >= 2*tmp[1]: #  tests 2*minerals < toxics
#                         if tmp[0] > res:
#                             res = tmp[0]
#                             # print(res, x, y, i, tmp, sub, all_row[x][y], all_row[x+i-1][y], all_col[x][y], all_col[x][y+i-1])
   
#             rows.append(row)
#             cols.append(col)
            
#         all_row = rows        
#         all_col = cols
    
#     return res
    
#############################################################################################

def not_brute2(dims, dat):
    small = min(dims)
    all_row = []
    all_col = []
    all_row.append(dat)
    all_col.append(dat)
    res = 0
    
    max_rows = [(0,0)]
    max_cols = [(0,0)]
    for i in range(1,small+1):
        cols = []
        rows = []
        col_max = 0
        row_max = 0
        pcmax = 0
        prmax = 0
        
        for x in range(dims[0]-i):
            col = []
            for y in range(dims[1]):
                tmp = (dat[x+i][y][0] + all_col[i-1][x][y][0], dat[x+i][y][1] + all_col[i-1][x][y][1])
                col.append(tmp)
                prev_cmax = col_max
                if tmp[0] > prev_cmax:
                    col_max = tmp[0]
                    pcmax = prev_cmax
            cols.append(col)
            
        for x in range(dims[0]):
            row = []
            for y in range(dims[1]-i):
                tmp = (dat[x][y+i][0] + all_row[i-1][x][y][0], dat[x][y+i][1] + all_row[i-1][x][y][1])
                row.append(tmp)
                prev_max = row_max
                if tmp[0] > prev_max:
                    row_max = tmp[0]
                    prmax = prev_max
            rows.append(row)
            
        all_row.append(rows)        
        all_col.append(cols)
    
        if col_max > max_cols[i-1][0]:
            max_cols.append((col_max,pcmax)) 
        else:
            max_cols.append(max_cols[i-1]) 
            
        if row_max > max_rows[i-1][0]:
            max_rows.append((row_max, prmax)) 
        else:
            max_rows.append(max_rows[i-1]) 
            
    for i in reversed(range(1,small+1)):

        if res > max_cols[i][0] + max_cols[i][1] + max_rows[i][0] + max_rows[i][1]:
            print(max_cols[i][0], max_cols[i][1], max_rows[i][0], max_rows[i][1]) #max_row + max_col:  #max_row + max_col:
            break
        else:
            for x in range(dims[0]-i):
                for y in range(dims[1]-i):   
                    sub = (dat[x][y][0] + dat[x+i][y+i][0] + dat[x+i][y][0] + dat[x][y+i][0], dat[x][y][1] + dat[x+i][y+i][1] + dat[x+i][y][1] + dat[x][y+i][1])
                    tmp = (all_row[i][x][y][0] + all_col[i][x][y][0] + all_row[i][x+i][y][0] + all_col[i][x][y+i][0] - sub[0], all_row[i][x][y][1] + all_col[i][x][y][1] + all_row[i][x+i][y][1] + all_col[i][x][y+i][1] - sub[1])

                    if tmp[0] >= 2*tmp[1]: #  tests 2*minerals < toxics
                        if tmp[0] > res:
                            res = tmp[0]

    return res
    
################################################################################

def not_brute3(dims, dat):
    small = min(dims)
    rows = []
    cols = []
    res = 0
    
    max_rows = [(0,0)]
    max_cols = [(0,0)]
    
    cols = [dat[0]]
    for x in range(dims[0]):
        row = [dat[x][0]] 
        col = []
        for y in range(dims[1]):
            if y+1<dims[1]:
                row.append((row[y][0] + dat[x][y+1][0], row[y][1] + dat[x][y+1][1]))
            if x+1<dims[0]:
                col.append((cols[x][y][0] + dat[x+1][y][0], cols[x][y][1] + dat[x+1][y][1]))
        rows.append(row)
        if x+1<dims[0]:
            cols.append(col)
    
    # print(rows)
    # print(cols)
    # print(small)
    for i in range(small,0,-1):
        for x in range(dims[0]-i):
            for y in range(dims[1]-i):
                if res > 4*i:
                    break
                else:
                    # print(i,x,y)
                    if y == 0:
                        top = (rows[x][y+i][0],rows[x][y+i][1])
                        bottom = (rows[x+i][y+i][0],rows[x+i][y+i][1])
                    else:
                        top = (rows[x][y+i][0] - rows[x][y-1][0],rows[x][y+i][1] - rows[x][y-1][1])
                        bottom = (rows[x+i][y+i][0] - rows[x+i][y-1][0],rows[x+i][y+i][1] - rows[x+i][y-1][1])
                    left = (cols[x+i-1][y][0] - cols[x][y][0],cols[x+i-1][y][1] - cols[x][y][1])
                    right = (cols[x+i-1][y+i][0] - cols[x][y+i][0],cols[x+i-1][y+i][1] - cols[x][y+i][1])
                    square = (top[0]+bottom[0]+left[0]+right[0],top[1]+bottom[1]+left[1]+right[1])
                    # print(i, square, top, bottom, left, right)
                    if square[0] >= 2*square[1]: #  tests 2*minerals < toxics
                        if square[0] > res:
                            res = square[0]
        
    return res

################################################################################
#################################################################################

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
    
if __name__ == '__main__':
    '''
    Run algorithm with files in ./datapub directory
    '''
    
    fn = '01'
    
    fin = './datapub/pub'+fn+'.in'
    dims, dat = read_input(fin)
    print(dims)
    print(dat)

    fout = './datapub/pub'+fn+'.out'
    res = read_output(fout)
    
    my_res = not_brute3(dims, dat)
    wrapped = wrapper(not_brute3, dims, dat)
    t = timeit.timeit(wrapped, number=1)
    print('My result: {} with time {}'.format(my_res, t))
    print('Actual result: {}'.format(res))

    ### UNCOMMENT AND SUBMIT BELOW THIS LINE ###
    '''
    Run algorithm with input from BRUTE system
    '''
    # dims, dat = parse_input()
    # # print(dims)
    # # print(dat)
    # res = not_brute2(dims, dat)
    # print(res)
