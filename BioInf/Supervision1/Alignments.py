# -*- coding: utf-8 -*-

from LCS import LCS, Ptr

def local_align(a, b):
    ''' Perform local alignment on sequences @a and @b.
    '''
    return LCS(a, b, {'match': 1, 'gap': -2, 'mismatch': -1})
    
def global_align(a, b):
    ''' Perform global alignment on sequences @a and @b.
    '''
    return LCS(a, b, {'match': 2, 'gap': -1, 'mismatch': -1})
    
def pretty_align(v, w, alignment_result):
    ''' Pad sequences with spaces according to alignment results.
    '''
    b = alignment_result[1]
    v_str = []
    w_str = []
    i, j = len(v), len(w)
    
    while i != 0 or j != 0:
        if b[i][j] == Ptr.Match:
            v_str += v[i-1]
            w_str += w[j-1]
            i -= 1; j -= 1
        elif b[i][j] == Ptr.Delete:
            v_str += v[i-1]
            w_str += '-'
            i -= 1
        elif b[i][j] == Ptr.Insert:
            v_str += '-'
            w_str += w[j-1]
            j -= 1
    
    v_aligned = ''.join(v_str[::-1])
    w_aligned = ''.join(w_str[::-1])
    
    return v_aligned, w_aligned
    