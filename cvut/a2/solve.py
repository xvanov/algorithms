# ALG - HW - 2
# River Basin Experiment
# See ALG_HW_2.html for explanation of problem
# Kalin Ivanov
# 04.04.19

import time

class global_var():
    '''
    Set global variables to be set in recursion function traversePostOrder and used throughout the algorithm
    :maxd: tuple containing max depth information (max depth, deepest node name)
    :path: straight path from deepest node to root list of tuples [(node,depth,leaf,left,deepest,deepest_l,deepest_r),...] 
    :depths: dictionary of node as key and node information tuple as value {node: (node,depth,leaf,left,deepest,deepest_l,deepest_r)}
    '''
    maxd = (1,0)
    path = [-1]
    depths = {}

def parse_input():
    '''
    Reads input from BRUTE system stdin and converts it into dictionary accepted into algorithm
    The input is a list of nodes in child-parent order that make up a binary tree
    :return dim: number of edges in tree
    :return dat: dictionary where key is a parent and values are a list of 1 or 2 children nodes
    Example:
    ## input ## pub01.in
        6
        5 3
        6 3
        3 1
        4 1
        1 0
        2 0
    ## output ##
    dim = 6
    dat = {0: [1, 2], 1: [3, 4], 3: [5, 6]}
    '''
    dim = int(input())
     
    dat = {}
    for i in range(dim):
        raw_dat = input()
        line = [int(j) for j in raw_dat.split()]
        try:
            tmp = dat[line[1]]
            tmp.append(line[0])
        except: 
            dat[line[1]] = [line[0]]
    return dim, dat

def read_input(fin):
    '''
    Reads input from a file and converts it into dictionary accepted into algorithm
    The input is a list of nodes in child-parent order that make up a binary tree
    :param fin: input file
    :return dim: number of edges in tree
    :return dat: dictionary where key is a parent and values are a list of 1 or 2 children nodes
    Example:
    ## input ## pub01.in
        6
        5 3
        6 3
        3 1
        4 1
        1 0
        2 0
    ## output ##
    dim = 6
    dat = {0: [1, 2], 1: [3, 4], 3: [5, 6]}
    '''
    with open(fin) as f:
        dim = int(f.readline())
        dat = {}
        for line in f.readlines():
            line = line.split(' ') # create list of chars
            line = list(map(int, line)) # convert each entry in line to int
            
            # if line[1] (parent) is a key in the dictionary append line[0] (child) to it
            # else create new entry in dictionary with line[1] (parent) as the key and line[0] (child) as the value
            try:
                tmp = dat[line[1]] 
                tmp.append(line[0])
            except: 
                dat[line[1]] = [line[0]]
                
    return dim, dat

def read_output(fout):
    '''
    Reads output file (solution of input file) and converts it to int
    :param fout: file containing single line with the solution to the input file
    :return res: solution as an int
    '''
    with open(fout) as f:
        res = f.readline()
        res = int(res)
    return res
    

def solve(dim, dat):
    '''
    Finds the greatest possible length of 3 unique paths (they don't go on top of each other)
    :param dim: number of edges in tree
    :param dat: dictionary where key is a parent and values are a list of 1 or 2 children nodes
    :return resn: max length of 3 unique paths combined
    '''
    
    ## PART 1 ##
    ##### Recursively traverse tree and find depths of nodes #####
    t1 = time.time()
    # traversePostOrder(dat, node, depth, left,deepest) = Recursive function, traverses tree in post-order and sets global variables:
    # global_var.maxd = (max depth, node name)
    # global_var.path = [deepest node,...,root]
    # global_var.depths = {} dictionary where each key is a node
    traversePostOrder(dat, 0, 0, left=1,deepest=0)
    t2 = time.time()
    print( "recurse time {}".format(t2-t1))
    
    
    ## PART 2 ##
    ##### Find 3 longest branches from longest path #####
    t1 = time.time()
    # path_r = length of deepest BRANCH (not longest PATH) (from depest node to where longest PATH and second longest BRANCH meet)
    # path_s = length of second longest BRANCH
    # path_n = length of deepest node to third longest BRANCH
    # path_t = length of third longest BRANCH
    path_r, path_s, path_t, path_n= 0, 0, 0, 0
    path = global_var.path # longest PATH
    node = global_var.maxd
    res = (0,0) # longest branch 
    prev = (0,0)
    for i in reversed(range(len(path))): # go from root to deepest node
        node = path[i]
        try: # if node has 0 children continue
            children = dat[node[0]]
        except:
            continue
        
        if len(children) != 2: # if node has 1 child continue
            continue
        else: # if node has 2 children 
            if path[i-1][0] == children[0]: # choose other to be child NOT on path to depest node
                other = children[1]
            else:
                other = children[0]
                
            other_d = global_var.depths[other][4] - node[1] # calculate length from deepest possible to current branching node depth
            total_d = other_d + node[4] - node[1] # calculate length from deepest possible to branching node deepest possible
            
            if total_d < res[0] and total_d > prev[0]: # update second longest path
                prev = (total_d, other)
                path_n = node[4] - node[1]
                path_t = other_d
            
            if total_d > res[0]: # update longest path
                path_r = node[4] - node[1]
                path_s = other_d
                res = (total_d, other)
    
    path3_total = path_n + path_t + path_s # sum longest 3 branches
    
    
    ## PART 3 ##
    ##### Find path length of (second longest branch with branch) + (path_r = longest branch) #####
    path2 = find_path(res) # find second longest path
    
    resn = path3_total # set result
    resq = find_length(path2) # length of 2 branches on the second longest branch

    path2_total = resq+path_r  # path2_total = (second longest branch with branch) + (longest branch)

    if resq == 0: # if (second longest branch with branch) = 0 then only 3 branch path is possible
        resn = path3_total
    else:
        resn = max(path2_total, path3_total)
    
    t2 = time.time()
    print( "iterate time {}".format(t2-t1))
    return resn
    

