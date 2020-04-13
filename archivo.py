#primer programa en python
#conceptos basicos
"""
a = True
while a :
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
        a = False 
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
#conevertir tuplas a listas y viceversa

tupla_dos = tuple(lista)
print(tupla_dos)
##################################
#formatos de texto en python
texto = "curso de Python 3"
resultdo = texto.title()
resultado_1 = texto.replace("curso", "Perro")
print(resultado_1)
#
curso1 = "Python"
version = 3

#result = "Curso de %s %s" %(curso1, version)
result = "Curso de {b} {a}".format(a=curso1,b=version)
print(result)
#concatenacion
texto = "C" + texto[1:] + " " + str(12312312) + " " + "hola estoy concatenando"
print(texto)
#dicionarios
diccionario = {}
diccionario["nombre"] = "nombreUsuario" #llave con su valor
valor = diccionario["nombre"]
print(valor)
#no pueden existir llaves duplicadas
### obtener valores de llaves ### 
#keys() retorna un objeto dic_keys con todas las llaves///puedes convertir este objeto
#values() retorna un objeto dic_values con todos los valores///puedes convertir este objeto
#items() dic_items
dictionary = {"a":1,"b":2,"c":3}
res = dictionary.get("z","La llave no existe")
res2 = dictionary.setdefault("z", 43)
print()
#eliminar elemetos
#clear() eliminar todos los elementos al igual que con una lista
print(len(dictionary))
del dictionary["b"]
#sintaxis alternativa//dictionary.pop("b") obtiene el valor de la llave que removimos 
print(len(dictionary))
print(dictionary)
#cliclo for

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    print(i)
#asignaciones de valores mediante if
calificacion = int(input())
color = 'verde' if calificacion >= 7 else 'rojo'
print(calificacion, color)

#funciones

def crearUsurio (nombre,apellido,correo,contraseña=1234):
    return {
        'Nombre':nombre,
        'Apellido' :apellido,
        'Correo' : correo,
        'Contraseña': contraseña
    }

codi = crearUsurio("usuario","apellido","corre@gmail.com",)
usuario = list(codi.items())
for key,value in usuario:
    print(key," ",value)

#funciones con n parametros

def usuarios_autenticados(**kwargs):
    print(kwargs)


usuarios_autenticados(Ali=True, Dariana = False)

#generadores
def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1,maximo+1):
        yield numero * posicion,numero,posicion


for resultado,numero,posicion in tabla_multiplicar(9):
    print(numero," x " ,posicion, " = ", resultado)



#calses










































































