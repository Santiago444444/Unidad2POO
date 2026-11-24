class ControladorTours:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                self._registrar_tour()
            elif opcion == "2":
                self._mostrar_tours()
            elif opcion == "3":
                self._reservar_cupos()
            elif opcion == "4":
                self.vista.mostrar_mensaje("Fuera")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida.")

    def _registrar_tour(self):
        try:
            nombre, precio, cupos = self.vista.pedir_datos_tour()
            nuevo_tour = self.modelo.registrar(nombre, precio, cupos)
            self.vista.mostrar_mensaje(f"Registrado con el código {nuevo_tour.codigo}.")
        except ValueError as e:
            self.vista.mostrar_mensaje(str(e))

    def _mostrar_tours(self):
        tours = self.modelo.obtener_todos()
        self.vista.mostrar_tours(tours)

    def _reservar_cupos(self):
        try:
            codigo = self.vista.pedir_codigo()
            tour = self.modelo.buscar(codigo)
            if tour is None:
                raise ValueError("Error: no existe ese código.")

            cantidad = self.vista.pedir_cantidad()
            tour = self.modelo.reservar_cupos(codigo, cantidad)
            self.vista.mostrar_mensaje(f"Listo. Quedan {tour.cupos} cupos.")
        except ValueError as e:
            self.vista.mostrar_mensaje(str(e))