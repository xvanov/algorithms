# ALG - HW - 3
# Longest path in a network
# See ALG_HW_3.html for explanation of problem
# Kalin Ivanov
# 04.04.19

import time
import sys
import re

def parse_input():
    '''
    Reads input from BRUTE system stdin into string
    :return res: nested list representing tree structure
    
    Example:
    res = (5(14(1(19)(2(10(8)))(3(5)(12(4)))(20))(4(17)(15)))(10(21(44)(13(35)(5(34)(4))(2(23)))(55(8)))(12(9)(10(6)(5(11))(4)))))
    '''
    raw = input()
    res = make_tree(raw)
    return res

def read_input(fin):
    '''
    Reads input from a file into a string
    :param fin: file containing single line with the input
    :return res: nested list representing tree structure
    
    Example:
    res = (5(14(1(19)(2(10(8)))(3(5)(12(4)))(20))(4(17)(15)))(10(21(44)(13(35)(5(34)(4))(2(23)))(55(8)))(12(9)(10(6)(5(11))(4)))))
    '''
    with open(fin) as f:
        raw = f.readline()

    res = make_tree(raw)
    return res


def make_tree(data):
    '''
    Converts string of nested integers separated by parentheses into list
    :param data: strin of nested integers representing tree
    :return req(1)[0]: nested list of integers representing tree
    
    Example:
    data = (5(14(1(19)(2(10(8)))(3(5)(12(4)))(20))(4(17)(15)))(10(21(44)(13(35)(5(34)(4))(2(23)))(55(8)))(12(9)(10(6)(5(11))(4)))))
    return [5, [14, [1, [19], [2, [10, [8]]], [3, [5], [12, [4]]], [20]], [4, [17], [15]]], [10, [21, [44], [13, [35], [5, [34], [4]], [2, [23]]], [55, [8]]], [12, [9], [10, [6], [5, [11]], [4]]]]]
    '''
    items = re.findall(r"\(|\)|\w+", data)

    def req(index):
        result = []
        item = items[index]
        while item != ")":
            if item == "(":
                subtree, index = req(index + 1)
                result.append(subtree)
            else:
                result.append(int(item))
            index += 1
            item = items[index]
        return result, index

    return req(1)[0]

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
    
def solve(dat):
    '''
    Finds the longest path in the network
    :param dat: nested list describing network
    :return res: the cost of the longest network
    
    Example:
    dat = [5, [14, [1, [19], [2, [10, [8]]], [3, [5], [12, [4]]], [20]], [4, [17], [15]]], [10, [21, [44], [13, [35], [5, [34], [4]], [2, [23]]], [55, [8]]], [12, [9], [10, [6], [5, [11]], [4]]]]]
    res = 136
    
    Algorithm:
    input network
    1: from the first leaf in network (leaf1) find cost to all other leaves, 
    2: choose leaf with max cost (leaf2)
    3: from leaf2 find cost to all other leaves
    4: choose leaf with max cost (leaf3)
    return the cost
    
    '''
    res = 0
    res = traverse_all(dat)
    return res
    
class global_var():
    max_node = 0
    total = 0
    
def traverse_all(dat):
    node = dat
    
    def recurse_all(node):
        if len(node) == 1:
            return node[0]
        else:
            child_costs = []
            for child in node[1:]:
                tmp = recurse_all(child)
                # print(node, child, tmp)
                if tmp != None:
                    child_costs.append(tmp)
                    # print('tmp',tmp)
                else:
                    child_costs.append(child[0])
                    # print('child',child[0])
                    
            # print('costs',child_costs)
            
            node[0] = max(child_costs) + node[0]
            
            child_costs.pop(child_costs.index(max(child_costs)))
            
            if len(child_costs) < 1:
                tmp_second = 0
            else:
                tmp_second = max(child_costs)
                
            # print(tmp_second)
            tmp_total = node[0] + tmp_second

            # if tmp_total > 584:
            #     print(node[0], tmp_second, tmp_total)
            if tmp_total > global_var.total:
                global_var.total = tmp_total
                
    recurse_all(node)  

    return global_var.total


if __name__ == '__main__':
    ############### USE INPUT FILE BELOW THIS LINE #####################
    fn = sys.argv[1]
    fin = './datapub/pub'+ fn + '.in'
    fout = './datapub/pub'+ fn + '.out'
    
    dat = read_input(fin)
    res = read_output(fout)
    # print(dat)
    t1 = time.time()
    my_res = solve(dat)
    t2 = time.time()
    print("solution time {}".format(t2-t1))
    
    
    print('Actual result: {}'.format(res))
    print('My result: {}'.format(my_res))
    
    ############### TURN IN BELOW THIS LINE #####################
    
    # dat = parse_input()
    # # print(dat)
    
    # # print(dat)
    # my_res = solve(dat)
    # print(my_res)
    
    
    
    
    
    