def find_length(path):
    resq = 0
    for i in range(len(path)):
        
        node = path[i]
        node = global_var.depths[node]
        try: # if node has 0 children continue
            children = dat[node[0]]
        except:
            continue
        if len(children) != 2: # if node has 1 child continue
            continue
        else: # if node has 2 children
            if path[i+1] == children[0]: # choose other to be child NOT on path to depest node
                other = children[1]
            else:
                other = children[0]
                
            other_d = global_var.depths[other][4] - node[1] # calculate length from deepest possible to current branching node depth
            total_d = other_d + node[4] - node[1] # calculate length from deepest possible to branching node deepest possible
            
            if total_d > resq: # update length of 2 branches on the second longest branch
                resq = total_d
    return resq
    
    
def find_path(res):
    '''
    Finds path from arbitrary node its deepest child
    :param res: tuple where res[1] = node : res=(total_d, other)
    :return path: list path from node to its deepest child 
    '''
    path = []
    node = res[1]
    cond = True
    while cond:
        try: 
            path.append(node)
            children = dat[node]

            if global_var.depths[node][5] >= global_var.depths[node][6]:
                node = children[0]
            else:
                node = children[1]
            cond = True
        except:
            cond = False
    return path

def traversePostOrder(dat, node, depth, left, deepest):
    '''
    Recursive function which traverses the tree once and populates the global variables
    :param dat: dictionary where key is a parent and values are a list of 1 or 2 children nodes
    :param node: current node
    :param depth: current depth
    :param left: right node = 0, left node = 1
    :param deepest: the deepest child of node
    '''
    try: # if node is not a leaf
        tmp = dat[node]
        depth +=1
        leaf = 0
        

        traversePostOrder(dat,tmp[0],depth,left=1,deepest=deepest) # recurse left child
        deepest_l = global_var.depths[tmp[0]][4]
        deepest_r = 0

        if len(tmp) > 1:
            traversePostOrder(dat,tmp[1], depth,left=0,deepest=deepest) # recurse right child
            deepest_r = global_var.depths[tmp[1]][4]
            if global_var.path[-1:][0][0] == tmp[1]:
                deepest = max([deepest_l,deepest_r])
                global_var.path.append((node,depth,leaf,left,deepest,deepest_l,deepest_r))
       
        deepest = max([deepest_l,deepest_r])
        global_var.depths[node] = (node,depth,leaf,left,deepest,deepest_l,deepest_r)

        if global_var.path[-1:][0][0] == tmp[0]:
            global_var.path.append((node,depth,leaf,left,deepest,deepest_l,deepest_r))
            
    except: # reached leaf
        depth += 1
        leaf = 1
        deepest_l, deepest_r = depth,depth
        deepest = depth
        if depth > global_var.maxd[0]:
            global_var.maxd = (depth,node)
            global_var.path = [(node,depth,leaf,left, deepest,deepest_l,deepest_r)]

        global_var.depths[node] = (node,depth,leaf,left, deepest,deepest_l,deepest_r)


if __name__ == '__main__':
    fn = '01'
    fin = './datapub/pub'+ fn + '.in'
    fout = './datapub/pub'+ fn + '.out'
    
    dim, dat = read_input(fin)
    # print(dim)
    # print(dat)
    res = read_output(fout)
    my_res = solve(dim, dat)
    
    
    print('Actual result: {}'.format(res))
    print('My result: {}'.format(my_res))
    
    ############### TURN IN BELOW THIS LINE #####################
    
    # dim, dat = parse_input()
    # # print(dim)
    # # print(dat)
    # my_res = solve(dim, dat)
    # print(my_res)
    
    
    
    
    
    