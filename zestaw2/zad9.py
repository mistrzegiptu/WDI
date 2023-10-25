k = int(input("Input k, x e <1, k>: "))
n = int(input("Input amount of rectangles: "))

area = 0
x = 1
w = (k-1) / n

for _ in range(n):
    area += w * 1/x
    x += w
    
print(area)