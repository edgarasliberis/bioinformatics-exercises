# -*- coding: utf-8 -*-

class Ptr:
    Match, Insert, Delete = range(3)

def LCS(v, w, prms):
    s = [[(j if i == 0 else i) * prms['gap'] 
            for j in range(len(w)+1)] 
            for i in range(len(v)+1)]
    b = [[(Ptr.Delete if j == 0 else Ptr.Insert) 
            for j in range(len(w)+1)]
            for i in range(len(v)+1)]
            
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            candidates = [
                s[i-1][j-1] + 
                    (prms['match'] if v[i-1] == w[j-1] else prms['mismatch']),
                s[i][j-1] + prms['gap'],
                s[i-1][j] + prms['gap']]
            s[i][j] = max(candidates)
            b[i][j] = candidates.index(s[i][j])
    return s, b
