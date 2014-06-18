#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

correo_upv = re.compile(r"""
 #Para explicar grupo
\b #límite de palabra
#(?:    # para que no cree un grupo
(
[\w\.\_\-]+ # 1 o más caracteres de palabra o punto
)
@
[\w\.\_\-]*
upv\.es
\b #limite de palabra
 #Para explicar grupo
""", re.VERBOSE|re.U)



textoU=u"""xxx@upv.es Estos son correos upv: perez@upv.es paco.perez@upv.es y este pablo@dsic.upv.es y
este paco_pepe@upv.es y esto pepe-paco@upv.es e incluso esto alfaro@dsic.upv.es o esto arsemio.tomas.alonso_1@dep.sis_comput-inf.upv.es
pero esto no lo son:
andres111@hotmail.com no este ole@ole.com, ???@upv.es """

print textoU
print "---"
# Matching

elm=correo_upv.match(textoU)
print "elm_Match:", elm
if elm: print elm.group()
print "----"

# Searching

elm1=correo_upv.search(textoU)
print "elm_Search:", elm1
if elm1:
      print elm1.group()
      print elm1.start()
      print elm1.end()
      print elm1.span()
print "----"

#Findall

elm2=correo_upv.findall(textoU)
print "elm_findall:", elm2
print "----"
            
# Iterator
print "elm_finditer:"
resultado=re.finditer(correo_upv,textoU)
for i in resultado:
      print i.group()


# Remplacing
print "Remplacing:\n","---------\n"
print "print re.sub( 'casa','cosas','En esta casa y en la otra casa')"

print re.sub( 'casa','cosas','En esta casa y en la otra casa')
print re.subn('casa','cosas','En esta casa y en la otra casa')

print correo_upv.sub(r""" <correo_upv> \1 <\correo_upv> """,textoU)
