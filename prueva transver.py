from random import randint
from statistics import mean, geometric_mean
nombres = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajadores = []
sueldos = []

def menu ():
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas.")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    
def sueldos_nombres():
    for i in nombres:
        todo = {"nombre":i},{"sueldos": randint(300000,2500000)}
        trabajadores.append(todo)
        sueldos.append(randint(300000,2500000))
    print(trabajadores)
    print ("sueldos asignados ") 
    
def clasificar():
    for i in sueldos:
        if i < 800000:
            print("Sueldos menores a 800.000:")
            for j in trabajadores:
                print(f"nombre de los empleados: {j["nombre"]} sueldos:{j["sueldos"]}")


def estadisticas():
    for i in sueldos:
        print (f"sueldos mas bajo: {min(sueldos)}")
        print (f"sueldos mas alto: {max(sueldos)}")
        print (f"promedio de los sueldos: {mean(sueldos)}")
        print (f"promedio aritmetico de los sueldos: {geometric_mean(sueldos)}")
        
        
while True:
    menu()
    opc = input("ingrese la opcion:")
    if opc == "1":
        sueldos_nombres()
    elif opc == "2":
        clasificar()
    elif opc == "3":
        estadisticas()   
    elif opc == "4":
        print("no pude profe :(")
    elif opc == "5":
        print ("Finalizando programa…")
        print ("Desarrollado por delvis santiago")
        print ( "RUT 27.119.672-5")
        break
    else:
        print("opcion no valida ")
    
            