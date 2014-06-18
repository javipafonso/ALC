#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-
from xml.dom import minidom
dom=minidom.parse("/home/javier/ALC/python/frase_ancora.xml")
nodes=dom.childNodes
def VisualizarNodos (lista, nivel):
	for nodo in lista:
		#print ("    ")*	nivel,nodo.nodeName, nodo.nodeValue
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

