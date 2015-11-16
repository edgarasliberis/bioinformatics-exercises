# -*- coding: utf-8 -*-

class Forward(object):
    def __init__(self, Trans, Emis, Init):
        self.trans_p = Trans
        self.emit_p = Emis
        self.init_p = Init
        
    def prob(self, seq):
        L = len(seq)
        nstates = len(self.trans_p)
        
        F = [[0 for j in range(nstates)] for i in range(L)] 
        for k in range(nstates):
            F[0][k] = self.emit_p[seq[0]][k] * self.init_p[k]
        
        for i in range(1, L):
            for j in range(nstates):
                F[i][j] = self.emit_p[seq[i]][j] * sum(
                    F[i-1][k] * self.trans_p[k][j] for k in range(nstates))
        
        return sum([F[L-1][k] for k in range(nstates)])
