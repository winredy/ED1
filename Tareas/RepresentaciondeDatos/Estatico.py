# Clase Producto: representa un producto de una tienda
class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    # Método para mostrar la información del producto
    def mostrar_producto(self):
        print(f"ID: {self.id} | {self.nombre} | ${self.precio:.2f}")


# Clase Catálogo: con representación estática (lista fija)
class Catalogo:
    def __init__(self, capacidad):
        self.productos = [None] * capacidad  # lista estática
        self.capacidad = capacidad
        self.total = 0  # cantidad actual de productos

    # Método para añadir un nuevo producto
    def agregar_producto(self, producto):
        if self.total < self.capacidad:
            self.productos[self.total] = producto
            self.total += 1
            print(f"\n✅ Producto '{producto.nombre}' añadido al catálogo.")
        else:
            print("\n⚠ El catálogo está lleno, no se pueden añadir más productos.")

    # Método para mostrar todos los productos
    def mostrar_catalogo(self):
        print("\n--- Catálogo de Productos ---")
        if self.total == 0:
            print("El catálogo está vacío.")
        else:
            for i in range(self.total):
                self.productos[i].mostrar_producto()

    # Método para buscar un producto por su ID
    def buscar_producto(self, id):
        for i in range(self.total):
            if self.productos[i].id == id:
                print("\n🔎 Producto encontrado:")
                self.productos[i].mostrar_producto()
                return
        print(f"\n❌ No se encontró un producto con ID {id}.")


# Programa principal con menú
if __name__ == "__main__":
    catalogo = Catalogo(5)  # capacidad máxima del catálogo

    while True:
        print("\n===== MENÚ DEL CATÁLOGO =====")
        print("1. Añadir producto")
        print("2. Mostrar catálogo")
        print("3. Buscar producto por ID")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                id = int(input("Ingrese ID del producto: "))
                nombre = input("Ingrese nombre del producto: ")
                precio = float(input("Ingrese precio del producto: "))
                nuevo = Producto(id, nombre, precio)
                catalogo.agregar_producto(nuevo)
            except ValueError:
                print("⚠ Entrada inválida. Intente de nuevo.")

        elif opcion == "2":
            catalogo.mostrar_catalogo()

        elif opcion == "3":
            try:
                id = int(input("Ingrese ID del producto a buscar: "))
                catalogo.buscar_producto(id)
            except ValueError:
                print("⚠ Entrada inválida. Intente de nuevo.")

        elif opcion == "4":
            print("\n👋 Saliendo del programa...")
            break

        else:
            print("⚠ Opción no válida. Intente de nuevo.")
