# -*- coding: utf-8 -*-

class Viterbi(object):
    def __init__(self, Trans, Emis, Init):
        self.trans_p = Trans
        self.emit_p = Emis
        self.init_p = Init
        
    def maxSeq(self, seq):
        L = len(seq)
        nstates = len(self.trans_p)
        
        # Initialisation        
        F = [[0 for j in range(nstates)] for i in range(L)] 
        for k in range(nstates):
            F[0][k] = self.emit_p[seq[0]][k] * self.init_p[k]
        
        # Only maintain paths for last considered seq element
        path = [[j] for j in range(nstates)]
        
        for i in range(1, L):
            newpath = {}
            for j in range(nstates):
                (prob, state) = max((F[i-1][k] * \
                    self.trans_p[k][j], k) for k in range(nstates))
                F[i][j] = self.emit_p[seq[i]][j] * prob
                newpath[j] = path[state] + [j]
            path = newpath
                
        (prob, state) = max((F[L-1][k], k) for k in range(nstates))
        return (prob, path[state])
    