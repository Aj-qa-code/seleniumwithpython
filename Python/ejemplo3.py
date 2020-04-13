#condicionales

numero = int(input("Digite su nemero: "))
if numero>0:
    print("El numero es positivo")
elif numero==0:
    print("El numero es cero")
else:
    print("El numero es negativo")
#El espacio se llama identación
#Lo que esta con identación esta dentro del if

#condicionales combinadas
edad = int(input("Digite su edad: "))
if edad>0 and edad<100:    #0>edad<100:  es lo mismo
    print("Edad correcta")
    if edad>=18:
        print("Es mayor de edad")
else:
    print("No es mayor de edad")

#Bucle while
numero = int(input("Digite su numero: "))
while numero<0:
    print("Error")
    numero = int(input("Digite su numero: "))

#Bucle while definido
i = 1
while i<=10:
    print(i)
    i += 1

#Bucle for
coleccion = {"andrea":12, "juan":15, "pedro":8}

for clave,valor in coleccion.items():
    print(f"{clave} - > {valor}")

coleccion = "Andrea"
for i in coleccion:
    print(f"{i}", end=" " )



