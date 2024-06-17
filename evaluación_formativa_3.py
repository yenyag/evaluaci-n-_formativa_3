#importaciones
import time;
import csv

def Registrar_Trabajador(trabajadores):
    Nombre = input("Ingrese Nombre")
    Apellido = input("Ingrese Su Apellido")
    cargo = input("ingrese su cargo")
    sueldo_bruto = int(input("ingrese su sueldo bruto"))

def Trabajador = Trabajador(Nombre, Apellido, Cargo, Sueldo_Bruto)
    trabajadores.append(trabajadores)
def imprimir_plantilla(Trabajadores):
    cargo=input("Ingrese el cargo para imprimir la plantilla o 'todos' para imprimir todos: ")
    pancracio = "plantilla.txt"
     with open(nombre_archivo, "w") as file:
        file.write("Trabajador, Cargo, Sueldo Bruto, Desc. Salud, Desc. AFP, Liquido a pagar\n")
        for trabajador in Trabajadores:
            if cargo.lower() == 'todos' or trabajador.cargo.lower() == cargo.lower():
                file.write(f"{trabajador.nombre} {trabajador.apellido}, {trabajador.cargo}, {trabajador.sueldo_bruto},
                           {trabajador.desc_salud}, {trabajador.desc_afp}, {trabajador.liquido_a_pagar}\n")
    print(f"Plantilla generada en {Pancracio}")


trabajadores=[]
#Aqui va el Menu
while True:
    print("\n---Menu de Opciones---\n")
    print("Opcion 1. Registrar trabajador")
    print("Opcion 2. Listar a todos los trabajadores")
    print("Opcion 3. Imprimir planilla de sueldos");
    print("Opcion 4. Salir del Programa");

    try:
        opcion=int(input("Ingrese la Opcion que deseas utilizar ----> "));
    except ValueError:
        print("Ingrese una opcion valida, desde 1 a 4")
    else:
        #Registro
        if opcion==1:
            print("Bienvenido empleado, por favor registre al trabajador");
            #Ingresando datos del trabajador
            Registrar_Trabajador(Trabajadores)



        elif opcion==2:
            print("Mostrando la Lista de todos los trabajadores actuales...");
            #Mostrando la lista de trabajadores que se han registrado
            listar_trabajadores(Trabajadores)



        elif opcion==3:
            print("Imprimiendo plantilla de sueldos");



        elif opcion==4:
            print("Saliendo del sistema...");
            time.sleep(2)
            print("Secion Cerrada Correctamente");
            break;
        else:
                print("Debes ingresar opciones desde 1 a 4");




