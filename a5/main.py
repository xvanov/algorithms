# ALG - HW - 5
# Safe Giraffes Transport
# See ALG_HW_5.html for explanation of problem
# Kalin Ivanov
# 02.05.19

import time
import sys
import graph

class global_var():
    '''
    Set global variables
    '''
    f = None
    global_graph = None

def file_input(brute):
    if not brute:
        tmp = global_var.f.readline()
        tmp = tmp.strip().rstrip()
    else:
        tmp = input()
        tmp = tmp.strip().rstrip()
    return tmp

def read_input():
    '''
    Reads input from a file or from stdin and converts it into data accepted by the algorithm
    The input is a graph
    :param fin: input file
    :return meta: meta data of input, meta[0] = # of nodes, meta[1] = # of edges, meta[2] = start city, meta[3] = end city, meta[4] = # of triangles, meta[5] = # of squares
    :return es: dictionary where key is a parent and values are a list of children nodes
    :return triangles: list of nodes that are triangles
    :return squares: list of nodes that are squares
    Example:
    ## input ##
        datapub/pub01.in
        
    ## output ##
    meta: [10, 12, 4, 6, 2, 2]
    es: {0: [1, 3], 1: [0, 2, 5], 2: [1, 7], 7: [2, 6], 6: [7, 9, 5], 9: [6, 8], 8: [9, 4], 4: [8, 3, 5], 3: [4, 0], 5: [1, 4, 6]}
    triangles: [0, 2]
    squares: [8, 9] 6: [5, 7, 1, 11], 7: [6, 8, 2, 12], 8: [7, 9, 3, 13], 9: [8, 4, 14], 10: [11, 5], 11: [10, 12, 6], 12: [11, 13, 7], 13: [12, 14, 8], 14: [13, 9]}
    '''
    try:
        fn = sys.argv[1]
        fin = './datapub/pub'+ fn + '.in'
        global_var.f = open(fin)
        brute = 0
        raw_in = file_input
    except:
        brute = 1
        raw_in = file_input
        
    meta = [int(j) for j in raw_in(brute).split(' ')]
    
    global_var.global_graph = graph.Graph(meta[0])
    
    for i in range(meta[1]):
        line = [int(j) for j in raw_in(brute).split(' ')] # convert each entry in line to int
        global_var.global_graph.addedge(line[0], line[1])
       
    triangles = [int(j) for j in raw_in(brute).split(' ')]
    squares = [int(j) for j in raw_in(brute).split(' ')]
    meta.append(triangles.pop(0))
    meta.append(squares.pop(0))
    
    return meta, triangles, squares

def read_output():
    '''
    Reads output file (solution of input file) and converts it to int
    :return res: solution as an int
    '''
    fn = sys.argv[1]
    fout = './datapub/pub'+ fn + '.out'
    with open(fout) as f:
        res = f.readline()
        res = int(res)
    return res
    
    
def solve(meta, triangles, squares):
    sol = 99999999999999
    
    combined = triangles + squares
    
    t1 = time.time()
    dists2start = graph.BFS2(global_var.global_graph, meta[2], combined)
    t2 = time.time()
#    print('dists2start', t2-t1)
    

    t1 = time.time()
    dists2end = graph.BFS2(global_var.global_graph, meta[3], combined)
    t2 = time.time()
#    print('dists2end', t2-t1)
    
    
#    print(dists2start)
#    print(dists2end)
    
    for t in triangles:
        t2s = graph.BFS2(global_var.global_graph, t, squares)
        for s in squares:
            subtotal = min([dists2start[t] + dists2end[s], dists2start[s] + dists2end[t]])
            if subtotal < sol:
                total = t2s[s] + subtotal - 2
                if total < sol:
                    sol = total
    
    return sol    

if __name__ == '__main__':
    ################ TURN IN BELOW THIS LINE #####################
    t1 = time.time() # comment out
    meta, triangles, squares = read_input()
    t2 = time.time() # comment out
    
#    print('meta: {}'.format(meta))
#    print('es: {}'.format(es))
#    print('triangles: {}'.format(triangles))
#    print('squares: {}'.format(squares))
    
    t3 = time.time() # comment out
    my_res = solve(meta, triangles, squares)
    t4 = time.time() # comment out
    
    
    print(my_res)
    
    ############### COMMENT OUT BELOW THIS LINE ##################

#    res = read_output()
#    print('Actual result: {}'.format(res))

#    print('Time to read data: {}'.format(t2-t1))
#    print('Time to solve: {}'.format(t4-t3))
#    
    
