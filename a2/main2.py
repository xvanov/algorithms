# import time

# import sys 

class global_var():
    maxd = (1,0)
    path = [-1]
    depths = {}
    all_leaves = []

def parse_input():
    '''
    Reads input from BRUTE system stdin and converts it into lists accepted into algorithm
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
    '''
    with open(fin) as f:
        dim = int(f.readline())
        dat = {}
        for line in f.readlines():
            line = line.split(' ') # create list of chars
            line = list(map(int, line)) # convert each entry in line to int]
            
            try:
                tmp = dat[line[1]]
                tmp.append(line[0])
            except: 
                dat[line[1]] = [line[0]]
                
    return dim, dat

def read_output(fout):
    '''
    Reads output file (solution of input file) and converts it to int
    '''
    with open(fout) as f:
        res = f.readline()
        res = int(res)
    return res
    
    
    
##################################################################################################################
# resqs_tst = []

    # for node in primary_path:
    #     path = find_path((0,node))
    #     path_r2, path_s2, path_n2, path_t2, biggest_branch2, all_nodes2 = find_length(path)
    #     resqs_tst.append(path_s2 + path_n2 + path_t2)

    # path_tst_total =  max(resqs_tst)
    # print(path_tst_total)
##################################################################################################################



def solve(dim, dat):

    traversePostOrder(dat, 0, 0, left=1,deepest=0)
    path = global_var.path

    primary_path = []
    for node in reversed(path):
        primary_path.append(node[0])

    path_r1, path_s1, path_n1, path_t1, biggest_branch1, potential_secondary_nodes = find_length(primary_path)
    resqs = []
    for node in potential_secondary_nodes:
        path = find_path(node)
        path_r2, path_s2, path_n2, path_t2, biggest_branch2, all_nodes2 = find_length(path)
        resqs.append(path_r2 + path_s2 + node[0])

    path2_total =  max(resqs)
    
    path1_total = path_s1+path_n1+path_t1
    
    # print(path_r1, path_s1, path_n1, path_t1)
    # print('path1 total = ', path1_total, '\npath2 total = ', path2_total)
    
    res = max(path1_total, path2_total)

    return res


def find_length(path):
    resq = (0, 0)
    prev = (0, 0)
    biggest_branch = 0
    path_n, path_r, path_t, path_s = 0, 0, 0, 0 
    all_nodes = []
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
            
            all_nodes.append((node[4] - node[1], other))
            if total_d > prev[0] and total_d <= resq[0]:
                prev = (total_d, other)
                path_n = node[4] - node[1]
                path_t = other_d
                
            if total_d > resq[0]: # update length of 2 branches on the second longest branch
                biggest_branch = other
                resq = (total_d, other)
                path_r = node[4] - node[1]
                path_s = other_d
            
    # print(path_r, path_s, path_n, path_t)
    # path3_total = path_n + path_t + path_s # sum longest 3 branches
    return path_r, path_s, path_n, path_t, biggest_branch, all_nodes
    
    
def find_path(res):
    path = []
    node = res[1]
    res = res[0]
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
    
    
    
    
################################################################################################################
################################################################################################################




def traversePostOrder(dat, node, depth, left, deepest):

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
            global_var.all_leaves.append(node)

        global_var.depths[node] = (node,depth,leaf,left, deepest,deepest_l,deepest_r)


if __name__ == '__main__':
    # fn = sys.argv[1]
    
    # fin = './datapub/pub'+ fn + '.in'
    # fout = './datapub/pub'+ fn + '.out'
    
    # dim, dat = read_input(fin)
    
    # res = read_output(fout)
    # my_res = solve(dim, dat)
    
    
    # print('Actual result: {}'.format(res))
    # print('My result: {}'.format(my_res))
    
    ############### TURN IN BELOW THIS LINE #####################
    
    dim, dat = parse_input()
    # print(dim)
    # print(dat)
    my_res = solve(dim, dat)
    print(my_res)
    
    
    
    
    
    