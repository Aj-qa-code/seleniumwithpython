#operadores aritméticos () ** */% + -
3**3 - (13/5 + (2*4))
#operadores relacionales
''' > mayor que
    < menor que
    >= mayor o igual que
    <= menor o igual que
    != diferente
    == igual
'''
#prioridad de los operadores
'''
    1 () 
    2 ** 
    3 * / % not
    4  + - and
    5 < > == != or
'''
resultado = 10 < 20
print(resultado)

a = 10
b = 12
c = 13
d = 10

resultado = ((a>b) or (a<c)) and ((a==c) or (a>=b))
print(resultado)

resultado = not ((a<b) or (a==d))
print(resultado)

#salida de datos
nombre = "Andrea"
edad = 31

print("hola", nombre, "tienes", edad, "anos")
print("Hola {} tienes {} anos".format(nombre, edad))
print(f"Hola {nombre} tienes {edad} anos")

#entrada de datos

numero = float(input("digite el numero: "))
print(f"el numero es{numero}")





