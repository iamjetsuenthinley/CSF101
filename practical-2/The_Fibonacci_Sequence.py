def fibonacci_sequence(n):
    a,b=0,1
    print(a,b, end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c, end=" ")
        a, b = b, c

term=int(input("Till which term do you want the fibonacci sequence for: "))

fibonacci_sequence(term)
    