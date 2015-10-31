# Bioinformatics Supervision #1 
# Author: Edgar, el398@cam.ac.uk

from Alignments import *

if __name__ == '__main__':
    
    # 1.1 Implement Needleman-Wunsch and Smith-Waterman
    
    # Test for global alignment
    a, b = "CATGT", "ACGCTG"
    res = global_align(a, b)
    a_al, b_al = pretty_align(a, b, res)
    
    print "*******************************************"
    print "Global alignment:", a, "<->", b
    print b_al
    print a_al
    print "Score:", res[0][len(a)][len(b)]
    print "*******************************************"
    
    # Test for local alignment
    a, b = "TAATA", "TACTAA"
    res = local_align(a, b)
    a_al, b_al = pretty_align(a, b, res)
    
    print "*******************************************"
    print "Local alignment:", a, "<->", b
    print b_al
    print a_al
    print "Score:", res[0][len(a)][len(b)]
    print "*******************************************"
    
    # Implementing affine gap would require maintaining several matrices in 
    # LCS (F, G, H, V) and a different initialisation expression for V
    
    ## 1.2 Dynamic programming
    # Similarly to a |v| x |w| matrix we build for dynamic programming
    # approach, we can build a grid-like DAG with |v| x |w| nodes, with edges
    # going from to the right, bottom and diagonal neighbours of any given 
    # node. Edge costs would be costs of Insert, Match or Delete. We can then
    # find a "longest" path in this DAG, which would correspond to finding a
    # highest-score path in a matrix.
    
    ## 1.3 Alignment scores
    # In local alignment we want to find almost-perfectly matching intervals,
    # possibly padded with many gaps in between. 
    # Therefore, we'd like to penalise mismatch more than rewarding a match, 
    # and prefer long gaps. To achieve the latter, we set a higher gap open
    # score (penalty for starting a gap), but lower gap extend (we're okay
    # with having larger gaps), which should be non-zero (prefer alignment)
    
    ## 2.1 Nussinov algorithm
    