from app.gestor import GestorSistema
from colorama import Fore, Back, Style, init

gestor = GestorSistema()

init(autoreset = True)

while True:
    print('')
    print("\033[0;37m             \033[0;97m▄\033[0;37m                         \033[0;97m▄▄\033[0;37m    \033[0;97m▄\033[0;37m                                  \033[0;97m▄\033[0;37m                                       \033[0;97m▄\033[0;37m       \033[0;97m▄▄\033[0;37m                         \033[0;97m▄\033[0;37m                        \033[0m")
    print("\033[0;37m           \033[0;97m▄\033[0;97;46m██\033[0;37m                        \033[0;97m▐\033[0;97;46m██\033[0;97m▌\033[0;37m \033[0;97m▄\033[0;97;46m██\033[0;37m                                  \033[0;97;46m██\033[0;97m▄\033[0;37m                                   \033[0;97m▄\033[0;97;46m██\033[0;37m      \033[0;97m▐\033[0;97;46m██\033[0;97m▌\033[0;37m                      \033[0;97m▄\033[0;97;46m██\033[0;37m                        \033[0m")
    print("\033[0;37m           \033[0;97;46m███\033[0;37m                    \033[0;97m▄\033[0;37m    \033[0;97m▀▀\033[0;37m  \033[0;97;46m███\033[0;37m                                  \033[0;97;46m███\033[0;37m                    \033[0;96m▄▄\033[0;37m             \033[0;97;46m███\033[0;37m       \033[0;97m▀▀\033[0;37m                  \033[0;97m▄\033[0;37m    \033[0;97;46m███\033[0;37m                        \033[0m")
    print("\033[0;37m  \033[0;97m▄\033[0;97;46m███\033[0;97m▄▄▄\033[0;37m  \033[0;97;46m█▓█\033[0;37m     \033[0;97m▄▄\033[0;97;46m█\033[0;97m▄\033[0;37m \033[0;97;46m█\033[0;97m▄▄\033[0;37m \033[0;97m▄\033[0;97;46m█\033[0;97m▌\033[0;37m  \033[0;97m▐\033[0;97;46m█▓\033[0;97m▄\033[0;37m  \033[0;97m▄▄\033[0;97;46m█\033[0;37m \033[0;97;46m█▓█\033[0;37m    \033[0;97m▄\033[0;97;46m██████\033[0;97m▄\033[0;37m \033[0;97m■▄\033[0;97;46m█\033[0;37m \033[0;97m▄\033[0;97;46m█\033[0;97m▄▄\033[0;37m       \033[0;97m▄\033[0;97;46m██████▓█\033[0;37m \033[0;97m▄\033[0;97;46m██████\033[0;97m▄\033[0;37m      \033[0;97m▄\033[0;97;46m█\033[0;36m  \033[0;96m▀\033[0;97;46m██▓\033[0;36m \033[0;37m  \033[0;97m▄\033[0;97;46m██████\033[0;97m▄\033[0;37m \033[0;97;46m█▓█\033[0;37m \033[0;97m▄\033[0;97;46m█\033[0;97m▄▄\033[0;37m  \033[0;97m▄▄\033[0;97;46m█\033[0;37m \033[0;97m▄\033[0;97;46m██████\033[0;97m▄\033[0;37m  \033[0;97m▄\033[0;97;46m█\033[0;97m▌\033[0;37m  \033[0;97m▐\033[0;97;46m█▓\033[0;97m▄\033[0;37m  \033[0;97;46m█▓█\033[0;37m    \033[0;97m▄\033[0;97;46m█\033[0;97m▀\033[0;97;46m████▓\033[0;97m▀\033[0;37m  \033[0;97m▄\033[0;97;46m███████\033[0;97m▀\033[0m")
    print("\033[0;97m▄\033[0;97;46m▒▓\033[0;37m  \033[0;97m▀\033[0;97;46m▓▒▓\033[0;97m▌\033[0;37m \033[0;97;46m▓▒▓\033[0;37m   \033[0;97m▐\033[0;97;46m▓▒▓\033[0;37m  \033[0;97m▀\033[0;97;46m▓▒\033[0;36m▌\033[0;97m▐\033[0;97;46m▒▓\033[0;37m    \033[0;97;46m▓▒▓\033[0;36m▌\033[0;97m▀\033[0;97;46m▓▒▓\033[0;37m \033[0;97;46m▓▒▓\033[0;37m   \033[0;97;46m▓▒▓\033[0;37m  \033[0;97m▀\033[0;97;46m▓▒▓\033[0;97m▌\033[0;36m▐\033[0;97;46m▒▓\033[0;97m▀\033[0;37m  \033[0;97;46m▓▒▓\033[0;97m▌\033[0;37m    \033[0;97;46m▓▒▓\033[0;37m  \033[0;97m▀\033[0;97;46m▓▓▒▓▓▒▓\033[0;37m  \033[0;97m▀\033[0;97;46m▓▒▓\033[0;97m▌\033[0;37m    \033[0;97m▐\033[0;97;46m▒▓\033[0;37m   \033[0;97m▀\033[0;97;46m▓▒▓\033[0;37m \033[0;97;46m▓▒▓\033[0;37m  \033[0;97m▀\033[0;97;46m▓▒▓\033[0;97m▌\033[0;97;46m▓▒▓\033[0;97m▀▀\033[0;97;46m▓▒▓\033[0;97m▌▀\033[0;97;46m▓▒▓▓▒▓\033[0;37m  \033[0;97m▀\033[0;97;46m▓▒▓\033[0;97m▌▐\033[0;97;46m▒▓\033[0;37m    \033[0;97;46m▓▒▓\033[0;36m▌\033[0;37m \033[0;97;46m▓▒▓\033[0;37m   \033[0;97m▐\033[0;97;46m▒▓\033[0;37m   \033[0;97m▀\033[0;97;46m▓▒▓\033[0;37m \033[0;97m▐\033[0;97;46m▓▓\033[0;97m▄\033[0;37m      \033[0m")
    print("\033[0;97;46m▒░▒\033[0;37m   \033[0;36m▐\033[0;97;46m▒░▒\033[0;37m \033[0;97;46m▒░▒\033[0;37m   \033[0;97;46m▒░▒\033[0;36m▌\033[0;37m   \033[0;97;46m▒░\033[0;36m▌\033[0;97;46m▒░▒\033[0;36m▌\033[0;37m   \033[0;36m▐\033[0;97;46m░▒\033[0;96m▌\033[0;37m \033[0;97;46m▒░▒\033[0;37m \033[0;97;46m▒░▒\033[0;37m   \033[0;97;46m▒░▒\033[0;36m▄▄▄\033[0;97;46m▒\033[0;36m▀▀\033[0;37m \033[0;36m▐\033[0;97;46m░▒\033[0;37m   \033[0;36m▐\033[0;97;46m▒░▒\033[0;37m    \033[0;97;46m▒░▒\033[0;37m   \033[0;36m▀\033[0;97;46m▒░▒▒░▒\033[0;36m▄▄▄\033[0;97;46m▒\033[0;36m▀▀\033[0;37m     \033[0;97;46m▒░▒\033[0;36m▌\033[0;37m   \033[0;36m▐\033[0;97;46m░▒\033[0;36m▌\033[0;97;46m▒░▒\033[0;36m▄▄▄\033[0;97;46m▒\033[0;36m▀▀\033[0;37m \033[0;97;46m▒░▒\033[0;37m  \033[0;36m▐\033[0;97;46m▒░▒\033[0;37m \033[0;97;46m▒░▒▒░▒\033[0;37m   \033[0;36m▀▀\033[0;37m  \033[0;97;46m▒░▒\033[0;36m▌\033[0;37m   \033[0;36m▐\033[0;97;46m░▒\033[0;96m▌\033[0;37m \033[0;97;46m▒░▒\033[0;37m   \033[0;97;46m▒░▒\033[0;36m▌\033[0;37m   \033[0;36m▐\033[0;97;46m░▒\033[0;36m▌\033[0;37m \033[0;36m▀\033[0;97;46m▒▒▒▒▒▒▒\033[0;36m▄\033[0m")
    print("\033[0;97;46m░ ░\033[0;37m \033[0;36m▄▀\033[0;37m \033[0;97;46m░ ░\033[0;37m \033[0;36m▐\033[0;36;46m \033[0;97;46m░\033[0;36m▄\033[0;37m  \033[0;36m▐\033[0;97;46m ░\033[0;37m  \033[0;36m▄▄\033[0;97;46m░\033[0;36;46m \033[0;36m▌▀█\033[0;97;46m░░\033[0;36m▄\033[0;37m  \033[0;97;46m░\033[0;96;46m▀░\033[0;37m  \033[0;97;46m░ ░\033[0;37m \033[0;36m▐\033[0;36;46m \033[0;97;46m░\033[0;36m▄\033[0;37m  \033[0;36m▐\033[0;36;46m \033[0;97;46m░\033[0;36m▄\033[0;37m    \033[0;36m▄▌▐\033[0;36;46m \033[0;97;46m░\033[0;37m           \033[0;36m▐\033[0;36;46m \033[0;97;46m░\033[0;36m▄\033[0;37m   \033[0;97;46m░ ░\033[0;36m▐\033[0;36;46m \033[0;97;46m░\033[0;36m▄\033[0;37m    \033[0;36m▄▌\033[0;37m     \033[0;36m▀\033[0;97;46m░░\033[0;36m▄\033[0;37m  \033[0;97;46m░ \033[0;36m▀\033[0;37m \033[0;36m▐\033[0;36;46m \033[0;97;46m░\033[0;36m▄\033[0;37m    \033[0;36m▄▌\033[0;97;46m░ ░\033[0;37m   \033[0;97;46m░ ░\033[0;37m \033[0;97;46m░ ░\033[0;36m▐\033[0;36;46m \033[0;97;46m░\033[0;36m▄\033[0;37m    \033[0;36m▄▌▀█\033[0;97;46m░░\033[0;36m▄\033[0;37m  \033[0;97;46m░\033[0;96;46m▀░\033[0;37m  \033[0;36m▐\033[0;36;46m \033[0;97;46m░\033[0;36m▄\033[0;37m   \033[0;36m▀\033[0;97;46m░░\033[0;36m▄\033[0;37m  \033[0;97;46m░ \033[0;36m▀\033[0;37m  \033[0;36m▄\033[0;37m  \033[0;36m▀▀▀\033[0;97;46m░░\033[0;36m▌\033[0m")
    print("\033[0;36m▀\033[0;36;46m  \033[0;36m▀\033[0;37m   \033[0;36;46m \033[0;36m▀\033[0;37m   \033[0;36m▀\033[0;36;46m   \033[0;36m▀\033[0;37m \033[0;36m▀\033[0;36;46m   \033[0;36m▀▀\033[0;36;46m   \033[0;37m  \033[0;36m▀███\033[0;96;46m░▒\033[0;36m▀\033[0;37m   \033[0;36;46m   \033[0;37m  \033[0;36m▀\033[0;36;46m   \033[0;36m▀\033[0;37m \033[0;36m▀\033[0;36;46m     \033[0;36m▀▀\033[0;37m \033[0;36m▐\033[0;36;46m  \033[0;37m            \033[0;36m▀\033[0;36;46m        \033[0;37m \033[0;36m▀\033[0;36;46m     \033[0;36m▀▀\033[0;37m        \033[0;36m ▀▀\033[0;36;46m \033[0;36m▀\033[0;37m    \033[0;36m▀\033[0;36;46m     \033[0;36m▀▀\033[0;37m \033[0;36;46m   \033[0;37m   \033[0;36;46m   \033[0;37m \033[0;36;46m   \033[0;37m \033[0;36m▀\033[0;36;46m     \033[0;36m▀▀\033[0;37m   \033[0;36m▀███\033[0;96;46m░▒\033[0;36m▀\033[0;37m    \033[0;36m▀\033[0;36;46m   \033[0;36m▀\033[0;37m    \033[0;36m▀▀\033[0;36;46m \033[0;36m▀\033[0;37m   \033[0;36m▀▀\033[0;36;46m      \033[0;36m▀\033[0;37m \033[0m")
    print("\033[0;37m              \033[0;36m▀\033[0;37m         \033[0;36;46m   \033[0;37m                   \033[0;36m▀\033[0;37m                                                                            \033[0;36m▐\033[0;36;46m  \033[0;36m▀\033[0;37m                             \033[0;36m▀\033[0;37m                       \033[0m")
    print("\033[0;37m                        \033[0;36;46m   \033[0;37m                                                                                                \033[0;36;46m \033[0;36m▀\033[0;37m                                                       \033[0m")
    print("\033[0;37m                        \033[0;36m▀\033[0;37m                                                                                                 \033[0;36m▀\033[0;37m                                                         \033[0m")

    print('')
    print(Back.WHITE + Fore.BLUE + Style.BRIGHT + '¡Bienvenido/a al sistema de alquiler de vehículos!')
    print('')
    print(Fore.CYAN + '1. Añadir vehículo')
    print(Fore.GREEN + '2. Listar vehículos')
    print(Fore.MAGENTA + '3. Reservar un vehículo')
    print(Fore.YELLOW + '4. Consultar el historial de reservas')
    print(Fore.BLUE + '5. Salir')
    print('')


    try:
        opcion = int(input(Fore.WHITE + 'Seleccione una opción (1, 2, 3, 4 o 5): '))
        print('')

    except ValueError:
        print(Fore.RED + 'Error. Introduce una opción válida (numero de la opción)')
        print('')
        input('Pulsa ENTER para volver al menú principal')  
        continue
    
    if opcion == 1:
        pregunta_vehiculo = input(Fore.CYAN + '¿Qué vehículo desea añadir (coche o moto)? ')
        

        if pregunta_vehiculo.lower() == 'coche':
            tipo = 'Coche'
        
        elif pregunta_vehiculo.lower() == 'moto':
            tipo = 'Moto'
        
        else:
            print(Fore.RED + 'Error. Tipo de vehículo no válido')
            print('')
            input('Pulsa ENTER para volver al menú principal')  
            continue

        pregunta_matricula = input(Fore.CYAN + 'Introduzca la matrícula: ')
        pregunta_modelo = input(Fore.CYAN + '¿Cuál es el modelo? ')

        resultado = gestor.añadir_vehiculo(tipo, pregunta_matricula, pregunta_modelo)

        if resultado == True:
            print('')
            print(Back.GREEN + Style.BRIGHT + '¡Vehículo añadido correctamente!')
            print('')
        
        else:
            print('')
            print(Back.RED + Style.BRIGHT + 'Error. Esta matrícula ya existe')
            print('')
        
        input('Pulsa ENTER para volver al menú principal')  


    elif opcion == 2:
        lista_vehiculos = gestor.listar_vehiculos()

        if len(lista_vehiculos) != 0:
            print(Fore.GREEN + '========= LISTADO DE VEHÍCULOS =========')
            
            for vehiculo in lista_vehiculos:
                print('Tipo: ', type(vehiculo).__name__)
                print('Matrícula: ', vehiculo.matricula)
                print('Modelo: ', vehiculo.modelo)
                print('-------------------------------')

            print(Fore.GREEN + '========================================')
            print('')

        else:
            print(Back.YELLOW + Style.BRIGHT + 'No hay ningún vehículo registrado')
            print('')
        
        input('Pulsa ENTER para volver al menú principal')
    

    elif opcion == 3:
        pregunta_matricula = input(Fore.CYAN + 'Introduzca la matrícula del vehículo: ')
        pregunta_fecha = input(Fore.CYAN + 'Introduzca la fecha de reserva (AAAA-MM-DD): ')
        resultado = gestor.reservar_vehiculo(pregunta_matricula, pregunta_fecha)

        if resultado == True:
            print('')
            print(Back.GREEN + Style.BRIGHT + '¡Reserva realizada correctamente!')
            print('')
        
        else:
            print('')
            print(Back.RED + Style.BRIGHT + 'Error. No se pudo realizar la reserva')
            print('')
            print(Fore.YELLOW + 'Compruebe la disponibilidad del vehículo, la fecha y la matrícula')
            print('')
        
        input('Pulsa ENTER para volver al menú principal')
    

    elif opcion == 4:

        lista_reservas = gestor.listar_reservas()

        if len(lista_reservas) != 0:
            print(Fore.GREEN + '========= LISTADO DE RESERVAS =========')
            
            for reserva in lista_reservas:
                print('Matrícula: ', reserva[0])
                print('Fecha: ', reserva[1])
                print('-------------------------------')

            print(Fore.GREEN + '========================================')
            print('')

        else:
            print(Back.YELLOW + Style.BRIGHT + 'No hay ninguna reserva registrada')
            print('')
        
        input('Pulsa ENTER para volver al menú principal')



    elif opcion == 5:
        print(Fore.GREEN + Style.BRIGHT + 'El programa se ha cerrado correctamente')
        print('')
        break
    

    else:
        print(Fore.RED + Style.BRIGHT + 'Opción no encontrada. Introduce una opcion valida')
        print('')
        input('Pulsa ENTER para volver al menú principal')
