##LIST COMPREHENSION

names:list[str]=['Bob', 'Luigi', 'Mario', 'Peach', 'Bowser']

long_names:list[str]=[name for name in names if len(names)>=4]
print(long_names)

##SET COMPREHENSION {}

values:list[int]=[5,5,5,11, 11, 5, 30, 30, 20, 5, 11, 2, 2, 100]
filtered_values={value for value in values if value>5 and value%2==0}
print(filtered_values)

##DICTIONARY COMPREHENSION {}

data:list[tuple[str,int]]=[('a',1), ('b',2), ('c',3)]

adict:dict[str, int]={k: v for k,v in data}
#Key: {Value for Key,Value in var}
print (adict)