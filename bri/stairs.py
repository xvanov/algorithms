
def remove(S, a):
    S.remove(a)
    return S

def f(N, S):
    print(N,S)
    if N == 0:
        total = 1
    elif N < 0:
        total = 0
    elif S == []:
        total = 0
    else:
        total = sum([f(N-a,remove(S,a)) for a in S])
    
    return total

if __name__ == '__main__':
    N = 20
    S = [1,2,3,4]
    print(f(N, S))