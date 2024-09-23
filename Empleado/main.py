from src.Empleado import Empleado
from src.Fecha import Fecha

empleado1 = Empleado("Juan", "Perez", 1300000, 1)
print(empleado1.DarSalario())
print(empleado1.CalcularSalarioAnual())
print(empleado1.CalcularImpuestoSalarioAnual())
print("----------------------------------------------------------------")
empleado1.CambiarSalario(2000000)
print(empleado1.DarSalario())
print(empleado1.CalcularSalarioAnual())
print(empleado1.CalcularImpuestoSalarioAnual())