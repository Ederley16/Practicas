#Ejercicio 1 

#Condicion >1 natural

num_1 = int(input("Introduzca un numero natural, mayor que 1:"))
fib_list = [1,1]

if num_1 < 1:
    print("El numero introducido es invalido")
else:
    while fib_list[-1] < num_1:
        fib_list.append(fib_list[-2]+fib_list[-1])

if fib_list[-1] < num_1:
    fib_list.pop(-1)
    print("La serie de fibonacci es: ", fib_list)
else:
    print("La serie de fibonacci es: ", fib_list)



#Ejercicio 2
num_2 = int(input("Introduzca un número natural, mayor a 1: " ))
fib_list = [1,1]
resultado = 0

while num_2 < 1:
  num_2 = int ( input ( "El numero introducido es invalido, intente nuevamente" ))

while  fib_list [-1] <=  num_2 :
    fib_list.append( fib_list [ - 2 ] + fib_list [ - 1 ])

if fib_list [-1] > num_2:
  fib_list.pop(-1)

for i in fib_list:
  resultado = resultado + i

print ( "La suma de fibonacci es: " , resultado )



#Ejercicio 3 suma de los primos 

num_3 = int(input("Introduzca un numero natural, mayor a 1: "))
fib_list =[1,1]
sum_primos = 0
primo_base_5 = 2 + 3 + 5

while num_3 < 1: 
  num_3 = int(input("El numero introducido no es valido, intentelo nuevamente"))


while fib_list[-1] < num_3:
    fib_list.append(fib_list[-2]+fib_list[-1]) 

if fib_list[-1] > num_3: 
  fib_list.pop(-1) 

fib_list.pop(0)
fib_list.pop(0) 

for i in fib_list:
  if num_3 <= 5 :
    sum_primos = sum_primos + i
    
  elif ((i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0)) :
    sum_primos = sum_primos + primo_base_5 + i


print("La suma de los numeros primos de fibonacci es: ", sum_primos)


#Ejercici 3 Suma de pares 
num_4 = int(input("Introduzca un numero natural, mayor a 1: "))
fib_list = [1,1]
sum_impar = 0

while num_4 < 1: 
  num_4 = int(input("El numero ingresado es invalido, intente nuevamente"))

while fib_list[-1] < num_4:
    fib_list.append(fib_list[-2]+fib_list[-1])

if fib_list[-1] > num_4: 
  fib_list.pop(-1)

for i in fib_list:
  if not i % 2 == 0:
    sum_impar = sum_impar + i