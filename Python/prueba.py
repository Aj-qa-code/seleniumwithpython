print('Hola Mundo\nMi nombre es Andrea')

cadena = "Estoy 'estudiando'"
print(cadena)
print(type(cadena))

number = 10
print(number)
print(type(number))

valor = True
print(valor)
print(type(valor))

num1 = 10
num2 = 5.6
resultado = (num1 + num2) * 10 / 6

print("El resultado es:", resultado)  

#Python permite el tipado dinámico
''' 
   El tipado dinámico es que una variable puede 
   contener diferentes tipos de dato
   a lo largo del programa.
'''
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





