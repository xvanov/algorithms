# ALG - HW - 4
# Loosely Connected Isolated Nodes
# See ALG_HW_4.html for explanation of problem
# Kalin Ivanov
# 14.04.19

import time
import sys

class global_var():
    '''
    Set global variables
    '''
    f = None

def file_input():
    return global_var.f.readline()

def read_input():
    '''
    Reads input from a file or from stdin and converts it into data accepted by the algorithm
    The input is a colored graph
    :param fin: input file
    :return meta: meta data of input, meta[0] = # of nodes, meta[1] = # of edges, meta[0] = # of colors
    :return cs: list where index is node and the value is the color
    :return es: dictionary where key is a parent and values are a list of children nodes
    Example:
    ## input ##
        datapub/pub01.in
        
    ## output ##
    meta = [15, 22, 3]
    cs = [1, 2, 0, 1, 1, 0, 2, 1, 2, 1, 0, 1, 0, 1, 0]
    es = {0: [1, 5], 1: [0, 2, 6], 2: [1, 3, 7], 3: [2, 4, 8], 4: [3, 9], 5: [6, 0, 10], 6: [5, 7, 1, 11], 7: [6, 8, 2, 12], 8: [7, 9, 3, 13], 9: [8, 4, 14], 10: [11, 5], 11: [10, 12, 6], 12: [11, 13, 7], 13: [12, 14, 8], 14: [13, 9]}
    '''
    try:
        fn = sys.argv[1]
        fin = './datapub/pub'+ fn + '.in'
        global_var.f = open(fin)
        raw_in = file_input
    except:
        raw_in = input
    
    meta = [int(j) for j in raw_in().split(' ')]
    cs = [int(j) for j in raw_in().split(' ')]
    es = {}
    
    for i in range(meta[1]):
        line = [int(j) for j in raw_in().split(' ')] # convert each entry in line to int
        
        try:
            es[line[0]].append(line[1])
        except: 
            es[line[0]] = [line[1]]
        try:
            es[line[1]].append(line[0])
        except: 
            es[line[1]] = [line[0]]
            
    return meta, cs, es

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
    
    
def solve(meta, cs, es):
    sol = 0
    all_isolated = [0]*meta[0]
    all_gcs = {}
    
    for node in range(meta[0]):
        node_c = cs[node]
        isolated = True
        tmp = []
        for child in es[node]:
            if node_c == cs[child]:
                isolated = False
            tmp.append(es[child])
    
        if isolated:
            all_isolated[node] = 1
            all_gcs[node] = tmp
    
    
    for node in all_gcs:
        tmp = []
        for group in all_gcs[node]:
            tmp.extend(group)
        tmp = list(set(tmp))
        tmp.remove(node)
        all_gcs[node] = tmp
            
    for node in all_gcs:
        for gc in all_gcs[node]:
            if gc < node:
                continue
            if all_isolated[gc]:
                sol += 1
    return sol


if __name__ == '__main__':
    ################ TURN IN BELOW THIS LINE ###################
    # t1 = time.time()
    meta, cs, es = read_input()
    # t2 = time.time()
    
    # print(meta)
    # print(cs)
    # print(es)

    # t3 = time.time()
    my_res = solve(meta, cs, es)
    # t4 = time.time()
    
    
    print(my_res)
    
    ############### COMMENT OUT BELOW THIS LINE ##################
    
    # print('\n')
    # res = read_output()
    # print('Actual result: {}'.format(res))
    
    # print('meta: {}'.format(meta))
    # print('cs: {}'.format(cs))
    # print('es: {}'.format(es))
    
    # print('Time to read data: {}'.format(t2-t1))
    # print('Time to solve: {}'.format(t4-t3))
    
    
    
    