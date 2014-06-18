#! /usr/bin/env python
# -*- coding: utf-8 -*-

# **** Ejercicio 3 ****
# Javier Pérez Afonso

import re


def tokenizer(fichero_in, fichero_out):
	
	f1 = open(fichero_in,'r')
	f2 = open(fichero_out,'w')

	exp_url="(http(s)?://(www\.)?([^\s]+)+\.[^\s]+)"  #expresión url_web
	exp_correo="([\w\.\_\-]+@[\w\.\_\-]+)" #expresión correo
	exp_horas ="(\d+:\d+)" #cualquier horas
	exp_fechas = "(\d{2}(/|-)\d{2}((/|-)\d{4})?)" #expresion fechas
	exp_numeros = "(\d+(/|.|,)\d+)" #expresion numeros
	exp_palabras = "(\w+)" #cualquier palabra
	exp_simbolos = "([^(\s|\w))]+)"	#cualquier símbolo
		
	reg_exp= exp_correo+"|"+exp_url+"|"+exp_numeros+"|"+exp_fechas+"|"+exp_horas+"|"+ exp_palabras+"|"+exp_simbolos
	reg_final = re.compile(reg_exp,re.U)
   
	for line in f1:
		result = re.finditer(reg_final,line)
		for i in result:
			f2.write(line[i.start():i.end()])
			f2.write('\n')

	f1.close()
	f2.close()           


tokenizer("entrada_tokenizador.txt","salida_tok.txt")
