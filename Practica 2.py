Num1=float(input("Ingrese un numero:"))
Num2=float(input("Ingrese otro numero:"))
Operacion=input("Operacion a realizar: 1. Suma(+), 2.Resta(-), 3.Multuplicación(*), 4.División(/):")

if Operacion == "1" or Operacion == "+":
     print(float(input(Num1+Num2)))

if Operacion == "2" or Operacion == "-":
    print(float(input(Num1-Num2)))

if Operacion == "3" or Operacion == "*":
    print(float(input(Num1*Num2)))

if Operacion == "4" or Operacion == "/":
    print(float(input(Num1/Num2)))

print