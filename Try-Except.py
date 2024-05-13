#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 11:30:28 2024

@author: xavier
"""

temp = input('Ingrese el valor de la temperatura: ')

try :
    farh = float(temp)
    cel = (farh - 32) * 0.5 / 9.0
    print(farh, 'grados Farh = ', cel, 'grados cel' )
except:
    print('Ingrese un numero valido')