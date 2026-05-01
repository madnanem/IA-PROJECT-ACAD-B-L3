import re
import math
from collections import Counter

def word_freq(tokens, n=30):
    return Counter(tokens).most_common(n) 
def ngrams(tokens, n, top=20): 

    grams = [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
    return Counter(grams).most_common(top)

def collocations_pmi(tokens, top=15):
    uni = Counter(tokens)
    bi  = Counter(tuple(tokens[i:i+2]) for i in range(len(tokens)-1))
    N   = len(tokens)

    res = []
    for (w1, w2), cnt in bi.items():
        if cnt < 2:
            continue

        p12 = cnt / N
        p1  = uni[w1] / N
        p2  = uni[w2] / N

        if p1 and p2:
            pmi = math.log2(p12 / (p1 * p2))
            res.append((" ".join([w1, w2]), round(pmi, 3), cnt))

    return sorted(res, key=lambda x: x[1], reverse=True)[:top]