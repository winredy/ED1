MAX = 5
invitados = [None] * MAX
total = 0

# Función para agregar un invitado
def agregar_invitado(nombre):
    global total
    if total < MAX:
        invitados[total] = nombre
        total += 1
        print(f"\n✅ Invitado agregado: {nombre}")
    else:
        print("\n⚠ Registro completo, no se pueden agregar más invitados")

# Función para mostrar la lista de invitados
def mostrar_invitados():
    print("\n--- Lista de Invitados ---")
    if total == 0:
        print("No hay invitados registrados.")
    else:
        for i in range(total):
            print(f"{i}. {invitados[i]}")

# Función para buscar un invitado por nombre
def buscar_invitado(nombre):
    for i in range(total):
        if invitados[i] == nombre:
            print(f"\n🔎 Invitado encontrado: {invitados[i]} en la posición {i}")
            return
    print(f"\n❌ No se encontró al invitado: {nombre}")

# Función para eliminar un invitado por índice
def eliminar_invitado(indice):
    global total
    if 0 <= indice < total:
        eliminado = invitados[indice]
        # Mover todos los elementos a la izquierda
        for i in range(indice, total - 1):
            invitados[i] = invitados[i + 1]
        invitados[total - 1] = None
        total -= 1
        print(f"\n🗑 Invitado eliminado: {eliminado}")
    else:
        print("\n⚠ Índice inválido")

# Programa principal con menú
if __name__ == "__main__":
    while True:
        print("\n===== MENÚ REGISTRO DE INVITADOS =====")
        print("1. Agregar invitado")
        print("2. Mostrar lista de invitados")
        print("3. Buscar invitado por nombre")
        print("4. Eliminar invitado por índice")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del invitado: ")
            agregar_invitado(nombre)

        elif opcion == "2":
            mostrar_invitados()

        elif opcion == "3":
            nombre = input("Ingresa el nombre del invitado a buscar: ")
            buscar_invitado(nombre)

        elif opcion == "4":
            mostrar_invitados()
            try:
                indice = int(input("Ingresa el índice del invitado a eliminar: "))
                eliminar_invitado(indice)
            except ValueError:
                print("⚠ Entrada inválida")

        elif opcion == "5":
            print("\n👋 Saliendo del programa...")
            break

        else:
            print("⚠ Opción no válida")
