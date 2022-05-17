# función lambda es anónima, no tiene nombre
# Es una función pequeña de una sola línea
# Sintaxis - >> lambda arguments : expression

suma =  lambda a,b: a+b
print(suma(8,7))

def triplica(n):
    return lambda a: a*n

tempo = triplica(3)

print(tempo(4))
print(tempo(7))
print(tempo(6))