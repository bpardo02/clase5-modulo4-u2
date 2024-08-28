class Personaje:
   """  
    Clase que representa un personaje en el juego de texto interactivo.  

    A través de esta clase, se gestionan las interacciones entre personajes y se   
    administran sus niveles de experiencia y decisiones en combate.   

    Atributos:  
    - nombre (str): El nombre del personaje.  
    - nivel (int): El nivel del personaje, inicializado en 1.  
    - experiencia (int): La experiencia del personaje, inicializada en 0.  

    Métodos:  
    - estado: Propiedad que devuelve un string con el estado actual del personaje.  
    - __lt__(self, other): Compara la experiencia con otro personaje (menor).  
    - __gt__(self, other): Compara la experiencia con otro personaje (mayor).  
    - __eq__(self, other): Compara la experiencia con otro personaje (igual).  
    - get_probabilidad_ganar(self, other): Calcula la probabilidad de ganar contra otro personaje.  
    - mostrar_dialogo_opcion(probabilidad_ganar): Muestra opciones al jugador para atacar o huir.  
    """
    def __init__(self, nombre):
        """  
        Inicializa un nuevo personaje.  

        Este método establece el nombre del personaje y asigna los valores   
        iniciales para el nivel y la experiencia.  

        Args:  
            nombre (str): El nombre del personaje.  
        """
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0 # Corregir exp inicial (debe ser 0)

    @property
    def estado(self):
        """  
        Devuelve el estado actual del personaje.  

        Returns:  
            str: Un string que representa el nombre, nivel y experiencia del personaje.  
        """
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}" # Corregir llamado de atributos

    @estado.setter
    def estado(self, exp):
       """  
        Actualiza la experiencia del personaje y ajusta el nivel si es necesario.  

        Este método se encarga de incrementar o decrementar la experiencia.   
        Si la experiencia alcanza el umbral requerido, el nivel se ajusta   
        correspondientemente.  

        Args:  
            exp (int): La cantidad de experiencia a agregar o restar.  
        """
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
        """  
        Compara si este personaje tiene menos experiencia que otro.  

        Args:  
            other (Personaje): Otro personaje a comparar.  

        Returns:  
            bool: True si este personaje tiene menos experiencia, False en caso contrario.  
        """
        return (
            self.experiencia < other.experiencia
        )

    def __gt__(self, other):
        """  
        Compara si este personaje tiene más experiencia que otro.  

        Args:  
            other (Personaje): Otro personaje a comparar.  

        Returns:  
            bool: True si este personaje tiene más experiencia, False en caso contrario.  
        """
        return (
            self.experiencia > other.experiencia
        )

    def __eq__(self, other):
        """  
        Compara si este personaje tiene la misma experiencia que otro.  

        Args:  
            other (Personaje): Otro personaje a comparar.  

        Returns:  
            bool: True si ambos personajes tienen la misma experiencia, False en caso contrario.  
        """
        return (
            self.experiencia == other.experiencia
        )

    def get_probabilidad_ganar(self, other):
        """  
        Calcula la probabilidad de ganar contra otro personaje.  

        Args:  
            other (Personaje): El personaje enemigo.  

        Returns:  
            float: La probabilidad de ganar (entre 0 y 1).  
        """
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
        """  
        Muestra opciones al jugador para atacar o huir en base a la probabilidad de ganar.  

        Esta función solicita al jugador que elija entre atacar al enemigo o huir.   
        La probabilidad de ganar también se presenta para ayudar en la toma de decisiones.  

        Args:  
            probabilidad_ganar (float): La probabilidad de ganar contra el enemigo.  

        Returns:  
            int: La opción elegida por el jugador (1 para atacar, 2 para huir).  
        """ 
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
