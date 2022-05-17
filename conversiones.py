#conversión de cadenas
cadena = 'Ventana'
lista = list(cadena)
tupla = tuple(cadena)
conjunto = set(cadena)
print(lista, tupla, conjunto)

#conversión de listas

listas = ['M', 'A', 'R']
cadena = ''.join(listas)
print(cadena)

#Conversion a diccionarios
cadena = "Colombia"
diccionario = dict(zip(range(len(cadena)),cadena))
print(diccionario)

conjunto = {3,6,'A',9}
diccionario2 = dict(zip(range(len(conjunto)),conjunto))
print(conjunto)

#Conversión de diccionarios a cadena
diccionario ={
    0: 'H',
    1: 'O',
    2: 'L',
    3: 'A'
}
cadena = ''.join(diccionario.values())
print(cadena)
