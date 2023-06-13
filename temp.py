'''
import timeit
import random
lista = [1,2,3,4,5]
lista = [random.randint(2,1000) for _  in range (10000000)]
start = timeit.default_timer()

x = map(lambda x:x**3, lista)
print(list(x))

stop = timeit.default_timer()
print(f "tiempo ejecucion = {stop - start} segundos")

nueva_lista = []
for e in lista:
    cubo = e**3
    nueva_lista.append(cubo)
    
print(nueva_lista)
'''

'''
L =  [1,2,3,4,5,6,7,8,9,10]
L2 = [n**2 for n in L if (n%2==0)]
print (L2)
'''

L =  [1,2,3,4,5,6,7,8,9,10]
L2 = [n**2 if (n%2==0) else (n**3) for n in L]
print(L2)