class ValidarIngreso():

    def ValidarIngresoSueldo(self):
        while True:
            try:
                dato = float(input("Ingrese el Sueldo Base : \t\t\t"))
                if dato<=0:
                    raise ValueError
                self.valor = dato
                break
            except ValueError as err:
                print("El dato ingresado es incorrecto")

        return dato

    def validarIngresoDias(self):
        while True:
            try:
                dato = input("Cuantos dias falto : \t\t\t\t")
                dato = int(dato)
                self.valor = dato
                break
            except ValueError:
                print("Ingrese un número entero .")

        return dato

    def validarIngresoMinutos(self):
        while True:
            try:
                dato = input("Cuantos minutos llego tarde : \t\t")
                dato = int(dato)
                self.valor = dato
                break
            except ValueError:
                print("Ingrese un número entero .")

        return dato

    def validarIngresoHoras(self):
        while True:
            try:
                dato = input("Cuantos Horas extra trabajo : \t\t")
                dato = int(dato)
                self.valor = dato
                break
            except ValueError:
                print("Ingrese un número entero .")

        return dato