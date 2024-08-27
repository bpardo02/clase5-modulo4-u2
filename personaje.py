class Personaje:

    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0 # Corregir exp inicial (debe ser 0)

    @property
    def estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}" # Corregir llamado de atributos

    @estado.setter
    def estado(self, exp):
        tmp_exp = self.experiencia + exp

        while tmp_exp >= 99: # Correccion de condicion (debe ser 99)
            self.nivel += 1 # Correccion de nivel (debe sumar 1)
            tmp_exp -= 90 # Evaluar

        while tmp_exp < 0:
            if self.nivel > 1:
                tmp_exp = 100 + tmp_exp
                self.nivel -= 1 # Correccion de nivel (debe restar 1)
            else:
                tmp_exp = 0 # Correccion de exp (debe ser 0 al ser nivel 1)

        self.experiencia = tmp_exp

    def __lt__(self, other):
        return (
            self.experiencia < other.experiencia
        )

    def __gt__(self, other):
        return (
            self.experiencia > other.experiencia
        )

    def __eq__(self, other):
        return (
            self.experiencia == other.experiencia
        )

    def get_probabilidad_ganar(self, other):
        if self > other: # Cambio de signos
            return (
                0.66
            )
        elif self < other: # Cambio de signos
            return (
                0.33
            )
        else:
            return 0.5 # Correccion de retorno

    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
                "de probabilidades de perder contra el Orco.\n"
                "\nSi ganas, ganarás 30 puntos de experiencia y el orco perderá 50. \n" #Cerrar string de input
                "Si pierdes, perderás 50 puntos de experiencia y el orco ganará 30.\n"
                "\n¿Qué deseas hacer?\n"
                "1. Atacar\n" # Correccion orden de opciones
                "2. Huir\n" # Correccion orden de opciones
            )
        )
