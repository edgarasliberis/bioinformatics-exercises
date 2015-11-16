# Bioinformatics supervision 3
# Edgar Liberis, el398@cam.ac.uk

from Forward import *
from Viterbi import *
from math import log

if __name__ == '__main__':

    TransitionP = [[0.8, 0.2], [0.4, 0.6]]
    InitialP = [0.5, 0.5]
    EmissionP = {
        'a': [0.25, 0.1],
        't': [0.25, 0.1],
        'c': [0.25, 0.4],
        'g': [0.25, 0.4]
    }
    
    for seq in ["aactgcacatgcggcgcgcccgcgctaat", "gggcgcgggcgccccgcg"]:
        # NB. Book and Lio's notes use integrated transition and initial 
        # distribution matrix (initial step is transition from dummy state 0)
        # This is confusing, so I will separate them out.  
        # Wiki has non-integrated Viterbi algorithm implementation
        
        # 1.1. Implement Forward algorithm
        fwd = Forward(TransitionP, EmissionP, InitialP)
        p = fwd.prob(seq)
        print "**************************************"
        print "Probability of", seq, ":", p
        print "Log probability:", -log(p)
        print "**************************************"
    
        # 1.2. Implement Viterbi algorithm
        vtb = Viterbi(TransitionP, EmissionP, InitialP)
        (prob, path) = vtb.maxSeq(seq)
        print "**************************************"
        print "Viterbi path:"
        print "P =", prob
        print seq
        print ''.join(str(i) for i in path)
        print "**************************************"
        
        # 1.3. Length distribution
        # Suppose we have a string of only G-C (with equal emission probili-
        # ties for each state).
        # Once HMM enters state 1 (detect G-C islands), modify the probability
        # of going out of this state to 1/200, and staying to 199/200. Then on 
        # average HMM will stay in that state for 200 characters.
