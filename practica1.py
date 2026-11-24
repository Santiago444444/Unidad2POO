class Tour:
    def __init__(self, codigo, nombre, precio, cupos):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cupos = cupos

    def reservar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
            return False
        if cantidad > self.cupos:
            print(f"Solo hay {self.cupos} cupos.")
            return False
        self.cupos -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8} {self.nombre:<20} ${self.precio:>7.2f} {self.cupos:>8}"


def buscar_tour(tours, codigo):
    for t in tours:
        if t.codigo == codigo:
            return t
    return None


def main():
    tours = [
        Tour(1, "Centro histórico", 15.00, 20),
        Tour(2, "El Cajas", 35.00, 12),
    ]

    while True:
        print("\n--- Tours Cuenca Colonial ---")
        print("1. Registrar tour")
        print("2. Mostrar tours")
        print("3. Reservar cupos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del tour: ")
            try:
                precio = float(input("Precio: "))
                cupos = int(input("Cupos: "))
            except ValueError:
                print("Error: precio y cupos deben ser valores numéricos.")
                continue

            codigo = len(tours) + 1
            nuevo_tour = Tour(codigo, nombre, precio, cupos)
            tours.append(nuevo_tour)
            print(f"Registrado con el código {codigo}.")

        elif opcion == "2":
            print(f"\n{'Código':<8} {'Nombre':<20} {'Precio':>8} {'Cupos':>8}")
            print("-" * 47)
            for t in tours:
                print(t)

        elif opcion == "3":
            try:
                codigo = int(input("Código del tour: "))
            except ValueError:
                print("Error: el código debe ser un número entero.")
                continue

            tour_encontrado = buscar_tour(tours, codigo)
            if tour_encontrado is None:
                print("Error: no existe ese código.")
                continue

            try:
                cantidad = int(input("Cantidad de cupos a reservar: "))
            except ValueError:
                print("Error: la cantidad debe ser un número entero.")
                continue

            if tour_encontrado.reservar(cantidad):
                print(f"Listo. Quedan {tour_encontrado.cupos} cupos.")

        elif opcion == "4":
            print("Fuera")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()