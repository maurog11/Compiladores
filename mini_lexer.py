import ply.lex as lex
import sys

# lista de tokens
tokens = (
    # Reserverd words
    'ABSTRACT',
    'AND',
    'AS',
    'BREAK',
    'CALLABLE' 
    'CASE',
    'CATCH',
    'CLONE',
    'CONST',
    'CONTINUE',
    'DECLARE',
    'DEFAULT',
    'ECHO',
    'ELSE',
    'ELSEIF',
    'ENDDECLARE',
    'ENDFOR',
    'ENDFOREACH',
    'ENDIF',
    'ENDSWITCH',
    'ENDWHILE',
    'EXTENDS',
    'FINAL',
    'FINALLY',
    'FN',
    'FOR',
    'FOREACH',
    'FUNCTION',
    'FUNCTION_NAME'
    'GLOBAL',
    'GOTO',
    'IF',
    'IMPLEMENTS',
    'INSTEADOF'
    'INTERFACE',
    'MATCH',
    'NAMESPACE',
    'NEW',
    'OR',
    'PRINT',
    'PRIVATE',
    'PROTECTED',
    'PUBLIC',
    'REQUIRE',
    'REQUIRE_ONCE',
    'RETURN',
    'STATIC',
    'SWITCH',
    'THROW'
    'TRAIT',
    'TRY',
    'USE',
    'VAR',
    'WHILE',
    'XOR',
    'YIELD',
   
    # Symbols
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MINUSMINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
    'QUESTION',
    'DOLLAR',
    'QUOTATION',
    'APOSTROPHE',

    # Others   
    'ID', 
    'NUMBER',
    'COMMENTS'
)

# Regular expressions rules for a simple tokens 
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_QUESTION = r'\?'
t_DOLLAR = r'\$'
t_QUOTATION = r'\"'
t_APOSTROPHE = r'\''

def t_ABSTRACT(t):
    r'abstract'
    return t

def t_AND(t):
    r'and'
    return t

def t_AS(t):
    r'as'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CALLABLE(t):
    r'callable'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CLONE(t):
    r'clone'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DECLARE(t):
    r'declare'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t

def t_ENDDECLARE(t):
    r'enddeclare'
    return t

def t_ENDFOR(t):
    r'endfor'
    return t

def t_ENDFOREACH(t):
    r'endforeach'
    return t

def t_ENDIF(t):
    r'endif'
    return t

def t_ENDSWITCH(t):
    r'endswitch'
    return t

def t_ENDWHILE(t):
    r'endwhile'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_FINAL(t):
    r'final'
    return t

def t_FINALLY(t):
    r'finally'
    return t

def t_FN(t):
    r'fn'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_GLOBAL(t):
    r'global'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_IF(t):
    r'if'
    return t

def t_IMPLEMENTS(t):
	r'implements'
	return t

def t_INSTEADOF(t):
    r'insteadof'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_MATCH(t):
    r'match'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_NEW(t):
    r'new'
    return t

def t_OR(t):
    r'or'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_REQUIRE_ONCE(t):
    r'require_once'
    return t

def t_RETURN(t):
	r'return'
	return t

def t_STATIC(t):
	r'static'
	return t

def t_SWITCH(t):
    r'switch'
    return t

def t_THROW(t):
	r'throw'
	return t

def t_TRAIT(t):
	r'trait'
	return t

def t_TRY(t):
	r'try'
	return t

def t_USE(t):
	r'use'
	return t

def t_VAR(t):
	r'var'
	return t
	
def t_WHILE(t):
	r'while'
	return t

def t_XOR(t):
	r'xor'
	return t

def t_YIELD(t):
	r'yield'
	return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_COMMENTS(t):
    r'(/\*(.|\n)*?\*/)|((//|\#)[^\n]*)'
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t
    
def t_MINUSMINUS(t):
	r'--'
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'test.php'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	#input()

