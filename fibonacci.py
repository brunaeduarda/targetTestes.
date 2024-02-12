def isFibonacci(numero):
    fib1=0
    fib2=1
    
    while (fib2<numero):
        fib1, fib2 = fib2, fib1+fib2
    
    return fib2==numero

numero = int(input("Digite um número: "))
if (isFibonacci(numero)):
  print("Faz parte da sequência de Fibonacci")
else:
  print("Não faz parte da sequência de Fibonacci")




    
