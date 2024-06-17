#Listas =D
listaTrabajadores=[]
listaCargos=[]
listaSueldoBruto=[]

#Aquí va el Menú :D
while True:
    print("\n---Menú de Opciones---\n")
    print("Opción 1. Registrar trabajador")
    print("Opción 2. Listar a todos los trabajadores")
    print("Opción 3. Imprimir planilla de sueldos");
    print("Opción 4. Salir del Programa");
    try:
        opcion=int(input("Ingrese la Opción que deseas utilizar ----> "));
    except ValueError:
        print("Ingrese una opción válida, desde 1 a 4")
    else:
        #Register
        if opcion==1:
            print("Bienvenido empleado, por favor registrese: ");
            Input
            

        elif opcion==2:
            print("Mostrando la Lista de todos los trabajadores actuales...");


        elif opcion==3:
            print("Imprimiendo planilla de sueltos");


        elif opcion==4:
            print("Saliendo del sistema...");
            break;

        else:
                print("Debes ingresar opciones desde 1 a 4");




