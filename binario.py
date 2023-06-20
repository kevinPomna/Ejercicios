print("-----------------------------")
print("-----------------------------")
print("Convertidor de decimal a binario")
numero = int(input("Ingrese el número: "))
binario = ""

while numero > 0:
    residuo = numero % 2
    numero = numero // 2
    binario = str(residuo) + binario

print("El número en binario es:", binario)


print("-----------------------------")
print("-----------------------------")