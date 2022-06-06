def ePrimo(n):
    c = 0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c == 2:
        return True
    else:
        return False
        
def maiorPrimo(r):
    c = r+1
    while True:
        c +=1
        for i in range(r+1,c):
            if ePrimo(i)==True:
                return i

n = int(input())
p = 2
lista = ''
while n>1 and p<=n:
    if n%p==0:
        n = n//p
        print(p, end=' ')
    p = maiorPrimo(p)
