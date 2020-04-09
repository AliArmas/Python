#primer programa en python
#conceptos basicos
"""
a = 1
while a>=1 :
    print("Calculadora")
    print("1.-Sumar")
    print("2.-Restar")
    print("3.-Multiplicar")
    print("4.-Salir")
    a = int(input())
    print("Ingresa el primer numero")
    numero = int(input())
    print("Ingresa el segundo numero")
    numero2 = int(input())
    if (a == 1):
        print("El resultado es:", numero+numero2)
    elif (a == 2):
        print("El resultado es:", numero-numero2)
    elif (a == 3):
        print("El resultado es: ", numero*numero2)
    elif (a == 4):
        a = 0 
print("terminé")
"""        
#listas 
lista = ["hola","men","sas","asasd"]
saludo = lista[0]
print(saludo)
#sublistas
#subLista = lista [::-1]
subLista = lista [3:]
print(subLista)
#tuplas
#las tuplas son inmutables 
# es decir que no se puede cambiar su valor una vez declarada
#instancia de tupla

tupla = (1,2,3,"hola",2,3,4,5,6,7,6)
lista = [12,34,45,56]

"""
uno,dos,tres,cuatro,*cinco = tupla

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
"""
resultado = zip(tupla, lista)
#resultado = tuple(resultado)
resultado = list(resultado)
print(resultado)

