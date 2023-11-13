t = [5,6,7,11,13,15,16,17]

def nwd(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
        
    return a
    
def trojki(T):
    n = len(T)
    counter = 0
    
    for i in range(n-2):
        for j in range(4):
            x = i+1+(j%2)
            y = x+1+((j//2)%2)
            if x < n and y < n:
                if nwd(nwd(T[i],T[x]),T[y]) == 1:
                    counter += 1
                    print(T[i],T[x],T[y])
                    
    return counter
    
print(trojki(t))