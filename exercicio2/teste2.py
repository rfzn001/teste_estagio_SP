def is_fibonacci_number(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

try:
    number = int(input("Informe um número: "))
    if is_fibonacci_number(number):
        print(f"O numero {number} pertence a sequencia de Fibonacci.")
    else: 
        print(f"O numero {number} não pertence a sequencia de Fibonacci")
except ValueError:
    print("Por favor, insira um numero inteiro válido.")