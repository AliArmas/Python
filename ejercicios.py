"""
Dado un diccionario, el cual almacena las calificaciones de un alumno
siendo las llaves los nombres de las materia y los valores las calificación
mostrar en pantalla el promedio del alumno.
"""
calC,calED,calBD,calPV,calFinal = None,None,None,None,None
calificaciones = {
    "Calculo":calC,
    "Estructura_de_datos":calED,
    "Bases_de_datos":calBD,
    "Programacion_Visual":calPV,
    "Calificacion_Final":calFinal,    
}
def addCal():
    control = True
    while control :
        print("1.-Calculo diferencial e integral")
        print("2.-Estructura de datos")
        print("3.-Bases de datos")
        print("4.-Programacion Visual")
        print("5.-Salir")
        opc1 = int(input())
        if  opc1 == 1:
            print("Ingrese la calificaion: ")
            calC = int(input())
            calificaciones["Calculo"] = calC
            print("Calificaion agreada correctamente")
        elif opc1 == 2:
            print("Ingrese la calificaion: ")
            calED = int(input())
            calificaciones["Estructura_de_datos"] = calED
            print("Calificaion agreada correctamente")
        elif opc1 == 3:
            print("Ingrese la calificaion: ")
            calBD = int(input())
            calificaciones["Bases_de_datos"] = calBD
            print("Calificaion agreada correctamente")
        elif opc1 == 4:
            print("Ingrese la calificaion: ")
            calPV = int(input())
            calificaciones["Programacion_Visual"] = calPV
            print("Calificaion agreada correctamente")
        elif opc1 == 5:
            control = False
        else:
            print("Ingrese una opcion valida")

def showCal():
    

accesControl = True
while accesControl :
    print("CALIFICACIONES DE CUATRIMESTRE")
    print("1.-Agreagr calificaciones")
    print("2.-Ver calificaiones")
    print("3.-Ver materias")
    print("4.-Calificaion mas alta")
    print("5.-Salir")
    opc = int(input())
    if opc == 1:
        addCal()
    elif opc == 2:
        #showCal()
        print("proximamente")
    elif opc == 3:
        print("proximamente")
        #showMat()
    elif opc == 4:
        #calTop()
        print("proximamente")
    elif opc == 5:
        accesControl = False
    else:
        print("Ups!")
        print("Ingrese una opcion Valida")
else:
    print("Vuelva pronto")

