# ALG - HW - 6
# Key Servers Statistics
# See ALG_HW_6.html for explanation of problem
# Kalin Ivanov
# 13.05.19

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
    
    leaves = []
    
    for i in range(meta[0]):
        line = [int(j) for j in raw_in(brute).split(' ')]
        global_var.global_graph.addedge(line[0], line[1], line[2])
        
    for node in global_var.global_graph.nodes:
        if len(node.neighbours) == 1:
            leaves.append(node.id)

    key_servers = [int(j) for j in raw_in(brute).split(' ')]
    
    return meta, key_servers, leaves

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
    
    
def solve(meta, key_servers, leaves):
    sol = 99999999999999
    start = min(key_servers)
#    key_servers = key_servers.remove(start)
    key_servers.sort()
    bool_servers = [False]*meta[0]
    for i in key_servers:
        bool_servers[i] = True
    tmp_key_dists = {}
    tmp_key_dists[start] = 0
    v = 999
    key_dists = {k:v for k in key_servers}
    key_dists[start] = 0
    keys = key_servers.copy()  
    i = 0 
    
    visited = []
    trees = []
    visited_keys = []
    last = []
    
    for leaf in leaves:
        current = global_var.global_graph.nodes[leaf]
        dist = 0
        count_bool = 0
        while len(current.neighbours) < 3:
#            print(current.id)
            if current.id in key_servers:
                count_bool = 1
                visited_keys.append(current.id)
                
            visited.append(current.id)
            neighbours = global_var.global_graph.nodes[current.id].neighbours
            for n in neighbours:
                if n[0].id not in visited:
                    current = global_var.global_graph.nodes[n[0].id]
                    if count_bool:
                        dist += n[1]
                    if len(current.neighbours) >= 3:
                        last.append(n[0].id)
                    
        trees.append(dist)
    
    to_visit = [x for x in list(range(0, meta[0])) if x not in visited] 
#    print(to_visit)
    
#    to_visit = not_visited + last
#    to_visit = list(dict.fromkeys(to_visit))
##    print(to_visit)
    current = to_visit[0]
    dist = 0
##    print(to_visit)
    max_edge = 0
    
#    while len(to_visit) > 0:
#        neighbours = global_var.global_graph.nodes[current].neighbours
#        visited.append(current)
#        if current in to_visit:
#            to_visit.remove(current)

#        for n in neighbours:
#            if n[0].id not in visited:
#                current = global_var.global_graph.nodes[n[0].id].id
#                dist += n[1]

#                if n[1] > max_edge:
#                    max_edge = n[1]
                
#                    

#    print(max_edge)
    print(dist)
#    print(trees)
    print(sum(trees)*2 + dist)
    return sol    

if __name__ == '__main__':
    ################ TURN IN BELOW THIS LINE #####################
    t1 = time.time() # comment out
    meta, key_servers, leaves = read_input()
    t2 = time.time() # comment out
    
#    print('meta: {}'.format(meta))
#    print('key_servers: {}'.format(key_servers))
#    global_var.global_graph.print_graph()
    
    t3 = time.time() # comment out
    my_res = solve(meta, key_servers, leaves)
    t4 = time.time() # comment out
#    
    
#    print(my_res)
    
    ############### COMMENT OUT BELOW THIS LINE ##################

    res = read_output()
    print('Actual result: {}'.format(res))

    print('Time to read data: {}'.format(t2-t1))
    print('Time to solve: {}'.format(t4-t3))
    
    
