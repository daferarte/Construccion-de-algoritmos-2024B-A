from Departamento import Departamento

class Curso:
    

    # -----------------------------------------------------------------
    # Constantes
    # -----------------------------------------------------------------
    MINIMA = 1.5  # Nota mínima
    MAXIMA = 5.0  # Nota máxima

    # -----------------------------------------------------------------
    # Constructor
    # -----------------------------------------------------------------
    def __init__(self, codigo: str, nombre: str, creditos: int, departamento: Departamento):
        """
        Crea el curso con los valores dados por parámetro.
        La nota del curso se inicializa en 0.0.
        :param codigo: Código del curso. No puede ser nulo o vacío.
        :param nombre: Nombre del curso. No puede ser nulo o vacío.
        :param creditos: Número de créditos del curso. Debe ser mayor que 0.
        :param departamento: Departamento al que pertenece el curso.
        """
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.departamento = departamento
        self.nota = 0.0

    # -----------------------------------------------------------------
    # Métodos
    # -----------------------------------------------------------------
    def dar_codigo(self) -> str:
        """Retorna el código del curso."""
        return self.codigo

    def dar_nombre(self) -> str:
        """Retorna el nombre del curso."""
        return self.nombre

    def dar_creditos(self) -> int:
        """Retorna el número de créditos del curso."""
        return self.creditos

    def dar_nota(self) -> float:
        """Retorna la nota del curso."""
        return self.nota

    def dar_departamento(self) -> Departamento:
        """Retorna el departamento del curso."""
        return self.departamento

    def asignar_nota(self, nueva_nota: float):
        """
        Asigna la nota dada por parámetro.
        :param nueva_nota: Nueva nota del curso. Debe estar entre 1.5 y 5.0.
        """
        if self.MINIMA <= nueva_nota <= self.MAXIMA:
            self.nota = nueva_nota
        else:
            raise ValueError(f'La nota debe estar entre {self.MINIMA} y {self.MAXIMA}.')

    def esta_calificado(self) -> bool:
        """Indica si el curso ya ha sido calificado."""
        return self.nota != 0.0