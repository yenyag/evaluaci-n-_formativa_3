#Benjamin Almonacid, Vicente Placencia, Martín Villarroel
#sección 006-D
#importaciones
import time;

class Trabajador:
    def __init__(self, nombre, apellido, cargo, sueldo_bruto):
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.sueldo_bruto = sueldo_bruto
        self.desc_salud = self.calcular_salud()
        self.desc_afp = self.calcular_afp()
        self.liquido_a_pagar = self.calcular_liquido()

    #Calcular los Sueldos y cada uno de sus valores respectivos   
    def calcular_salud(self):
        return self.sueldo_bruto*0.07

    def calcular_afp(self):
        return self.sueldo_bruto*0.12
 
    def calcular_liquido(self):
        return self.sueldo_bruto - self.desc_salud - self.desc_afp
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.cargo}, Sueldo Bruto: {self.sueldo_bruto}, Desc. Salud: {self.desc_salud}, Desc. AFP: {self.desc_afp}, Liquido a Pagar: {self.liquido_a_pagar}"

#Proceso para registrar a los trabajadores
def registrar_trabajador(trabajadores):
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    cargo   = input ("Ingrese cargo: ") 
    sueldo_bruto = float(input ("Ingrese sueldo bruto: "))

    trabajador = Trabajador(nombre, apellido, cargo, sueldo_bruto)
    trabajadores.append(trabajador)
    #guardar lista de trabajadores en archivo despues de registrar un trabajador nuevo
    funcionArchivo(trabajadores)

    
#Da el listado de los trabajadores
def listar_trabajadores(trabajadores):
    for trabajador in trabajadores:
        print(trabajador)
        
#Imprimir la plantilla
def imprimir_plantilla(Trabajadores):
    cargo=input("Ingrese el cargo para imprimir la plantilla o 'todos' para imprimir todos: ")
    archivo= "plantilla.txt"
        
    with open(archivo, "w") as file:
        file.write("Trabajador, Cargo, Sueldo Bruto, Desc. Salud, Desc. AFP, Líquido a Pagar\n")
        for trabajador in trabajadores:
            if cargo.lower() == 'todos' or trabajador.cargo.lower() == cargo.lower():
                file.write(f"{trabajador.nombre} {trabajador.apellido}, {trabajador.cargo}, {trabajador.sueldo_bruto}, {trabajador.desc_salud}, {trabajador.desc_afp}, {trabajador.liquido_a_pagar}\n")
    
    print(f"Plantilla generada en {archivo}")
    #Guardar lista de trabajadores en archivo despues de imprimir la plantilla
    funcionArchivo(trabajadores)

def funcionArchivo(trabajadores, nombre_archivo='list_of_employee.txt'):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Trabajador, Cargo, Sueldo Bruto, Desc. Salud, Desc. AFP, Líquido a Pagar\n")
        for trabajador in trabajadores:
            archivo.write(f"{trabajador.nombre} {trabajador.apellido}, {trabajador.cargo}, {trabajador.sueldo_bruto}, {trabajador.desc_salud}, {trabajador.desc_afp}, {trabajador.liquido_a_pagar}\n")
#Lista de trabajadores
trabajadores=[]
#Aqui va el Menu
while True:
    print("\n---Menu de Opciones---\n")
    print("Opcion 1. Registrar Trabajador")
    print("Opcion 2. Listar a Todos los Trabajadores")
    print("Opcion 3. Imprimir Planilla de Sueldos");
    print("Opcion 4. Salir del Programa");

    try:
        opcion=int(input("Ingrese La Opcion Que Deseas Utilizar ----> "));
    except ValueError:
        print("Ingrese Una Opcion Valida, Desde 1 a 4")
    else:
        #Registro 
        if opcion==1:
            print("Bienvenido empleado, por favor registre al trabajador ---->");
            #Ingresando datos del trabajador
            registrar_trabajador(trabajadores)

        #Lista de Empleados
        elif opcion==2:
            print("Mostrando La Lista De Todos Los Trabajadores Actuales...");
            listar_trabajadores(trabajadores)

        #Imprimir la Plantilla de Datos
        elif opcion==3:
            print("Imprimiendo Plantilla De Sueldos");
            imprimir_plantilla(trabajadores)

        #Salir del Programa
        elif opcion==4:
            print("Saliendo Del sistema...");
            time.sleep(2)
            print("Secion Cerrada Correctamente");
            break;
        else:
                print("Debes Ingresar Opciones Desde 1 a 4");
                
