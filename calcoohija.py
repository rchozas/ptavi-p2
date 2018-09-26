#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def multiplica(self):

        return self.operando1 * self.operando2

    def divide(self):

        return self.operando1 / self.operando2


if __name__ == "__main__":

    try:
        operando1 = float(sys.argv[1])
        operacion = sys.argv[2]
        operando2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calcular = CalculadoraHija(operando1, operando2)

    if operacion == "suma":
        resultado = calcular.suma()
    elif operacion == "resta":
        resultado = calcular.resta()
    elif operacion == "multiplica":
        resultado = calcular.multiplica()
    elif operacion == "divide":
        try:
            resultado = calcular.divide()
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")
    else:
        sys.exit("Operación sólo puede ser suma, resta, multiplica o divide.")

    print(resultado)
