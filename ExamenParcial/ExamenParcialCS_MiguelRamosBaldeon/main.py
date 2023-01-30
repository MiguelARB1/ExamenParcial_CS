from src.Validaciones.ValidarIngreso import ValidarIngreso

nombreTrabajador = (input("Digite los nombres del trabajador\t"))

sueldoBasico = ValidarIngreso()
sueldoBasico.ValidarIngresoSueldo()

diasFalta = ValidarIngreso()
diasFalta.validarIngresoDias()

minutosTardanza = ValidarIngreso()
minutosTardanza.validarIngresoMinutos()

horasExtras = ValidarIngreso()
horasExtras.validarIngresoHoras()


pagoHorasExtras = 1.50 * horasExtras.valor * sueldoBasico.valor / 30 / 8
movilidad = 1000.
bonificacionSuplementaria = 0.03*sueldoBasico.valor
bonificaciones = movilidad + bonificacionSuplementaria + pagoHorasExtras
remuneracionComputable = sueldoBasico.valor + movilidad + bonificacionSuplementaria
remuneracionMinima = sueldoBasico.valor + bonificaciones
DescuentoFaltas = remuneracionComputable / 30 * diasFalta.valor
descuentoTardanzas = remuneracionComputable / 30 / 8 / 60 * minutosTardanza.valor
descuentos = DescuentoFaltas + descuentoTardanzas
sueldoNeto = sueldoBasico.valor + bonificaciones - descuentos

print("\n\n")
print("===================BOLETA DE PAGO======================")
print("=======================================================")
print(f"\033[92mNombres\t\t\t\t\t\t{nombreTrabajador.upper()}\033[0m")
print(f"\033[92mSueldo Base \t\t\t\tS/ {sueldoBasico.valor}\033[0m")
print("=======================================================")
print(f"Pago por horas extras\t\tS/ {round(pagoHorasExtras,2)}")
print(f"Bonificacion suplementaria\tS/ {round(bonificacionSuplementaria,2)}")
print(f"Movilidad\t\t\t\t\tS/ {movilidad}")
print(f"\033[92mBonificacion Total\t\t\tS/ {round(bonificaciones,2)}\033[0m")
print("=======================================================")
print(f"Descuentos por faltas\t\tS/ {round(DescuentoFaltas,2)}")
print(f"Descuentos por Tardanzas\tS/ {round(descuentoTardanzas,2)})")
print(f"\033[91mDescuento Total\t\t\t\tS/ {round(descuentos,2)}\033[0m")
print("=======================================================")
print(f"\033[93mSueldo Neto\t\t\t\t\tS/ {round(sueldoNeto,2)}\033[0m")
print("=======================================================")

