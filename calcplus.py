#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == '__main__':
    
    calcuplus = calcoohija.CalculadoraHija(operando1, operando2)

    fichero = open(sys.argv[1] "r")
    lineas = fichero.readlines()
    
         
        
        if operacion == "suma":
            resultado = calcuplus.suma()
        elif operacion == "resta":
            resultado = ccalcuplus.resta()
        elif operacion == "multiplica":
            resultado = calcuplus.multiplica()
        elif operacion == "divide":
            try:
                resultado = calcuplus.divide()
            except ZeroDivisionError:
                sys.exit("Division by zero is not allowed") 

    
    Fichero.close()
