longest = 0
longestNum = 0

for j in range(2, 1000000):
    i = j
    length = 0
    
    while i != 1:
        if i % 2 == 0:
            i = i // 2
        else: 
            i = 3 * i + 1
        length += 1
    
    if length > longest:
        longest = length
        longestNum = j

print(longestNum, longest)