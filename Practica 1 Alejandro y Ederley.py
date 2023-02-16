#EJERCICIO 1
list_1 = ["gato","","perro","ratones",""]
list_1.pop(1)
print(list_1)

list_1.pop(3)
print(list_1)


#EJERCICIO 2
list1 = [1,2,[200,400,[1000,6000],800],30,40]
list1[2][2].insert(1,5000)
print(list1)


#EJERCICIO 3
str = "Despues de la tempestad, viene la calma"
str1 = str[0] + str[19] + str[38]
print(str1)

#EJERCICIO 4
temperatura_centigradros = 20
temperatura_farhenheint = (temperatura_centigradros * 9/5) + 32
print(temperatura_farhenheint)


#EJERCICIO 5
dict1 = {"diez": 10, "veinte": 20, "treinta": 30}
dict2 = {"treinta": 30, "cuarenta": 40, "cincuenta": 50}
dict1.update(dict2)
print(dict1)


#EJERCICIO 6
diccionarioEstudiante = {
    "clase": {
        "estudiante": {
            "Nombre": "Mike", 
            "marcas": {
                "fisica": 70,
                "historia": 80 
            }
        }
    }
}
print(diccionarioEstudiante["clase"]["estudiante"]["marcas"]["historia"])

#EJERICIO 7
dict = {"nombre": "platon", "pais": "Antigua Grecia", "fecha_de_nacimiento": -427 ,"maestro": "Socrates", "alumno": "Aistoteles"}
dict["fecha de nacimiento"] = 428
print(dict)