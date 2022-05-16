# Los conjuntos son colecciones de datos que se utilizan para almacenar varios
# elementos
# No están ordenados, son inmutables y no permiten valores duplicadods

ciudades = {'Barranquilla', 'Cali', 'Medellín'}
print(ciudades)
print(type(ciudades))
ciudades.add('Bogotá')
ciudades.remove('Cali')
for i in ciudades:
    print(i)
    
    
listas = [0,7,8,6,7,5,5,4,3,9,8,7,6,6,1,2,2,4, 67, 34, -8,-8, 67]
conjunto = set(listas)
print(conjunto)

