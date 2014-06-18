#! /usr/bin/env python
# -*- coding: utf-8 -*-

# **** Ejercicio 2 ****
# Javier Pérez Afonso

import re

def find_dates(entry):
    exp_month = "enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre|\d{1,2}"
    exp_day = "\d{1,2}"
    exp_year = "\d{2,4}"
    exp_sep = "(-|/| de |\s)"
    exp_date = "("+exp_day+")"+exp_sep+"("+exp_month+")("+exp_sep+exp_year+")?"

    reg_exp = re.compile(exp_date)
    res = re.finditer(reg_exp,entry)

    last_match = 0
    new_text = ""
    for i in res:
        new_text += entry[last_match:i.start()]+'<FECHA>'+i.group()+'<FECHA>'        
        last_match = i.end()
    new_text += entry[i.end():len(entry)]
    print new_text
    return new_text


phrase = "El 12-03-2011 no habrá clase, se pasa al 01/04/11 o al 02/04.\n El 12 de febrero de 2011 no habrá examen, será el 13 de enero o sea, el 13/01/2011"
find_dates(phrase)
