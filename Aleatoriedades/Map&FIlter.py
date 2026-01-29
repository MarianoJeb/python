##MAP
""" APLICA A FUNÇÃO A TODOS OS ITENS DA LISTA
map(func, list) """

number_list=[2,3,4,5,6,7]

new_list=list(map(lambda num: num**2, number_list))
print(new_list)



##FILTER
""" FILTRA UMA LISTA CONFORME A FUNÇÃO
filter(func, list) """

even_numbers=list(filter(lambda num: num%2==0, number_list))
print(even_numbers)
