# -*- coding: utf-8 -*-

class Ptr:
    LUnmatch, RUnmatch, Match, Bifurcation = range(4)

def is_pair(a, b):
    ''' Returns 1 if @a and @b can form a pair, 0 otherwise '''
    return int((a, b) in [('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G')])
    
def nussinov_fold(a):
    ''' Computes RNA fold of a string using Nussinov's algorithm '''
    D = [[0 for j in range(len(a))] 
            for i in range(len(a))]
    P = [[0 for j in range(len(a))] 
            for i in range(len(a))]
    B = [[0 for j in range(len(a))] 
            for i in range(len(a))]

# Alternative (lecturer's) iteration
#    for l in range(1, len(a)):
#        for i in range(0, len(a) - l):
#            j = i + l    

    # Fill in the matrix going backwards in rows, and then in order of columns
    for i in range(len(a) - 2, -1, -1):
        for j in range(i+1, len(a)):
            # Candidates for a max: 
            #  0. l unmatch
            #  1. r unmatch
            #  2. match
            #  3+. bifurcation
            candidates = \
                [D[i+1][j], D[i][j-1], D[i+1][j-1] + is_pair(a[i], a[j])] + \
                [D[i][k] + D[k+1][j] for k in range(i+1, j)] 
            D[i][j] = max(candidates)
            max_idx = candidates.index(D[i][j]) # Find out which one gave max
            # If bifurcation yielded maximum result
            if max_idx > 2:
                P[i][j] = Ptr.Bifurcation
                B[i][j] = max_idx - 2 + i
            else: # LUnmatch, RUnmatch, Match
                P[i][j] = max_idx 
    return D, P, B
    
def nussinov_brackets(a, fold):
    ''' Computes dot-bracket structure given string @a and it's fold. '''
    D, P, B = fold
    dbr = list('.' * len(a)) # String of all dots

    # Recursion implemented by stack-based iteration    
    stack = [(0, len(a)-1)] # Initially consider entire string
    while stack:
        i, j = stack.pop()
        if i >= j:
            continue
        
        # We have a match, ends form a bracketed pair
        if P[i][j] == Ptr.Match:
            stack.append((i+1, j-1))
            dbr[i] = '('
            dbr[j] = ')'
        # Skip over left item
        elif P[i][j] == Ptr.LUnmatch:
            stack.append((i+1, j))
        # Skip over right item
        elif P[i][j] == Ptr.RUnmatch:
            stack.append((i, j-1))
        # Split current item into (i, k), (k+1, j)
        elif P[i][j] == Ptr.Bifurcation:
            k = B[i][j]
            stack.append((k+1, j))
            stack.append((i, k))
            
    return ''.join(dbr) # Concat list into a string
