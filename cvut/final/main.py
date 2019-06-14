# ALG - Final
# Kalin Ivanov
# 18.06.19

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
    
    global_var.global_graph = graph.Graph(meta[0])
    nodes = {}
    
    for i in range(meta[1]):
        line = [int(j) for j in raw_in(brute).split(' ')] # convert each entry in line to int
        
        global_var.global_graph.addedge(line[0], line[1])
        try:
            nodes[line[0]]
        except:
            nodes[line[0]] = []
        try:
            nodes[line[1]]
        except:
            nodes[line[1]] = []
        
        len0 = len(nodes[line[0]])
        len1 = len(nodes[line[1]])

        nodes[line[0]].append((line[1], len1))
        nodes[line[1]].append((line[0], len0))
            
    return meta 

def read_output():
    '''
    Reads output file (solution of input file) and converts it to int
    :return res: solution as an int
    '''
    fn = sys.argv[1]
    fout = './datapub/pub'+ fn + '.out'
    with open(fout) as f:
        res = f.readline()
    return res
    
def find_degree(meta):
    degree = {}
    for i in range(meta[0]):
        degree[i] = len(global_var.global_graph.nodes[i].neighbours)
    return degree
    
def find_grade(degree):
    grade = {}
    T = (99999999, 0)
    L = (0, 0)
    for d in degree:
        grade[d] = 0
        for n in global_var.global_graph.nodes[d].neighbours:
            grade[d] = grade[d] + degree[n.id]
    for d in degree:
        if grade[d] >= L[0]:                
            L = (grade[d], d)
        if grade[d] < T[0]:
            T = (grade[d], d)
    return grade, T, L
    
def solve(meta):
    sol = 99999999999999
    degree = find_degree(meta)
    grade, T, L = find_grade(degree)
#    print(grade)
#    print(T, L)
    D = graph.BFS2(global_var.global_graph, T[1], [L[1]])
    D = D[L[1]] - 1

    T = T[1]
    L = L[1]
    return T, L, D    

if __name__ == '__main__':
    ################ TURN IN BELOW THIS LINE #####################
#    t1 = time.time() # comment out
    meta = read_input()
#    t2 = time.time() # comment out

    
#    print('meta: {}'.format(meta))

    
#    t3 = time.time() # comment out
    T, L, D = solve(meta)
#    t4 = time.time() # comment out
    
#    print(global_var.global_graph.nodes[0].neighbours[3].id)
    
    print(T, L, D)
    
    ############### COMMENT OUT BELOW THIS LINE ##################

#    res = read_output()
#    print('Actual result: {}'.format(res))

#    print('Time to read data: {}'.format(t2-t1))
#    print('Time to solve: {}'.format(t4-t3))
#    
    
