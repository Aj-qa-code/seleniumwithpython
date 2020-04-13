#listas o arrays
smartphones = ["iphone","alcatel","samsung"]
    print(smartphones[1])    #1 es == a alcatel. Se cuenta desde el 0

paises  = ["Perú", "Chile", "Argentina", "Colombia"]
    print("El pais es: " + paises[-3])  #el pais será Colombia porque se cuenta de atrás

#para eleminar un elemento de la lista uso DEL

del paises[1]   #y eliminará Chile - tambien se puede usar numeros negativos
paises.remove("Argentina")

#para anadir elementos a una lista se usa .append() -se agrega al final
paises.append("Brasil")
paises.insert(7,"Espana")  #primero la posicion y luego el elemento

diccionarios = {} #clave y valor (keys values)
listas = [] #elementos
print(paises.items()) #muestra cada clave y valor
print(paises.values()) #muestra solo los valores
print(paises.keys()) #muesta solo las claves

print(len(paises)) #me dice cuantos elementos hay en total
paises.clean #vacia el diccionario
















