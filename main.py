from modelo import GestorTours
from vista import VistaTours
from controlador import ControladorTours


def main():
    modelo = GestorTours()
    vista = VistaTours()
    controlador = ControladorTours(modelo, vista)



if __name__ == "__main__":
    main()