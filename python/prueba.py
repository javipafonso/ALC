# -*- coding: iso-8859-15 -*-
diccionario={"El":"DT", "perro":"N", "come":"V", "carne":"N", "de":"P", "la":"DT", "carnicería":"N", "y":"C", "de":"P", "la":"DT", "nevera":"N", "y":"C", "canta":"V", "el":"DT", "la":"N", "la":"N", "la":"N", ".":"Fp"}
print diccionario
navs = {}
for k,value in diccionario.iteritems(): 
    navs[value] = navs.get(value,0) + 1
k=sorted(navs.iteritems())
for k,v in k:
  print k, v
print '\n'
print "Segundo ejercicio"
dicm={}
cont=0
for k1,value in diccionario.iteritems():   
  #print diccionario.get(k1,value) + 1 
  contv=diccionario.get(value,0) + 1
  for k2,v in navs.iteritems():
    if (diccionario.get(k1,0) == k2):
      dicm[k1] = cont, k2, contv
  cont=0
  contv=0
z=sorted(dicm.iteritems())
for k in z:
  print k
