#! /usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import cess_esp
#Pregunta 1.a
#forma larga
print "pregunta 1a"
etiquetado=cess_esp.tagged_words()
etiquetas=set(tag for (word,tag) in etiquetado)
print etiquetas
#otra forma simplificada
etiquetado=cess_esp.tagged_words(simplify_tags=True)
etiquetas=set(tag for (word,tag) in etiquetado)
print etiquetas
#pregunta 1.b
print "pregunta 1b"
for field in cess_esp.fileids():
  vocabulario = set([w.lower() for w in cess_esp.words(field)])
print vocabulario
#Pregunta 1.c
print "pregunta 1c"
etiquetado=cess_esp.tagged_words()
for i in etiquetado:
  print i[0]," ",i[1]
#Pregunta 1.d
print "pregunta 1d"
t=cess_esp.parsed_sents()[0]
print t
#Pregunta 2
print "pregunta 2"
from xml.dom import minidom
dom=minidom.parse("/home/javier/ALC/python/frase_ancora.xml")
nodes=dom.childNodes
def VisualizarNodos (lista, nivel):
	for nodo in lista:
		if nodo.nodeType == nodo.ELEMENT_NODE:
			if nodo.attributes.get("wd"):
				x=nodo.attributes.get("wd").value    #guardamos valor del nodo
				if nodo.attributes.get("pos"):
					y=nodo.attributes.get("pos").value  #guardamos valor del atributo pos
					if nodo.attributes.get("ne"):
						print x,y,nodo.attributes.get("ne").value    #guardamos valor del atributo ne
					else:
						print x,y,"NO_NE"
				else:
					print x,"UNK_POS"
		
					
     # Llamamos recursivamente a la función.
		VisualizarNodos (nodo.childNodes, nivel + 1)

# Llamamos a la función.
VisualizarNodos(dom.childNodes, 0)
