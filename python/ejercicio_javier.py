#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

dicc = {}
cadena = "El/DT perro/N come/V carne/N de/P la/DT carnicería/N y/C de/P la/DT nevera/N y/C canta/V el/DT la/N la/N la/N ./Fp"

#funcion para obtener las categorias
def ObtCategoria():
	dcc={}
	cad = cadena.split()
	for elemento in cad:
		el = elemento.split("/")
		if ( not dcc.has_key(el[1]) ):
			dcc[el[1]]=1
		else:
			dcc[el[1]]=dcc[el[1]]+1

	return dcc

print "Question 1", '\n'
dicc = ObtCategoria()
for k,v in sorted(dicc.iteritems()):
	print k,v

#funcion para obtener la frecuencia de los elementos
def Frecuencia(adc, elm):
	if (not  adc.has_key(elm) ):
		adc[elm]=1
	else:
		adc[elm]=adc[elm]+1
	
#funcion para obtener la frecuencia de las palabras y categoria
def ObtenerPalabras():
	dcc={}
	cad_split = cadena.split()
	for elemento in cad_split:
		el_split = elemento.split("/")
		key = el_split[0].lower()
		cat = el_split[1]
		if ( not dcc.has_key(key) ):
			dcc[key]=[1,{}]
			Frecuencia( dcc[key][1], cat )
		else:
			dcc[key][0]=dcc[key][0]+1
			Frecuencia( dcc[key][1], cat )
	return dcc

print '\n',"Question 2",'\n'
dicc = ObtenerPalabras()
s=""
for k,v in sorted(dicc.iteritems()):
	s = str(k) + " " + str(v[0])
	for i,l in v[1].iteritems():
		s += " " + str(i) + " " + str(l)
	print s
	
	
#funcion para obtener la frecuencia de los bigramas con inicio y fin de cadena
def FreqBigramas(cad):
	dcc={}
	cad_sp = cad.split()
	for i in range( len(cad_sp) ):
		elemento=cad_sp[i]
		
		if(elemento=="</S>"):
			break
		
		elemento2=cad_sp[i+1]
		
		if(elemento=="<S>"):
			cat=elemento
		else:
			cat=elemento.split("/")[1]
		if(elemento2=="</S>"):
			cat2=elemento2
		else:
			cat2=elemento2.split("/")[1]
		
		key = cat + ", " + cat2
		if ( not dcc.has_key(key) ):
			dcc[key]=1
		else:
			dcc[key]=dcc[key]+1
	return dcc

print '\n',"Question 3",'\n'
dicc = FreqBigramas("<S> "+cadena+" </S>")
for k,v in sorted(dicc.iteritems()):
	print "{" ,k,v,"}"
	
#Obtener la frecuencia de los bigramas con la palabra la
def Probabilidad(palabra):
	Pdcc=ObtenerPalabras()
	catDict=ObtCategoria()
	
	for key in Pdcc[palabra][1]:
		res = float(Pdcc[palabra][1][key])/float(Pdcc[palabra][0])
		print "P ("+key+" | "+palabra+")="+str(res)
	
	for key in Pdcc[palabra][1]:
		res = float(Pdcc[palabra][1][key])/float(catDict[key])
		print "P ("+palabra+" | "+key+")="+str(res)

print '\n',"Question 4",'\n'
Probabilidad("la")
