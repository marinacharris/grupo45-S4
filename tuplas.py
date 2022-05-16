# Las tuplas son colecciones de datos que se utilizan para alamacenar 
# varios datos
# Las tuplas son ordenadas y son inmutables
# Las tuplas son colecciones indexadas

from regex import B


frutas = ('manzana', 'piña', 'pera')
nombres = ['Carlos', 'Pedro', 'Ana', 'Vivi']
datosPersonales = ('Juan', 50, True, 2500000.00, [0,1,2])
print(frutas)
print(frutas[0])
# frutas[1] = 'mango', esto NO se puede porque las tuplas son inmutables
print(type(frutas), type(nombres))
print(datosPersonales)
print(datosPersonales[4][2])
datosPersonales[4][2]= 56
print(datosPersonales)

def operaciones(a,b):
    suma = a+b
    resta = a-b 
    mul = a*b 
    div = a/b 
    return suma, resta, mul, div

resultados = operaciones(85,5)
print(resultados)
print(type(resultados))

for i in datosPersonales:
    print(i)
    
tupla4 = (1,) # tuplas de un solo elemento se le añade una coma
tuple5 = ('Pedro',)
print(type(tupla4), type(tuple5))