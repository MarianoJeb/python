##LIST COMPREHENSION
##DEIXA O OCODIGO MAIS COMPACTO E FÁCIL PARA LER
##[OQ FAZER/retorno for ITEM in ITERABLE if CODITION(opcional)]

######SEM O LIST COMPREHENSION######
Hard=[]
for num in range(1,10):
    Hard.append(num*2)

######COM O LIST COMPREHENSION######
Easy=[item*2 for item in range(1,11)]
print (Easy)    

#EX:
nums=[1,-2,3,-4,5,-6,7,-8,10]

pos_nums=[num for num in nums if num>=0]
neg_nums=[num for num in nums if num<0]
even_nums=[num for num in nums if num%2==0]
odd_nums=[num for num in nums if num%2==1]

print(pos_nums)
print(neg_nums)
print(even_nums)
print(odd_nums)