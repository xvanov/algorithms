# ALG - HW - 6
# Key Servers Statistics
# See ALG_HW_6.html for explanation of problem
# Kalin Ivanov
# 14.06.19

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
    
#    global_var.global_graph = graph.Graph(meta[0])
    
    leaves = []
    nodes = {}
    
    for i in range(meta[0]):
        line = [int(j) for j in raw_in(brute).split(' ')]
#        global_var.global_graph.addedge(line[0], line[1], line[2])
        try:
            nodes[line[0]].append((line[1], line[2]))
        except:
            nodes[line[0]] = [(line[1], line[2])]
        try:
            nodes[line[1]].append((line[0], line[2]))
        except:
            nodes[line[1]] = [(line[0], line[2])]
    
    for node in nodes:
        if len(nodes[node]) == 1:
            leaves.append(node)
#    for node in global_var.global_graph.nodes:
#        if len(node.neighbours) == 1:
#            leaves.append(node.id)

    key_s = [int(j) for j in raw_in(brute).split(' ')]
    key_s = sorted(key_s)
    key_ss = key_s.copy()
    start = key_s[0]
    key_servers = {}
    for i in range(meta[0]):
        if len(key_s) > 0:
            if i == key_s[0]:
                key_servers[i] = 1;
                key_s.pop(0)
            else:
                key_servers[i] = 0;
        else:
            key_servers[i] = 0;

    return meta, nodes, key_servers, leaves, start, key_ss

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
    
def solve2(meta, nodes, key_servers, leaves, start, key_ss):
    sol = 99999999999999
    trees = []
    branched = 0
    special = 0
    branchings = []
    tree_keys = 0
    start_branch = 0
    total_start_branch = 0
    keys = list(range(0,meta[0]))
    branchings_parents = {key: 0 for key in keys}
    
    for leaf in leaves:
        current = leaf
        path = []
        bool_s = 0
        dist = 0
        local_branched = 0
        
        while len(nodes[current]) < 3:
            parent = current
            if key_servers[current]:
                tree_keys += 1
                key_servers[current] = 0
                bool_s = 1
                if current == start:
                    local_branched = 1
                    branched = 1
                    total_start_branch = dist
                
            path.append(current)
            if len(path) >= 2:
                child1 = nodes[current][0]
                child2 = nodes[current][1]
                if path[-2] == child1[0]:
                    current = child2
                else:
                    current = child1
            else:
                current = nodes[current][0]
            
            if bool_s:
                dist += current[1]
                if local_branched:
                    start_branch += current[1]
                    branching_parent = parent
                    branching = current[0]
                    total_start_branch += current[1]
            lasts = current[0]
            
            current = current[0]

        if key_servers[lasts] == 1:
            tree_keys -= 1
        key_servers[lasts] = 1
        trees.append(dist)
        branchings.append(lasts)
        branchings_parents[parent] = 1
    

    K = meta[1]
    N = K + tree_keys + len(branchings)
    
    path = []
    if branched:
        current = branching
        path.append(parent)
        child1 = nodes[current][0]
        child2 = nodes[current][1]
        child3 = nodes[current][2]
        children = [child1, child2, child3]
        for c in children:
            if branchings_parents[c[0]]:
                children.remove(c)
    else:
        current = start
        child1 = nodes[current][0]
        child2 = nodes[current][1]
        children = [child1, child2]

    
    dist = children[0][1]
    exit = 0
    path = [current, children[0][0]]
    while exit == 0:
        last = path[-1]
        currents = nodes[last]
        if last == path[0]:
            exit = 1
            break
        
        print(currents)
        pot1 = currents[0][0]
        pot2 = currents[1][0]
        
        if pot1 != path[-2] and not  branchings_parents[pot1]:
            path.append(pot1)
            dist += currents[0][1]
        elif pot2 != path[-2] and not  branchings_parents[pot2]:
            path.append(pot2)
            dist += currents[1][1]
        else:
            pot3 = currents[2][0]
            path.append(pot3)
            dist += currents[2][1]
           
            
    sol = sum(trees)*2 + dist
    return sol 
    
    
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
        prev = leaf
        tree =[leaf]
        while len(current.neighbours) < 3:
#            print(current.id)
            if current.id in key_servers:
                count_bool = 1
                visited_keys.append(current.id)
            tree.append(current.id)
            prev = tree.pop(0)
#            print(prev)
            visited.append(current.id)
            neighbours = global_var.global_graph.nodes[current.id].neighbours
            for n in neighbours:
#                print(n[0].id)
                if n[0].id != prev:
#                if n[0].id not in visited:
                    current = global_var.global_graph.nodes[n[0].id]
                    if count_bool:
                        dist += n[1]
                    if len(current.neighbours) >= 3:
                        last.append(n[0].id)
                    break
            
                    
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
    meta, nodes, key_servers, leaves, start, key_ss = read_input()
    t2 = time.time() # comment out
    
#    print('meta: {}'.format(meta))
#    print('nodes: {}'.format(nodes))
#    print('key_servers: {}'.format(key_servers))
#    print('leaves: {}'.format(leaves))
#    global_var.global_graph.print_graph()
    
    t3 = time.time() # comment out
#    my_res = solve(meta, key_servers, leaves)
    my_res = solve2(meta, nodes, key_servers, leaves, start, key_ss)
    t4 = time.time() # comment out
#    
    
    print(my_res)
    
    ############### COMMENT OUT BELOW THIS LINE ##################

    res = read_output()
    print('Actual result: {}'.format(res))

    print('Time to read data: {}'.format(t2-t1))
    print('Time to solve: {}'.format(t4-t3))
    
    
