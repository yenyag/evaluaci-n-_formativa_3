#importaciones
import time;

class Trabajador:
    def __init__(self, nombre, apellido, cargo, sueldo_bruto):
        self.nombre=nombre
        self.apellido=apellido
        self.cargo=cargo
        self.sueldo_bruto=sueldo_bruto
        self.desc_salud=self.calcular_salud()
        self.desc_afp=self.calcular_afp()
        self.liquido_a_pagar=self.calcular_liquido()
        
    def calcular_salud(self):
        return self.sueldo_bruto*0.07

    def calcular_afp(self):
        return self.sueldo_bruto*0.12

    def calcular_liquido(self):
        return self.calcular_liquido
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.cargo}, Sueldo Bruto: {self.sueldo_bruto}, Desc. Salud: {self.desc_salud}, Desc. AFP: {self.desc_afp}, Liquidio a Pagar: {self.liquido_a_pagar}"


def Registrar_Trabajador(Trabajadores):
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    cargo   = input ("Ingrese cargo: ") 
    sueldo_bruto = float(input ("Ingrese sueldo bruto: "))

    trabajador = Trabajador(nombre, apellido, cargo, sueldo_bruto)
    Trabajadores.append(trabajador)

def listar_trabajadores(Trabajadores):
    for trabajador in Trabajadores:
        print(trabajador)

def imprimir_plantilla(Trabajadores):
    cargo=input("Ingrese el cargo para imprimir la plantilla o 'todos' para imprimir todos: ")
    Pancracio = "plantilla.txt"
        
    with open(Pancracio, "w") as file:
        file.write("Trabajador, Cargo, Sueldo Bruto, Desc. Salud, Desc. AFP, Liquido a pagar\n")
        for trabajador in Trabajadores:
            if cargo.lower() == 'todos' or trabajador.cargo.lower() == cargo.lower():
                file.write(f"{trabajador.nombre} {trabajador.apellido}, {trabajador.cargo}, {trabajador.sueldo_bruto}, {trabajador.desc_salud}, {trabajador.desc_afp}, {trabajador.liquido_a_pagar}\n")
    print(f"Plantilla generada en {Pancracio}")


Trabajadores=[]

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
            imprimir_plantilla(Trabajadores)


        elif opcion==4:
            print("Saliendo del sistema...");
            time.sleep(2)
            print("Secion Cerrada Correctamente");
            break;
        else:
                print("Debes ingresar opciones desde 1 a 4");
