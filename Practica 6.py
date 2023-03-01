num_rows = int(input("Ingrese un numero de filas:  "))
num_colum = 2

matrix = []
last_value = 0

for rows in range(1, num_rows + 1):
    list = []
    if rows % 2 != 0:
        for columns in range(1, num_colum + 1):
            list.append(last_value + columns)

        list.append(list[0] + list[1])
        matrix.append(list)
        last_value = list[1]

    if rows % 2 == 0 :
        for columns in range(1, num_colum + 1):
            list.append(last_value + columns)

        list.append(list[0]+ list[1])
        matrix.append(list)
        last_value = list[1]

print(matrix)