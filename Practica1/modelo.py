class Tour:
    def __init__(self, codigo, nombre, precio, cupos):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cupos = cupos
        self.validar()

    def validar(self):
        if not self.nombre or not self.nombre.strip():
            raise ValueError("Error: el nombre del tour no puede estar vacío.")
        if self.precio <= 0:
            raise ValueError("Error: el precio debe ser mayor que 0.")
        if self.cupos <= 0:
            raise ValueError("Error: los cupos deben ser mayores que 0.")

    def reservar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        if cantidad > self.cupos:
            raise ValueError(f"Solo hay {self.cupos} cupos.")
        self.cupos -= cantidad

    def __str__(self):
        return f"{self.codigo:<8} {self.nombre:<20} ${self.precio:>7.2f} {self.cupos:>8}"


class GestorTours:
    def __init__(self):
        self.tours = [
            Tour(1, "Centro histórico", 15.00, 20),
            Tour(2, "El Cajas", 35.00, 12),
        ]

    def obtener_todos(self):
        return self.tours

    def registrar(self, nombre, precio, cupos):
        try:
            precio = float(precio)
            cupos = int(cupos)
        except ValueError:
            raise ValueError("Error: precio y cupos deben ser valores numéricos.")

        codigo = len(self.tours) + 1
        nuevo_tour = Tour(codigo, nombre, precio, cupos)
        self.tours.append(nuevo_tour)
        return nuevo_tour

    def buscar(self, codigo):
        try:
            codigo = int(codigo)
        except ValueError:
            raise ValueError("Error: el código debe ser un número entero.")

        for t in self.tours:
            if t.codigo == codigo:
                return t
        return None

    def reservar_cupos(self, codigo, cantidad):
        tour = self.buscar(codigo)
        if tour is None:
            raise ValueError("Error: no existe ese código.")

        try:
            cantidad = int(cantidad)
        except ValueError:
            raise ValueError("Error: la cantidad debe ser un número entero.")

        tour.reservar(cantidad)
        return tour