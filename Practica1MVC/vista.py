class VistaTours:
    def mostrar_menu(self):
        print("\n--- Tours Cuenca Colonial ---")
        print("1. Registrar tour")
        print("2. Mostrar tours")
        print("3. Reservar cupos")
        print("4. Salir")
        return input("Seleccione una opción: ").strip()

    def pedir(self, mensaje):
        return input(mensaje)

    def mostrar_tabla(self, tours):
        print(f"\n{'Código':<8} {'Nombre':<20} {'Precio':>8} {'Cupos':>8}")
        print("-" * 47)
        for t in tours:
            print(t)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)