'''
Utils
'''

def minmax(l, h, n):
    if n < l: return l
    if n > h: return h
    return n

def normalizer(tl, tb, rl, rb):
    r = (tb - tl) + tl
    u = (rb - rl)
    def scale(m):
        return ((m - rl) / u) * r
    return scale
