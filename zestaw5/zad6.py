T = [1,7,3,5,11,2]

minCounter = 10**10

def f(T, se = 0, si = 0, p = 0):
    n = len(T)
    global minCounter
    
    if se == si and se != 0 and 0 < p < minCounter:
        print(se)
        minCounter = p
    elif p == n:
        if se == si:
            return se
    else:
        f(T, se, si, p+1)
        f(T, se+T[p], si+p, p+1)

f(T)