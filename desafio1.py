def reverse(n):
    inverso = 0 
    while n!=0:
        resto = n%10
        inverso = resto + inverso * 10  
        n = n//10   
    return inverso


n = int(input())
h = reverse(n)
if n == h:
    print("E palindromo")
else:
    print("Nao e palindromo")