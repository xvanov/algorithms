# ALG - HW - 1
# Collecting samples
# Kalin Ivanov
# 29.03.19

def parse_input():
    '''
    Reads input from BRUTE system stdin and converts it into lists accepted into algorithm
    :return dims: dimensions (x, y)
    :return dat: field where each square is a tuple (i,j) where i=1 indicates mineral and j=1 indicates toxic
    Example:
    input:
    4 4
    1 0 1 2
    2 0 2 1
    1 2 1 0
    0 1 2 0
    output:
    dims = [4, 4]
    dat = [[(1, 0), (0, 0), (1, 0), (0, 1)], 
           [(0, 1), (0, 0), (0, 1), (1, 0)], 
           [(1, 0), (0, 1), (1, 0), (0, 0)], 
           [(0, 0), (1, 0), (0, 1), (0, 0)]]
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
    
    for i in range(small,0,-1):
        for x in range(dims[0]-i):
            for y in range(dims[1]-i):
                if res > 4*i:
                    break
                else:
                    if y == 0:
                        top = (rows[x][y+i][0],rows[x][y+i][1])
                        bottom = (rows[x+i][y+i][0],rows[x+i][y+i][1])
                    else:
                        top = (rows[x][y+i][0] - rows[x][y-1][0],rows[x][y+i][1] - rows[x][y-1][1])
                        bottom = (rows[x+i][y+i][0] - rows[x+i][y-1][0],rows[x+i][y+i][1] - rows[x+i][y-1][1])
                    left = (cols[x+i-1][y][0] - cols[x][y][0],cols[x+i-1][y][1] - cols[x][y][1])
                    right = (cols[x+i-1][y+i][0] - cols[x][y+i][0],cols[x+i-1][y+i][1] - cols[x][y+i][1])
                    square = (top[0]+bottom[0]+left[0]+right[0],top[1]+bottom[1]+left[1]+right[1])
                    if square[0] >= 2*square[1]: #  tests 2*minerals < toxics
                        if square[0] > res:
                            res = square[0]
        
    return res

if __name__ == '__main__':
    '''
    Run algorithm with input from BRUTE system
    '''
    dims, dat = parse_input()
    res = not_brute3(dims, dat)
    print(res)
