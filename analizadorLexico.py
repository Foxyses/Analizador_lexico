import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['if','while','return','else','int','float']

tokens = reservadas+['Id','Numero','OpAdicion','OpMenos','OpMulti','OpDividir',
		'OpAsignacion','OpRel1','OpRel2','OpRel3','OpRel4','OpRel5','OpRel6',
		'OpAnd','OpOR','OpNot','OpParentI', 'OpParentD','LlaveI','LlaveD','PuntoYComa'
		]

#declaracion de los tokens

t_ignore = '\t '
t_OpAdicion = r'\+'
t_OpMenos = r'\-'
t_OpMulti = r'\*'
t_OpDividir = r'/'
t_OpAsignacion = r'='
t_OpRel1 = r'<'
t_OpRel2 = r'<='
t_OpRel3 = r'>'
t_OpRel4 = r'>='
t_OpRel5 = r'!='
t_OpRel6 = r'=='
t_OpAnd = r'&&'
t_OpOR = r'\|\|'
t_OpNot = r'!'
t_OpParentI = r'\('
t_OpParentD = r'\)'
t_LlaveI = r'\{'
t_LlaveD = r'\}'
t_PuntoYComa = r';'

#identificador
def t_Id(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value

	return t
#nueva linea
def t_nuevalinea(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#comentario
def t_Comentario(t):
	r'\#.*'
	pass
#numero
def t_Numero(t):
	r'\d+'
	t.value = int(t.value)
	return t
#para el error
def t_error(t):
	print ("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)

#busca y seleciona el fichero
def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('Numero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

directorio = 'test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok : break
	print (tok)
