class Automovil:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__encendido = False
        self.__velocidad = 0

    # Getters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_año(self):
        return self.__año

    def get_encendido(self):
        return self.__encendido

    def get_velocidad(self):
        return self.__velocidad

    # Setters
    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_año(self, año):
        self.__año = año

    # Métodos del auto
    def arrancar(self):
        if not self.__encendido:
            self.__encendido = True
            print(f"{self.__marca} {self.__modelo} arrancó.")
        else:
            print(f"{self.__marca} {self.__modelo} ya estaba encendido.")

    def frenar(self):
        if self.__velocidad > 0:
            self.__velocidad = 0
            print(f"{self.__marca} {self.__modelo} frenó.")
        else:
            print(f"{self.__marca} {self.__modelo} ya está detenido.")

    def acelerar(self, velocidad):
        if self.__encendido:
            self.__velocidad += velocidad
            print(f"{self.__marca} {self.__modelo} aceleró a {self.__velocidad} km/h.")
        else:
            print(f"Primero debes arrancar el {self.__marca} {self.__modelo}.")

    def mostrar(self):
        estado = "encendido" if self.__encendido else "apagado"
        print(f"{self.__marca} {self.__modelo} ({self.__año}) - {estado} - Velocidad: {self.__velocidad} km/h")


# -------------------------
# Programa principal
# -------------------------

# Lista estática de tamaño fijo
autos = [None]*3

# Crear autos
autos[0] = Automovil("Toyota", "Corolla", 2020)
autos[1] = Automovil("Honda", "Civic", 2019)
autos[2] = Automovil("Ford", "Focus", 2021)

# Mostrar autos
print("Lista de autos:")
for auto in autos:
    auto.mostrar()

# Probar métodos
print("\nPrueba de métodos:")
autos[0].arrancar()
autos[0].acelerar(50)
autos[0].frenar()
autos[0].mostrar()
