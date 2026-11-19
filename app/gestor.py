from . import persistencia
from .vehiculos import Coche, Moto
from datetime import datetime

class GestorSistema:
    """Gestiona las reservas y los vehículos del sistema"""
    def __init__(self):
        """Inicia el gestor del sistema cargando los vehículos y las reservas ya guardadas"""
        self.vehiculos = persistencia.cargar_vehiculos()
        self.reservas = persistencia.cargar_reservas()

    
    def añadir_vehiculo(self, tipo, matricula, modelo):
        """Añade un vehículo nuevo en el sistema (flota) si su matrícula no existe aun."""
        matricula = matricula.strip().upper()

        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                return False
        
        if tipo == 'Coche':
            vehiculo = Coche(matricula, modelo)
                    
        elif tipo == 'Moto':
            vehiculo = Moto(matricula, modelo)
                    
        else:
            return False
        

        self.vehiculos.append(vehiculo)
        persistencia.guardar_vehiculos(self.vehiculos)

        return True
    

    def listar_vehiculos(self):
        """Devuelve la lista completa de vehículos disponibles en el sistema."""
        return self.vehiculos
    

    def reservar_vehiculo(self, matricula, fecha):
        """Reserva un vehículo para una fecha concreta, en caso de estar disponible."""
        matricula = matricula.strip().upper()

        try:
            datetime.strptime(fecha, '%Y-%m-%d')
        
        except ValueError:
            return False
        
        disponibilidad = False

        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                disponibilidad = True
                break
        
        if not disponibilidad:
            return False
        
        for reserva in self.reservas:
            if reserva[0] == matricula and reserva[1] == fecha:
                return False
        

        self.reservas.append([matricula, fecha])
        persistencia.guardar_reservas(self.reservas)

        return True


    def listar_reservas(self):
        """Devuelve el historial completo de reservas realizadas en el sistema."""
        return self.reservas