def gen_primes(inicio:int, fim:int):
    for num in range (inicio,fim+1):
        if num<2:
            continue
        prime=True
        for div in range(2,num):
            if num%div==0:
                prime=False
                break
        if prime:
            yield num

numerozitos=gen_primes(50,100)
for i in numerozitos:
    print(i)