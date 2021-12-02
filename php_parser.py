import ply.yacc as yacc
from php_lexer import tokens
import php_lexer
import sys

VERBOSE = 1

val=False

def p_inicio(p):
    '''program : import declaracion_sentencias
                | import
                | declaracion_sentencias'''
    pass


def p_declaracion_sentencias(p):
    '''declaracion_sentencias : sentencias declaracion_sentencias
                                | sentencias'''
    pass


def p_sentencias(p):
    '''sentencias : sentassign
                    | call_function CIERRE
                    | sentif
                    | sentecho
                    | sentfunc
                    | sentreturn
                    | sentfor
                    | sentwhile
                    | sentdowhile
                    '''
    pass

#sentencia return
def p_sentreturn(p):
    '''sentreturn : RETURN type CIERRE
                    | RETURN cond CIERRE'''

# sentencia para imprimir
def p_sentecho(p):
    '''sentecho : ECHO typevar CIERRE
                | ECHO exp CIERRE
                | ECHO cond CIERRE'''
    pass

# para el if, else if, else
def p_sentif(p):
    '''sentif : IF genif auxsentif'''
    pass

def p_auxsentif(p):
    '''auxsentif : ELSE IF genif auxsentif
                    | ELSE LCURBRACE declaracion_sentencias RCURBRACE
                    | empty'''
    pass

def p_generatorif(p):

    '''genif : LPARENT cond RPARENT LCURBRACE declaracion_sentencias RCURBRACE'''
    pass
#asignaciones
def p_sentassign(p):
    '''sentassign :  ID EQUAL exp CIERRE
                    | ID PLUS PLUS CIERRE
                    | ID MINUS MINUS CIERRE'''
    pass


#expresiones logicas


def p_booleanos(p):
    '''bool : TRUE
            | FALSE '''
    pass

def p_operadoreslogicos(p):
    '''oplogicos : AND
                    | OR
                    | XOR
                    | NOT '''
    pass



#expresiones de comparacion

def p_exp(p):
    '''exp : expsimple  opcomparacion  expsimple
            | LPARENT expsimple  opcomparacion  expsimple RPARENT
            | expsimple'''
    pass


def p_opcomparacion(p):
    '''opcomparacion : IGUAL
                        | NOIGUAL
                        | IDENTICO
                        | MAYOR
                        | MAYORIG
                        | MENOR
                        | MENORIG'''



#expresiones matematicas
def p_expression_simple(p):
    '''expsimple :  expsimple  opsuma term
                | term'''
    pass

def p_term(p):
    '''term : term opmult factor
            | factor'''
    pass

def p_factor(p):
    '''factor : INTEGER
                | ID
                | call_function
                | LPARENT expsimple RPARENT'''
    pass

def p_typevar(p):
    '''typevar : INTEGER
                | STRING
                | STRINGG
                | TRUE
                | FALSE'''
    pass

def p_opsuma(p):
    '''opsuma : PLUS
                | MINUS '''
    pass

def p_opmult(p):
    '''opmult : TIMES
                | DIV
                | MODULO
                | EXPONENCIACION '''
    pass

def p_cond(p):
    '''cond : type
            | cond opcomparacion cond
            | cond oplogicos cond
            | LPARENT type RPARENT
            | LPARENT cond RPARENT'''
    pass


def p_type(p):
	'''type : typevar
				| var_declaration_gen'''
	pass

def p_var_declaration_gen(p):
	'''var_declaration_gen : ID
    						| ID PLUS PLUS
                            | ID MINUS MINUS
    						| MINUS MINUS  ID
                            | PLUS PLUS ID
    						| typevar
                            | exp '''
	pass

def p_arg(p):
	'''arg : var_declaration_gen
			| type
			| expsimple
			| type COMMA arg
			| STRING
            | STRINGG
			| var_declaration_gen COMMA arg
			| STRING COMMA arg
            | STRINGG COMMA arg
            |'''
	pass

def p_arg2(p):
	'''argfunc : ID
			| ID COMMA argfunc
            |'''
	pass

#referente a funciones
#declara funcionees
def p_sentfunc(p):
    '''sentfunc : FUNCTION NFUNCTION LPARENT argfunc RPARENT LCURBRACE declaracion_sentencias RCURBRACE'''
    pass

# para el llamado de las funciones
def p_call_function(p):
	'''call_function : NFUNCTION
						| NFUNCTION LPARENT arg RPARENT'''
	pass

#secuencias de los ciclos
def p_sentfor(p):
    '''sentfor : FOR LPARENT ID EQUAL expsimple CIERRE cond CIERRE expsimple  RPARENT LCURBRACE  declaracion_sentencias RCURBRACE
                | FOR LPARENT ID EQUAL expsimple CIERRE cond CIERRE ID PLUS PLUS  RPARENT LCURBRACE  declaracion_sentencias RCURBRACE
                | FOR LPARENT ID EQUAL expsimple CIERRE cond CIERRE ID MINUS MINUS  RPARENT LCURBRACE  declaracion_sentencias RCURBRACE'''
    pass


def p_sentwhile(p):
    '''sentwhile : WHILE LPARENT cond RPARENT LCURBRACE declaracion_sentencias RCURBRACE '''
    pass

def p_sentdowhile(p):
    '''sentdowhile : DO LCURBRACE  declaracion_sentencias RCURBRACE WHILE LPARENT cond RPARENT CIERRE'''
    pass

#importaciones dentro de php
def p_import(p):
    '''import : INCLUDE STRINGG CIERRE'''
    pass

def p_empty(p):
    'empty : '
    pass
# Error rule for syntax errors
def p_error(p):
    global val
    val = True
    if p is None:
        print('Error de sintaxis')
    else:
        print('ERROR DE SINTAXIS en la linea')

# Build the parser
parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba_1.php'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	if not val :
		print("Tu parser reconocio correctamente todo")
	#input()