class Vehiculo:
    """Representa un vehículo de nuestro sistema de alquiler"""
    def __init__(self, matricula, modelo):
        """Inicializa un vehículo con los parámetros de matrícula y modelo"""
        self.__matricula = matricula
        self.__modelo = modelo
    
    @property
    def matricula(self):
        """Devuelve la matrícula del vehículo"""
        return self.__matricula
    
    @property
    def modelo(self):
        """Devuelve el modelo del vehículo"""
        return self.__modelo


class Coche(Vehiculo):
    """Representa un coche que forma parte del sistema de alquiler (flota)"""
    def __init__(self, matricula, modelo):
        """Inicializa un coche utilizando la clase genérica de Vehículo"""
        super().__init__(matricula, modelo)


class Moto(Vehiculo):
    """Representa una moto que forma parte del sistema de alquiler (flota)"""
    def __init__(self, matricula, modelo):
        """Inicializa una moto utilizando la clase genérica de Vehículo"""
        super().__init__(matricula, modelo)


