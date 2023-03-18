option = 1
deportistas = [] 
while option != 0:       
    print('Ciclo ruta medellin')
    print('Opción 1 =  Ingresa el nombre del deportista')
    print('Opción 2 =  Corregir el tiempo del ciclista')
    print('Opción 3 =  listas los participantes')
    print('Opción 4 =  Descalificar o eliminar un ciclista')
    print('Opción 0 para salir')
    option = int(input('Escoja una opción: '))

    if(option == 1):
        deportista = { }
        deportista['id'] = len(deportistas) + 1
        deportista['nombre'] = input('Ingresa un nombre: ')
        deportista['edad'] = float(input('Ingresa la edad del deportista: '))
        deportista['pais'] = input('Ingresa el nombre del pais: ')
        deportista['equipo'] = input('A cual equipo pertenece: ')
        deportista['tiempo'] = float(input('Digite el tiempo de la vuelta en segundos: '))
        deportistas.append(deportista)
        print('deportista registrada')

    elif(option == 2):
        _id = int(input('Digite el id de la deportista que desea editar: '))
        for deportista in deportistas:
            if deportista['id'] == _id :
                print(f"el tiempo actual del deportista es: {deportista['tiempo']}")
                deportista['tiempo'] = float(input('Ingresa el nuevo tiempo: '))
                pass
        print('el numero no esta asignado a un deportista de la carrera')
    
    elif(option == 3):      
        for deportista in deportistas:
          print(deportista)

    elif(option == 4):
        buscarCiclista = int(input("Ingrese id de deportista a eliminar: "))
        for deportista in deportistas:
            if deportista['id'] == buscarCiclista:
                deportistas.remove(deportista)
                print(f"el deportista ha sido descalificado exitosamente")
                pass
        print("No se encontró la deportista")
    elif(option == 0):
        option = 0
    else:
        print('Opción invalida')
