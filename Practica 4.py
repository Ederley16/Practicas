#Ejercicio 1 Anagrama 
word_1= input("Ingrese palabra 1:")
word_2= input("Ingrese palabra 2:")
word_1=word_1.lower()
word_2=word_2.lower()

if sorted(word_1)==sorted(word_2):
    print("Las palabras ingresadas son anagrama")

else: 
    print("Las palabras ingresadas NO son anagrama")


#Ejercicio 2 
senten_1= input("Ingrese una frase:").lower()
senten_2= senten_1.split()

for senten in senten_2:
    if senten[0] != senten_1[0]:
        print(False)
        break
    
else:
    print(True)
