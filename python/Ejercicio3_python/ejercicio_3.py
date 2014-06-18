# Ejercicio 3
# -*- coding: utf-8 -*-

import re

def tokenizador(in_file,out_file):
    in_f = open(in_file,'r')
    ou_f = open(out_file,'w')

    re_mail = "(\w+@[^\s]+)"
    re_web = "(http(s)?://(w{3}\.)?([^\s]+)+\.[^\s]+)"
    re_decimal = "(\d+[\.,]\d+)"
    re_fecha = "(\d{2}(/|-)\d{2}((/|-)\d{4})?)"
    re_hora = "(\d{1,2}:\d{2})"
    re_palabra = "(\w+)"
    re_simbolos = "([^(\s|\w)]+)"

    reg_expr_string = re_mail+"|"+re_web+"|"+re_decimal+"|"+re_fecha+"|"+re_hora+"|"+re_palabra+"|"+re_simbolos
    
    reg_expr = re.compile(reg_expr_string,re.U)

    for line in in_f:
        found = re.finditer(reg_expr,line)
        for i in found:
            ou_f.write(line[i.start():i.end()])
            print line[i.start():i.end()]
            ou_f.write('\n')

    in_f.close()
    ou_f.close()

tokenizador("entrada_tokenizador.txt","salida.txt")    
