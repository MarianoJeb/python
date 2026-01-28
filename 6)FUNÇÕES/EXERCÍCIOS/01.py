##EXERCICIO 01
""" Crie uma função chamada quadrado(numero) que recebe um número como argumento e retorna o quadrado dele.
Depois, use a função com um valor recebido via input() e exiba o resultado com print(). """

def quadrado(numero):
    return numero**2

num=float(input("Fale o número:"))
print(f'O numero {num} ao quadrado é igual a {quadrado(num)}!')