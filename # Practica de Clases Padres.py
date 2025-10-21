# Practica de Clases Padres.py

# Clase padre
class Espadachin:
    def __init__(self, nombre, nivel, fuerza):
        self.nombre = nombre
        self.nivel = nivel
        self.fuerza = fuerza

    def atacar(self):
        print(f"{self.nombre} ataca con su espada con fuerza {self.fuerza}.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} | Nivel: {self.nivel} | Fuerza: {self.fuerza}")


# Clase hija 1
class EspadachinDelVacio(Espadachin):
    def __init__(self, nombre, nivel, fuerza, elemento='Sombra'):
        super().__init__(nombre, nivel, fuerza)
        self.elemento = elemento

    def ataque_especial(self):
        print(f"{self.nombre} lanza una tormenta de oscuridad con su espada.")


# Clase hija 2
class EspadachinDeRayo(Espadachin):
    def __init__(self, nombre, nivel, fuerza, elemento='Rayo'):
        super().__init__(nombre, nivel, fuerza)
        self.elemento = elemento

    def ataque_especial(self):
        print(f"{self.nombre} lanza una tormenta eléctrica con su espada.")


if __name__ == "__main__":
    # Creación de objetos (instancias)
    sombra = EspadachinDelVacio("Grimaa", 19, 100)
    rayo = EspadachinDeRayo("Pelagato", 10, 50)

    # Mostrar información
    print("\n--- Información de los espadachines ---")
    sombra.mostrar_info()
    rayo.mostrar_info()

    # Ejecución de métodos heredados y propios
    print("\n--- Ataques ---")
    sombra.atacar()
    sombra.ataque_especial()

    print()
    rayo.atacar()
    rayo.ataque_especial()