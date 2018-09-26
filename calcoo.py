#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def __init__(self, operando1, operando2):

        self.operando1 = operando1
        self.operando2 = operando2

    def suma(self):

        return self.operando1 + self.operando2

    def resta(self):

        return self.operando1 - self.operando2


if __name__ == "__main__":

    try:
        operando1 = float(sys.argv[1])
        operacion = sys.argv[2]
        operando2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calculos = Calculadora(operando1, operando2)

    if operacion == "suma":
        resultado = calculos.suma()
    elif operacion == "resta":
        resultado = calculos.resta()
    else:
        sys.exit("Operación sólo puede ser suma o resta.")

    print(resultado)
