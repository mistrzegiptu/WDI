#SOLUTION BY KAMIL RUDNY

T = [7,8,6,4,7,3]

def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i+=2
    
    return True

def find_max(T):
    n = len(T)
    max_res = 0

    for l in range(n):
        for k in range(2, n):
            A = T[l:k]
            if len(A) > 0:
                i, j, res = 0, 1, 0

                while j < len(A):
                    res += A[i] * A[j]
                    i += 2
                    j += 2
                
                if isPrime(res):
                    max_res = max(max_res, res/len(A))

                i, j, res = 1, 2, A[0]

                while j < len(A):
                    res += A[i] * A[j]
                    i += 2
                    j += 2
                
                if isPrime(res):
                    max_res = max(max_res, res/len(A))
    
    return max_res

print(find_max(T))