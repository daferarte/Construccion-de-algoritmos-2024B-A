from Curso import Curso
from Departamento import Departamento

class Estudiante:
    NOTA_PRUEBA_ACADEMICA = 3.25
    NOTA_CANDIDATO_BECA = 4.75

    def __init__(self):
        self.nombre = "Juliana"
        self.apellido = "Ramírez"
        self.codigo = 201612345
        self.curso1 = Curso("ISIS1204", "APO1", 3, Departamento.SISTEMAS)
        self.curso2 = Curso("MATE1203", "Cálculo diferencial", 3, Departamento.MATEMATICAS)
        self.curso3 = Curso("FISI1100", "Física 1", 4, Departamento.FISICA)
        self.curso4 = Curso("BIOL1405", "Biología celular", 4, Departamento.BIOLOGIA)

    def dar_codigo(self):
        return self.codigo

    def dar_nombre(self):
        return self.nombre

    def dar_apellido(self):
        return self.apellido

    def dar_curso1(self):
        return self.curso1

    def dar_curso2(self):
        return self.curso2

    def dar_curso3(self):
        return self.curso3

    def dar_curso4(self):
        return self.curso4

    def calcular_promedio_estudiante(self):
        total_nota = 0.0
        total_creditos = 0.0

        for curso in [self.curso1, self.curso2, self.curso3, self.curso4]:
            if curso.esta_calificado():
                total_nota += curso.dar_nota() * curso.dar_creditos()
                total_creditos += curso.dar_creditos()

        if total_creditos > 0:
            return total_nota / total_creditos
        return -1

    def esta_en_prueba(self):
        promedio = self.calcular_promedio_estudiante()
        return promedio < self.NOTA_PRUEBA_ACADEMICA if promedio != -1 else False

    def es_candidato_beca(self):
        promedio = self.calcular_promedio_estudiante()
        return promedio >= self.NOTA_CANDIDATO_BECA if promedio != -1 else False

    def buscar_curso(self, codigo_curso: str):
        for curso in [self.curso1, self.curso2, self.curso3, self.curso4]:
            if curso.dar_codigo() == codigo_curso:
                return curso
        return None

    def asignar_nota_curso(self, codigo_curso: str, nota: float):
        curso = self.buscar_curso(codigo_curso)
        if curso and Curso.MINIMA <= nota <= Curso.MAXIMA:
            curso.asignar_nota(nota)
            return True
        return False

    def cambiar_curso(self, codigo_actual: str, nuevo_codigo: str, nombre: str, creditos: int, departamento: Departamento):
        curso_existente = self.buscar_curso(nuevo_codigo)
        if curso_existente is None:
            for idx, curso in enumerate([self.curso1, self.curso2, self.curso3, self.curso4]):
                if curso.dar_codigo() == codigo_actual:
                    nuevo_curso = Curso(nuevo_codigo, nombre, creditos, departamento)
                    if idx == 0:
                        self.curso1 = nuevo_curso
                    elif idx == 1:
                        self.curso2 = nuevo_curso
                    elif idx == 2:
                        self.curso3 = nuevo_curso
                    else:
                        self.curso4 = nuevo_curso
                    return True
        return False

    def metodo1(self):
        return "Respuesta 1"

    def metodo2(self):
        return "Respuesta 2"