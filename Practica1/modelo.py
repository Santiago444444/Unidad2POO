class Tour:
    def __init__(self, codigo, nombre, precio, cupos):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cupos = cupos
        self.validar()

    def validar(self):
        self.nombre = self.nombre.strip()
        if self.nombre == "":
            raise ValueError("Error: el nombre del tour no puede estar vacío.")
        if self.precio <= 0:
            raise ValueError("Error: el precio debe ser mayor que 0.")
        if self.cupos < 0:
            raise ValueError("Error: los cupos deben ser mayores o iguales a 0.")

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
        self.tours = []
        self.siguiente_codigo = 1
        self.cargar_datos()

    def cargar_datos(self):
        self.registrar("Centro histórico", 15.00, 20)
        self.registrar("El Cajas", 35.00, 12)

    def registrar(self, nombre, precio, cupos):
        nuevo_tour = Tour(self.siguiente_codigo, nombre, precio, cupos)
        self.tours.append(nuevo_tour)
        self.siguiente_codigo += 1
        return nuevo_tour

    def buscar(self, codigo):
        for t in self.tours:
            if t.codigo == codigo:
                return t
        raise ValueError("Error: no existe ese código.")

    def reservar_cupos(self, codigo, cantidad):
        tour = self.buscar(codigo)
        tour.reservar(cantidad)
        return tour

    def obtener_todos(self):
        return self.tours