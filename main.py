
def f(n):
    if n < 0:
        return 1
    if n >0 and n % 2 == 1:
        return 1 + f(n - 1)
    return f(n/2)

count = 0
for i in range (1,500000000):
    if f(i) == 5:
        count +=1

print (count)