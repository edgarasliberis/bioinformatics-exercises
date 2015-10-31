# -*- coding: utf-8 -*-

class Ptr:
    Match, LUnmatch, RUnmatch, Bifurcation = range(4)

def is_pair(a, b):
    return int((a, b) in [('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G')])
    
def nussinov_fold(a):
    D = [[0 for j in range(len(a))] 
            for i in range(len(a))]
    P = [[0 for j in range(len(a))] 
            for i in range(len(a))]
    B = [[0 for j in range(len(a))] 
            for i in range(len(a))]
            
    # Fill in the matrix going backwards in rows, and then in order of columns
#    for l in range(1, len(a)):
#        for i in range(0, len(a) - l):
#            j = i + l    
    for i in range(len(a) - 2, -1, -1):
        for j in range(i+1, len(a)):
            # Candidates for a maximum: match, l unmatch, r unmatch, bifurcation
            candidates = [D[i+1][j-1] + is_pair(a[i], a[j]), D[i+1][j], D[i][j-1]] + [D[i][k] + D[k+1][j] for k in range(i+1, j)] 
            D[i][j] = max(candidates)
            max_idx = candidates.index(D[i][j])
            # If bifurcation yielded maximum result
            if max_idx > 2:
                P[i][j] = Ptr.Bifurcation
                B[i][j] = max_idx - 2 + i
            else:
                P[i][j] = max_idx # Match, LUnmatch, RUnmatch
    return D, P, B
    
def nussinov_brackets(a, fold):
    D, P, B = fold
    dbr = list('.'*len(a))

    stack = [(0, len(a)-1)]
    while stack:
        i, j = stack.pop()
        if i >= j:
            continue
        if P[i][j] == Ptr.Match:
            stack.append((i+1, j-1))
            dbr[i] = '('
            dbr[j] = ')'
        elif P[i][j] == Ptr.LUnmatch:
            stack.append((i+1, j))
        elif P[i][j] == Ptr.RUnmatch:
            stack.append((i, j-1))
        elif P[i][j] == Ptr.Bifurcation:
            k = B[i][j]
            stack.append((k+1, j))
            stack.append((i, k))
    return ''.join(dbr)
