#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija
import calcplus

if __name__ == "__main__":
    
    with open(sys.argv[1]) as fichero:
        infor = csv.reader(fichero)
        
        
