import pytest
from ElEstudiante.src.Curso import Curso
from ElEstudiante.src.Departamento import Departamento

class TestCurso:
    # -----------------------------------------------------------------
    # Atributos
    # -----------------------------------------------------------------

    curso = None

    # -----------------------------------------------------------------
    # Métodos
    # -----------------------------------------------------------------

    def setup_method(self):
        """
        Escenario 1: Construye un curso sin nota.
        """
        self.curso = Curso("COD", "Nombre", 3, Departamento.SISTEMAS)

    def test_curso(self):
        """
        Prueba 1: Verifica el método constructor.

        Métodos a probar:
        - Curso
        - dar_codigo
        - dar_nombre
        - dar_creditos
        - dar_departamento
        - dar_nota

        Casos de prueba:
        1. Los valores de los atributos corresponden.
        """
        assert self.curso.dar_codigo() == "COD", "El código no corresponde."
        assert self.curso.dar_nombre() == "Nombre", "El nombre no corresponde."
        assert self.curso.dar_creditos() == 3, "Los créditos no corresponden."
        assert self.curso.dar_nota() == 0.0, "La nota no corresponde."
        assert self.curso.dar_departamento() == Departamento.SISTEMAS, "El departamento no corresponde."

    def test_asignar_nota(self):
        """
        Prueba 2: Verifica el método asignar_nota.

        Métodos a probar:
        - asignar_nota
        - dar_nota

        Casos de prueba:
        1. El curso no tiene nota.
        """
        self.curso.asignar_nota(4.5)
        assert self.curso.dar_nota() == 4.5, "La nota no corresponde."

    def test_esta_calificado(self):
        """
        Prueba 3: Verifica el método esta_calificado.

        Métodos a probar:
        - asignar_nota
        - esta_calificado

        Casos de prueba:
        1. El curso no tiene nota.
        2. El curso tiene nota.
        """
        assert not self.curso.esta_calificado(), "El curso no debería tener nota."
        self.curso.asignar_nota(4.5)
        assert self.curso.esta_calificado(), "El curso debería tener nota."
