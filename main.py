def fatorial(num1):
    for i in range(num1, 1, -1):
        num1 *= i - 1
    return num1

num = int(input("Digite um número: "))
print(fatorial(num))
