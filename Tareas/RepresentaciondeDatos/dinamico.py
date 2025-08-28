# Clase Estudiante
class Estudiante:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

    def mostrar_estudiante(self):
        print(f"ID: {self.id} | Nombre: {self.nombre} | Edad: {self.edad}")


# Clase Registro: usa lista dinámica
class Registro:
    def __init__(self):
        self.estudiantes = []  # lista dinámica

    # Añadir estudiante
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"\n✅ Estudiante '{estudiante.nombre}' añadido al registro.")

    # Mostrar todos los estudiantes
    def mostrar_registro(self):
        print("\n--- Registro de Estudiantes ---")
        if not self.estudiantes:
            print("El registro está vacío.")
        else:
            for est in self.estudiantes:
                est.mostrar_estudiante()

    # Buscar estudiante por ID
    def buscar_estudiante(self, id):
        for est in self.estudiantes:
            if est.id == id:
                print("\n🔎 Estudiante encontrado:")
                est.mostrar_estudiante()
                return
        print(f"\n❌ No se encontró un estudiante con ID {id}.")

    # Eliminar estudiante por ID
    def eliminar_estudiante(self, id):
        for est in self.estudiantes:
            if est.id == id:
                self.estudiantes.remove(est)
                print(f"\n🗑 Estudiante con ID {id} eliminado.")
                return
        print(f"\n❌ No se encontró un estudiante con ID {id}.")


# Programa principal con menú
if __name__ == "__main__":
    registro = Registro()

    while True:
        print("\n===== MENÚ DEL REGISTRO DE ESTUDIANTES =====")
        print("1. Añadir estudiante")
        print("2. Mostrar registro")
        print("3. Buscar estudiante por ID")
        print("4. Eliminar estudiante por ID")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                id = int(input("Ingrese ID del estudiante: "))
                nombre = input("Ingrese nombre del estudiante: ")
                edad = int(input("Ingrese edad del estudiante: "))
                nuevo = Estudiante(id, nombre, edad)
                registro.agregar_estudiante(nuevo)
            except ValueError:
                print("⚠ Entrada inválida. Intente de nuevo.")

        elif opcion == "2":
            registro.mostrar_registro()

        elif opcion == "3":
            try:
                id = int(input("Ingrese ID del estudiante a buscar: "))
                registro.buscar_estudiante(id)
            except ValueError:
                print("⚠ Entrada inválida. Intente de nuevo.")

        elif opcion == "4":
            try:
                id = int(input("Ingrese ID del estudiante a eliminar: "))
                registro.eliminar_estudiante(id)
            except ValueError:
                print("⚠ Entrada inválida. Intente de nuevo.")

        elif opcion == "5":
            print("\n👋 Saliendo del programa...")
            break

        else:
            print("⚠ Opción no válida. Intente de nuevo.")
