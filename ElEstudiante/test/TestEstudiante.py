import pytest
from ElEstudiante.src.Estudiante import Estudiante
from ElEstudiante.src.Curso import Curso
from ElEstudiante.src.Departamento import Departamento

class TestEstudiante:

    # -----------------------------------------------------------------
    # Atributos
    # -----------------------------------------------------------------
    estudiante = None

    # -----------------------------------------------------------------
    # Métodos
    # -----------------------------------------------------------------

    def setup_method(self):
        """
        Escenario 1: Crea un nuevo estudiante sin calificaciones.
        """
        self.estudiante = Estudiante()

    def test_estudiante(self):
        """
        Prueba 1: Verifica el método constructor.

        Métodos a probar:
        - dar_nombre
        - dar_apellido
        - dar_codigo
        - dar_curso1, dar_curso2, dar_curso3, dar_curso4

        Casos de prueba:
        1. Los valores de los atributos corresponden.
        """
        assert self.estudiante.dar_nombre() == "Juliana", "El nombre no corresponde."
        assert self.estudiante.dar_apellido() == "Ramírez", "El apellido no corresponde."
        assert self.estudiante.dar_codigo() == 201612345, "El código no corresponde."
        assert self.estudiante.dar_curso1() is not None, "Debería existir el curso 1."
        assert self.estudiante.dar_curso2() is not None, "Debería existir el curso 2."
        assert self.estudiante.dar_curso3() is not None, "Debería existir el curso 3."
        assert self.estudiante.dar_curso4() is not None, "Debería existir el curso 4."

    def test_buscar_curso(self):
        """
        Prueba 2: Verifica el método buscarCurso.

        Métodos a probar:
        - buscarCurso

        Casos de prueba:
        1. El curso existe.
        2. El curso no existe.
        """
        assert self.estudiante.buscar_curso("ISIS1204") is not None, "El curso debería existir."
        assert self.estudiante.buscar_curso("ISIS1205") is None, "El curso no debería existir."

    def test_asignar_nota_curso(self):
        """
        Prueba 3: Verifica el método asignarNotaCurso.

        Métodos a probar:
        - asignarNotaCurso

        Casos de prueba:
        1. El curso no existe.
        2. El curso existe y la nota no está en el rango.
        3. El curso existe y la nota está en el rango.
        """
        assert not self.estudiante.asignar_nota_curso("ISSI1205", 3.0), "No debería asignar la nota."
        assert not self.estudiante.asignar_nota_curso("ISIS1204", 6.0), "No debería asignar la nota."
        assert self.estudiante.asignar_nota_curso("ISIS1204", 3.0), "Debería asignar la nota."

    def test_calcular_promedio_estudiante(self):
        """
        Prueba 4: Verifica el método calcularPromedioEstudiante.

        Métodos a probar:
        - calcularPromedioEstudiante
        - asignarNotaCurso

        Casos de prueba:
        1. Ningún curso tiene notas.
        2. Todos los cursos tienen notas.
        """
        assert self.estudiante.calcular_promedio_estudiante() == -1, "El promedio no corresponde."

        self.estudiante.asignar_nota_curso("ISIS1204", 4)
        self.estudiante.asignar_nota_curso("FISI1100", 3)
        self.estudiante.asignar_nota_curso("MATE1203", 5)
        self.estudiante.asignar_nota_curso("BIOL1405", 4)

        assert self.estudiante.calcular_promedio_estudiante() == pytest.approx(3.93, 0.01), "El promedio no corresponde."

    def test_esta_en_prueba(self):
        """
        Prueba 5: Verifica el método estaEnPrueba.

        Métodos a probar:
        - estaEnPrueba
        - asignarNotaCurso

        Casos de prueba:
        1. No está en prueba.
        2. Está en prueba.
        """
        self.estudiante.asignar_nota_curso("ISIS1204", 4)
        self.estudiante.asignar_nota_curso("FISI1100", 3)
        self.estudiante.asignar_nota_curso("MATE1203", 4)
        self.estudiante.asignar_nota_curso("BIOL1405", 4)
        assert not self.estudiante.esta_en_prueba(), "No debería estar en prueba."

        self.estudiante.asignar_nota_curso("ISIS1204", 2)
        self.estudiante.asignar_nota_curso("FISI1100", 3)
        self.estudiante.asignar_nota_curso("MATE1203", 2)
        self.estudiante.asignar_nota_curso("BIOL1405", 4)
        assert self.estudiante.esta_en_prueba(), "Debería estar en prueba."

    def test_es_candidato_a_beca(self):
        """
        Prueba 6: Verifica el método esCandidatoABeca.

        Métodos a probar:
        - esCandidatoABeca
        - asignarNotaCurso

        Casos de prueba:
        1. Es candidato.
        2. No es candidato.
        """
        self.estudiante.asignar_nota_curso("ISIS1204", 4.7)
        self.estudiante.asignar_nota_curso("FISI1100", 5)
        self.estudiante.asignar_nota_curso("MATE1203", 4.9)
        self.estudiante.asignar_nota_curso("BIOL1405", 4.8)
        assert self.estudiante.es_candidato_a_beca(), "Debería ser candidato a beca."

        self.estudiante.asignar_nota_curso("ISIS1204", 3)
        self.estudiante.asignar_nota_curso("FISI1100", 3)
        self.estudiante.asignar_nota_curso("MATE1203", 3)
        self.estudiante.asignar_nota_curso("BIOL1405", 4)
        assert not self.estudiante.es_candidato_a_beca(), "No debería ser candidato a beca."

    def test_cambiar_curso(self):
        """
        Prueba 7: Verifica el método cambiarCurso.

        Métodos a probar:
        - cambiarCurso
        - buscarCurso

        Casos de prueba:
        1. Ya existe un curso con el nuevo código.
        2. No existe un curso con el nuevo código.
        """
        cambio = self.estudiante.cambiar_curso("ISIS1204", "MATE1203", "Nomb", 3, Departamento.SISTEMAS)
        assert not cambio

        cambio = self.estudiante.cambiar_curso("MATE1203", "ISIS1205", "APO2", 3, Departamento.SISTEMAS)
        assert cambio
