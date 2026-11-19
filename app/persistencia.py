from .vehiculos import Coche, Moto

def guardar_vehiculos(lista_vehiculos):
    """Guarda el listado de vehículos en el archivo vehículos.txt."""
    with open('vehiculos.txt', 'w', encoding='utf-8') as f:
        for vehiculo in lista_vehiculos:
            tipo = type(vehiculo).__name__
            matricula = vehiculo.matricula
            modelo = vehiculo.modelo
            f.write(f'{tipo}, {matricula}, {modelo}\n')



def cargar_vehiculos():
    """Carga los vehículos guardados en el archivo vehículos.txt."""
    lista_vehiculos = []

    try:
        with open('vehiculos.txt', 'r', encoding='utf-8') as f:
            for linea in f:
                datos = linea.strip().split(',')
                if len(datos) != 3:
                    continue

                tipo = datos[0].strip()
                matricula = datos[1].strip()
                modelo = datos[2].strip()

                if tipo == 'Coche':
                    vehiculo = Coche(matricula, modelo)
                    
                elif tipo == 'Moto':
                    vehiculo = Moto(matricula, modelo)
                    
                else:
                    continue
                    
                lista_vehiculos.append(vehiculo)
        
    except FileNotFoundError:
        pass
        
    return lista_vehiculos


def guardar_reservas(lista_reservas):
    """Guarda el listado de reservas en el archivo reservas.txt."""
    with open('reservas.txt', 'w', encoding='utf-8') as f:
        for reserva in lista_reservas:
            matricula = reserva[0]
            fecha = reserva[1]
            f.write(f'{matricula}, {fecha}\n')


def cargar_reservas():
    """Carga las reservas guardadas en el archivo reservas.txt."""
    lista_reservas = []

    try:
        with open('reservas.txt', 'r', encoding='utf-8') as f:
            for linea in f:
                datos = linea.strip().split(',')
                if len(datos) != 2:
                    continue

                matricula = datos[0].strip()
                fecha = datos[1].strip()
                lista_reservas.append([matricula, fecha])

    except FileNotFoundError:
        pass
        
    return lista_reservas









