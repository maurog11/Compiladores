
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CIERRE COMMA CONCATSTR DIV DO DOSPUNTOS ECHO ELSE EQUAL EXPONENCIACION FALSE FOR FUNCTION ID IDENTICO IF IGUAL INCLUDE INTEGER LCORCHETE LCURBRACE LPARENT MAYOR MAYORIG MENOR MENORIG MINUS MODULO NFUNCTION NOIGUAL NOT OR PLUS RCORCHETE RCURBRACE RETURN RPARENT STRING STRINGG TIMES TRUE WHILE XORprogram : import declaracion_sentencias\n                | import\n                | declaracion_sentenciasdeclaracion_sentencias : sentencias declaracion_sentencias\n                                | sentenciassentencias : sentassign\n                    | call_function CIERRE\n                    | sentif\n                    | sentecho\n                    | sentfunc\n                    | sentreturn\n                    | sentfor\n                    | sentwhile\n                    | sentdowhile\n                    sentreturn : RETURN type CIERRE\n                    | RETURN cond CIERREsentecho : ECHO typevar CIERRE\n                | ECHO exp CIERRE\n                | ECHO cond CIERREsentif : IF genif auxsentifauxsentif : ELSE IF genif auxsentif\n                    | ELSE LCURBRACE declaracion_sentencias RCURBRACE\n                    | emptygenif : LPARENT cond RPARENT LCURBRACE declaracion_sentencias RCURBRACEsentassign :  ID EQUAL exp CIERRE\n                    | ID PLUS PLUS CIERRE\n                    | ID MINUS MINUS CIERREbool : TRUE\n            | FALSE oplogicos : AND\n                    | OR\n                    | XOR\n                    | NOT exp : expsimple  opcomparacion  expsimple\n            | LPARENT expsimple  opcomparacion  expsimple RPARENT\n            | expsimpleopcomparacion : IGUAL\n                        | NOIGUAL\n                        | IDENTICO\n                        | MAYOR\n                        | MAYORIG\n                        | MENOR\n                        | MENORIGexpsimple :  expsimple  opsuma term\n                | termterm : term opmult factor\n            | factorfactor : INTEGER\n                | ID\n                | call_function\n                | LPARENT expsimple RPARENTtypevar : INTEGER\n                | STRING\n                | STRINGG\n                | TRUE\n                | FALSEopsuma : PLUS\n                | MINUS opmult : TIMES\n                | DIV\n                | MODULO\n                | EXPONENCIACION cond : type\n            | cond opcomparacion cond\n            | cond oplogicos cond\n            | LPARENT type RPARENT\n            | LPARENT cond RPARENTtype : typevar\n\t\t\t\t| var_declaration_genvar_declaration_gen : ID\n    \t\t\t\t\t\t| ID PLUS PLUS\n                            | ID MINUS MINUS\n    \t\t\t\t\t\t| MINUS MINUS  ID\n                            | PLUS PLUS ID\n    \t\t\t\t\t\t| typevar\n                            | exp arg : var_declaration_gen\n\t\t\t| type\n\t\t\t| expsimple\n\t\t\t| type COMMA arg\n\t\t\t| STRING\n            | STRINGG\n\t\t\t| var_declaration_gen COMMA arg\n\t\t\t| STRING COMMA arg\n            | STRINGG COMMA arg\n            |argfunc : ID\n\t\t\t| ID COMMA argfunc\n            |sentfunc : FUNCTION NFUNCTION LPARENT argfunc RPARENT LCURBRACE declaracion_sentencias RCURBRACEcall_function : NFUNCTION\n\t\t\t\t\t\t| NFUNCTION LPARENT arg RPARENTsentfor : FOR LPARENT ID EQUAL expsimple CIERRE cond CIERRE expsimple  RPARENT LCURBRACE  declaracion_sentencias RCURBRACE\n                | FOR LPARENT ID EQUAL expsimple CIERRE cond CIERRE ID PLUS PLUS  RPARENT LCURBRACE  declaracion_sentencias RCURBRACE\n                | FOR LPARENT ID EQUAL expsimple CIERRE cond CIERRE ID MINUS MINUS  RPARENT LCURBRACE  declaracion_sentencias RCURBRACEsentwhile : WHILE LPARENT cond RPARENT LCURBRACE declaracion_sentencias RCURBRACE sentdowhile : DO LCURBRACE  declaracion_sentencias RCURBRACE WHILE LPARENT cond RPARENT CIERREimport : INCLUDE STRINGG CIERREempty : '
    
_lr_action_items = {'INCLUDE':([0,],[4,]),'ID':([0,2,5,6,8,9,10,11,12,13,14,18,20,27,28,31,32,33,43,56,58,59,60,61,64,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,103,104,105,106,107,110,111,112,113,114,118,119,121,122,124,125,126,127,129,136,147,151,156,158,161,163,166,167,170,172,174,175,178,180,181,185,191,195,196,197,200,201,],[15,15,15,-6,-8,-9,-10,-11,-12,-13,-14,48,48,-7,62,48,-99,48,48,48,115,48,15,-98,62,-20,-23,-17,-18,-19,48,48,-37,-38,-39,-40,-41,-42,-43,-30,-31,-32,-33,62,62,-57,-58,48,62,-59,-60,-61,-62,143,144,146,-15,-16,-25,62,-26,-27,48,48,48,48,15,62,62,62,-99,15,146,15,-21,-22,15,48,48,-24,-96,-90,183,-97,15,15,15,-93,-94,-95,]),'NFUNCTION':([0,2,5,6,8,9,10,11,12,13,14,18,19,20,27,28,31,32,33,43,56,59,60,61,64,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,103,104,105,106,107,113,114,118,119,121,122,124,125,126,127,129,136,147,151,156,158,163,166,167,170,172,174,175,178,180,181,185,191,195,196,197,200,201,],[16,16,16,-6,-8,-9,-10,-11,-12,-13,-14,16,52,16,-7,16,16,-99,16,16,16,16,16,-98,16,-20,-23,-17,-18,-19,16,16,-37,-38,-39,-40,-41,-42,-43,-30,-31,-32,-33,16,16,-57,-58,16,16,-59,-60,-61,-62,-15,-16,-25,16,-26,-27,16,16,16,16,16,16,16,16,-99,16,16,-21,-22,16,16,16,-24,-96,-90,16,-97,16,16,16,-93,-94,-95,]),'IF':([0,2,5,6,8,9,10,11,12,13,14,27,32,60,61,75,76,77,79,80,81,113,114,118,121,122,129,156,158,163,166,167,170,175,178,180,185,191,195,196,197,200,201,],[17,17,17,-6,-8,-9,-10,-11,-12,-13,-14,-7,-99,17,-98,-20,128,-23,-17,-18,-19,-15,-16,-25,-26,-27,17,-99,17,17,-21,-22,17,-24,-96,-90,-97,17,17,17,-93,-94,-95,]),'ECHO':([0,2,5,6,8,9,10,11,12,13,14,27,32,60,61,75,77,79,80,81,113,114,118,121,122,129,156,158,163,166,167,170,175,178,180,185,191,195,196,197,200,201,],[18,18,18,-6,-8,-9,-10,-11,-12,-13,-14,-7,-99,18,-98,-20,-23,-17,-18,-19,-15,-16,-25,-26,-27,18,-99,18,18,-21,-22,18,-24,-96,-90,-97,18,18,18,-93,-94,-95,]),'FUNCTION':([0,2,5,6,8,9,10,11,12,13,14,27,32,60,61,75,77,79,80,81,113,114,118,121,122,129,156,158,163,166,167,170,175,178,180,185,191,195,196,197,200,201,],[19,19,19,-6,-8,-9,-10,-11,-12,-13,-14,-7,-99,19,-98,-20,-23,-17,-18,-19,-15,-16,-25,-26,-27,19,-99,19,19,-21,-22,19,-24,-96,-90,-97,19,19,19,-93,-94,-95,]),'RETURN':([0,2,5,6,8,9,10,11,12,13,14,27,32,60,61,75,77,79,80,81,113,114,118,121,122,129,156,158,163,166,167,170,175,178,180,185,191,195,196,197,200,201,],[20,20,20,-6,-8,-9,-10,-11,-12,-13,-14,-7,-99,20,-98,-20,-23,-17,-18,-19,-15,-16,-25,-26,-27,20,-99,20,20,-21,-22,20,-24,-96,-90,-97,20,20,20,-93,-94,-95,]),'FOR':([0,2,5,6,8,9,10,11,12,13,14,27,32,60,61,75,77,79,80,81,113,114,118,121,122,129,156,158,163,166,167,170,175,178,180,185,191,195,196,197,200,201,],[21,21,21,-6,-8,-9,-10,-11,-12,-13,-14,-7,-99,21,-98,-20,-23,-17,-18,-19,-15,-16,-25,-26,-27,21,-99,21,21,-21,-22,21,-24,-96,-90,-97,21,21,21,-93,-94,-95,]),'WHILE':([0,2,5,6,8,9,10,11,12,13,14,27,32,60,61,75,77,79,80,81,113,114,118,121,122,129,149,156,158,163,166,167,170,175,178,180,185,191,195,196,197,200,201,],[22,22,22,-6,-8,-9,-10,-11,-12,-13,-14,-7,-99,22,-98,-20,-23,-17,-18,-19,-15,-16,-25,-26,-27,22,164,-99,22,22,-21,-22,22,-24,-96,-90,-97,22,22,22,-93,-94,-95,]),'DO':([0,2,5,6,8,9,10,11,12,13,14,27,32,60,61,75,77,79,80,81,113,114,118,121,122,129,156,158,163,166,167,170,175,178,180,185,191,195,196,197,200,201,],[23,23,23,-6,-8,-9,-10,-11,-12,-13,-14,-7,-99,23,-98,-20,-23,-17,-18,-19,-15,-16,-25,-26,-27,23,-99,23,23,-21,-22,23,-24,-96,-90,-97,23,23,23,-93,-94,-95,]),'$end':([1,2,3,5,6,8,9,10,11,12,13,14,24,26,27,32,61,75,77,79,80,81,113,114,118,121,122,156,166,167,175,178,180,185,197,200,201,],[0,-2,-3,-5,-6,-8,-9,-10,-11,-12,-13,-14,-1,-4,-7,-99,-98,-20,-23,-17,-18,-19,-15,-16,-25,-26,-27,-99,-21,-22,-24,-96,-90,-97,-93,-94,-95,]),'STRINGG':([4,18,20,31,33,43,56,59,82,83,84,85,86,87,88,89,90,91,92,93,94,99,124,125,126,127,172,174,],[25,39,39,73,39,39,39,39,39,39,-37,-38,-39,-40,-41,-42,-43,-30,-31,-32,-33,39,73,73,73,73,39,39,]),'RCURBRACE':([5,6,8,9,10,11,12,13,14,26,27,32,75,77,79,80,81,113,114,117,118,121,122,156,157,166,167,168,173,175,176,178,180,185,194,197,198,199,200,201,],[-5,-6,-8,-9,-10,-11,-12,-13,-14,-4,-7,-99,-20,-23,-17,-18,-19,-15,-16,149,-25,-26,-27,-99,167,-21,-22,175,178,-24,180,-96,-90,-97,197,-93,200,201,-94,-95,]),'CIERRE':([7,16,25,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,63,65,66,67,123,131,132,133,134,137,138,139,140,141,142,143,144,162,169,177,182,],[27,-91,61,79,80,81,-48,-53,-54,-55,-56,-36,-63,-45,-69,-47,-49,-50,113,114,-68,-76,-49,118,-48,121,122,-92,-64,-65,-34,-44,-51,-66,-67,-46,-71,-72,-74,-73,172,-35,181,185,]),'EQUAL':([15,115,],[28,147,]),'PLUS':([15,16,18,20,29,31,33,37,42,43,45,47,48,49,51,56,59,62,65,71,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,108,120,123,124,125,126,127,133,134,135,137,140,150,159,162,165,172,174,183,184,186,],[29,-91,49,49,66,49,49,-48,97,49,-45,-47,108,110,-50,49,49,-49,-48,97,49,49,-37,-38,-39,-40,-41,-42,-43,-30,-31,-32,-33,49,97,141,97,-92,49,49,49,49,97,-44,97,-51,-46,97,97,97,97,49,49,186,97,189,]),'MINUS':([15,16,18,20,30,31,33,37,42,43,45,47,48,50,51,56,59,62,65,71,82,83,84,85,86,87,88,89,90,91,92,93,94,99,100,109,120,123,124,125,126,127,133,134,135,137,140,150,159,162,165,172,174,183,184,187,],[30,-91,50,50,67,50,50,-48,98,50,-45,-47,109,111,-50,50,50,-49,-48,98,50,50,-37,-38,-39,-40,-41,-42,-43,-30,-31,-32,-33,50,98,142,98,-92,50,50,50,50,98,-44,98,-51,-46,98,98,98,98,50,50,187,98,190,]),'TIMES':([16,37,45,47,48,51,62,65,123,134,137,140,183,],[-91,-48,104,-47,-49,-50,-49,-48,-92,104,-51,-46,-49,]),'DIV':([16,37,45,47,48,51,62,65,123,134,137,140,183,],[-91,-48,105,-47,-49,-50,-49,-48,-92,105,-51,-46,-49,]),'MODULO':([16,37,45,47,48,51,62,65,123,134,137,140,183,],[-91,-48,106,-47,-49,-50,-49,-48,-92,106,-51,-46,-49,]),'EXPONENCIACION':([16,37,45,47,48,51,62,65,123,134,137,140,183,],[-91,-48,107,-47,-49,-50,-49,-48,-92,107,-51,-46,-49,]),'IGUAL':([16,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,65,71,78,100,101,102,116,120,123,131,132,133,134,135,137,138,139,140,141,142,143,144,159,169,177,179,],[-91,-68,-76,84,-48,-53,-54,-55,-56,84,-63,-45,-69,-47,-49,-50,-63,84,-68,-76,-49,-48,84,84,84,-63,84,84,84,-92,84,84,-34,-44,84,-51,-66,-67,-46,-71,-72,-74,-73,-34,-35,84,84,]),'NOIGUAL':([16,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,65,71,78,100,101,102,116,120,123,131,132,133,134,135,137,138,139,140,141,142,143,144,159,169,177,179,],[-91,-68,-76,85,-48,-53,-54,-55,-56,85,-63,-45,-69,-47,-49,-50,-63,85,-68,-76,-49,-48,85,85,85,-63,85,85,85,-92,85,85,-34,-44,85,-51,-66,-67,-46,-71,-72,-74,-73,-34,-35,85,85,]),'IDENTICO':([16,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,65,71,78,100,101,102,116,120,123,131,132,133,134,135,137,138,139,140,141,142,143,144,159,169,177,179,],[-91,-68,-76,86,-48,-53,-54,-55,-56,86,-63,-45,-69,-47,-49,-50,-63,86,-68,-76,-49,-48,86,86,86,-63,86,86,86,-92,86,86,-34,-44,86,-51,-66,-67,-46,-71,-72,-74,-73,-34,-35,86,86,]),'MAYOR':([16,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,65,71,78,100,101,102,116,120,123,131,132,133,134,135,137,138,139,140,141,142,143,144,159,169,177,179,],[-91,-68,-76,87,-48,-53,-54,-55,-56,87,-63,-45,-69,-47,-49,-50,-63,87,-68,-76,-49,-48,87,87,87,-63,87,87,87,-92,87,87,-34,-44,87,-51,-66,-67,-46,-71,-72,-74,-73,-34,-35,87,87,]),'MAYORIG':([16,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,65,71,78,100,101,102,116,120,123,131,132,133,134,135,137,138,139,140,141,142,143,144,159,169,177,179,],[-91,-68,-76,88,-48,-53,-54,-55,-56,88,-63,-45,-69,-47,-49,-50,-63,88,-68,-76,-49,-48,88,88,88,-63,88,88,88,-92,88,88,-34,-44,88,-51,-66,-67,-46,-71,-72,-74,-73,-34,-35,88,88,]),'MENOR':([16,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,65,71,78,100,101,102,116,120,123,131,132,133,134,135,137,138,139,140,141,142,143,144,159,169,177,179,],[-91,-68,-76,89,-48,-53,-54,-55,-56,89,-63,-45,-69,-47,-49,-50,-63,89,-68,-76,-49,-48,89,89,89,-63,89,89,89,-92,89,89,-34,-44,89,-51,-66,-67,-46,-71,-72,-74,-73,-34,-35,89,89,]),'MENORIG':([16,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,65,71,78,100,101,102,116,120,123,131,132,133,134,135,137,138,139,140,141,142,143,144,159,169,177,179,],[-91,-68,-76,90,-48,-53,-54,-55,-56,90,-63,-45,-69,-47,-49,-50,-63,90,-68,-76,-49,-48,90,90,90,-63,90,90,90,-92,90,90,-34,-44,90,-51,-66,-67,-46,-71,-72,-74,-73,-34,-35,90,90,]),'AND':([16,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,65,78,100,101,102,116,123,131,132,133,134,135,137,138,139,140,141,142,143,144,159,169,177,179,],[-91,-68,-76,91,-48,-53,-54,-55,-56,-36,-63,-45,-69,-47,-49,-50,-63,91,-68,-76,-49,-48,91,-36,-63,91,91,-92,91,91,-34,-44,-36,-51,-66,-67,-46,-71,-72,-74,-73,-34,-35,91,91,]),'OR':([16,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,65,78,100,101,102,116,123,131,132,133,134,135,137,138,139,140,141,142,143,144,159,169,177,179,],[-91,-68,-76,92,-48,-53,-54,-55,-56,-36,-63,-45,-69,-47,-49,-50,-63,92,-68,-76,-49,-48,92,-36,-63,92,92,-92,92,92,-34,-44,-36,-51,-66,-67,-46,-71,-72,-74,-73,-34,-35,92,92,]),'XOR':([16,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,65,78,100,101,102,116,123,131,132,133,134,135,137,138,139,140,141,142,143,144,159,169,177,179,],[-91,-68,-76,93,-48,-53,-54,-55,-56,-36,-63,-45,-69,-47,-49,-50,-63,93,-68,-76,-49,-48,93,-36,-63,93,93,-92,93,93,-34,-44,-36,-51,-66,-67,-46,-71,-72,-74,-73,-34,-35,93,93,]),'NOT':([16,34,35,36,37,38,39,40,41,42,44,45,46,47,48,51,53,54,55,57,62,65,78,100,101,102,116,123,131,132,133,134,135,137,138,139,140,141,142,143,144,159,169,177,179,],[-91,-68,-76,94,-48,-53,-54,-55,-56,-36,-63,-45,-69,-47,-49,-50,-63,94,-68,-76,-49,-48,94,-36,-63,94,94,-92,94,94,-34,-44,-36,-51,-66,-67,-46,-71,-72,-74,-73,-34,-35,94,94,]),'RPARENT':([16,31,37,38,39,40,41,42,44,45,46,47,48,51,55,57,62,65,68,69,70,71,72,73,74,78,100,101,102,112,116,120,123,124,125,126,127,131,132,133,134,135,137,138,139,140,141,142,143,144,145,146,150,152,153,154,155,159,161,165,169,171,179,183,184,189,190,],[-91,-86,-48,-53,-54,-55,-56,-36,-63,-45,-69,-47,-49,-50,-68,-76,-49,-48,123,-69,-78,-36,-53,-54,-68,130,137,138,139,-89,148,137,-92,-86,-86,-86,-86,-64,-65,-34,-44,137,-51,-66,-67,-46,-71,-72,-74,-73,160,-87,137,-83,-80,-84,-85,169,-89,169,-35,-88,182,-49,188,192,193,]),'COMMA':([16,37,40,41,45,47,48,51,57,62,65,69,70,71,72,73,74,123,133,134,137,140,141,142,143,144,146,169,],[-91,-48,-55,-56,-45,-47,-49,-50,-76,-49,-48,124,125,-36,126,127,-68,-92,-34,-44,-51,-46,-71,-72,-74,-73,161,-35,]),'LPARENT':([16,17,18,20,21,22,28,31,33,43,52,56,59,64,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,103,104,105,106,107,119,124,125,126,127,128,136,147,151,164,172,174,181,],[31,33,43,56,58,59,64,64,56,99,112,56,56,119,56,56,-37,-38,-39,-40,-41,-42,-43,-30,-31,-32,-33,119,119,-57,-58,56,119,-59,-60,-61,-62,119,64,64,64,64,33,119,119,119,174,56,56,119,]),'INTEGER':([18,20,28,31,33,43,56,59,64,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,103,104,105,106,107,119,124,125,126,127,136,147,151,172,174,181,],[37,37,65,37,37,37,37,37,65,37,37,-37,-38,-39,-40,-41,-42,-43,-30,-31,-32,-33,65,65,-57,-58,37,65,-59,-60,-61,-62,65,37,37,37,37,65,65,65,37,37,65,]),'STRING':([18,20,31,33,43,56,59,82,83,84,85,86,87,88,89,90,91,92,93,94,99,124,125,126,127,172,174,],[38,38,72,38,38,38,38,38,38,-37,-38,-39,-40,-41,-42,-43,-30,-31,-32,-33,38,72,72,72,72,38,38,]),'TRUE':([18,20,31,33,43,56,59,82,83,84,85,86,87,88,89,90,91,92,93,94,99,124,125,126,127,172,174,],[40,40,40,40,40,40,40,40,40,-37,-38,-39,-40,-41,-42,-43,-30,-31,-32,-33,40,40,40,40,40,40,40,]),'FALSE':([18,20,31,33,43,56,59,82,83,84,85,86,87,88,89,90,91,92,93,94,99,124,125,126,127,172,174,],[41,41,41,41,41,41,41,41,41,-37,-38,-39,-40,-41,-42,-43,-30,-31,-32,-33,41,41,41,41,41,41,41,]),'LCURBRACE':([23,76,130,148,160,188,192,193,],[60,129,158,163,170,191,195,196,]),'ELSE':([32,156,175,],[76,76,-24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'import':([0,],[2,]),'declaracion_sentencias':([0,2,5,60,129,158,163,170,191,195,196,],[3,24,26,117,157,168,173,176,194,198,199,]),'sentencias':([0,2,5,60,129,158,163,170,191,195,196,],[5,5,5,5,5,5,5,5,5,5,5,]),'sentassign':([0,2,5,60,129,158,163,170,191,195,196,],[6,6,6,6,6,6,6,6,6,6,6,]),'call_function':([0,2,5,18,20,28,31,33,43,56,59,60,64,82,83,95,96,99,103,119,124,125,126,127,129,136,147,151,158,163,170,172,174,181,191,195,196,],[7,7,7,51,51,51,51,51,51,51,51,7,51,51,51,51,51,51,51,51,51,51,51,51,7,51,51,51,7,7,7,51,51,51,7,7,7,]),'sentif':([0,2,5,60,129,158,163,170,191,195,196,],[8,8,8,8,8,8,8,8,8,8,8,]),'sentecho':([0,2,5,60,129,158,163,170,191,195,196,],[9,9,9,9,9,9,9,9,9,9,9,]),'sentfunc':([0,2,5,60,129,158,163,170,191,195,196,],[10,10,10,10,10,10,10,10,10,10,10,]),'sentreturn':([0,2,5,60,129,158,163,170,191,195,196,],[11,11,11,11,11,11,11,11,11,11,11,]),'sentfor':([0,2,5,60,129,158,163,170,191,195,196,],[12,12,12,12,12,12,12,12,12,12,12,]),'sentwhile':([0,2,5,60,129,158,163,170,191,195,196,],[13,13,13,13,13,13,13,13,13,13,13,]),'sentdowhile':([0,2,5,60,129,158,163,170,191,195,196,],[14,14,14,14,14,14,14,14,14,14,14,]),'genif':([17,128,],[32,156,]),'typevar':([18,20,31,33,43,56,59,82,83,99,124,125,126,127,172,174,],[34,55,74,55,55,55,55,55,55,55,74,74,74,74,55,55,]),'exp':([18,20,28,31,33,43,56,59,82,83,99,124,125,126,127,172,174,],[35,57,63,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'cond':([18,20,33,43,56,59,82,83,99,172,174,],[36,54,78,102,102,116,131,132,102,177,179,]),'expsimple':([18,20,28,31,33,43,56,59,64,82,83,95,99,119,124,125,126,127,136,147,151,172,174,181,],[42,42,42,71,42,100,100,42,120,42,42,133,135,150,71,71,71,71,159,162,165,42,42,184,]),'type':([18,20,31,33,43,56,59,82,83,99,124,125,126,127,172,174,],[44,53,70,44,101,101,44,44,44,101,70,70,70,70,44,44,]),'term':([18,20,28,31,33,43,56,59,64,82,83,95,96,99,119,124,125,126,127,136,147,151,172,174,181,],[45,45,45,45,45,45,45,45,45,45,45,45,134,45,45,45,45,45,45,45,45,45,45,45,45,]),'var_declaration_gen':([18,20,31,33,43,56,59,82,83,99,124,125,126,127,172,174,],[46,46,69,46,46,46,46,46,46,46,69,69,69,69,46,46,]),'factor':([18,20,28,31,33,43,56,59,64,82,83,95,96,99,103,119,124,125,126,127,136,147,151,172,174,181,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,140,47,47,47,47,47,47,47,47,47,47,47,]),'arg':([31,124,125,126,127,],[68,152,153,154,155,]),'auxsentif':([32,156,],[75,166,]),'empty':([32,156,],[77,77,]),'opcomparacion':([36,42,54,71,78,100,102,116,120,131,132,135,177,179,],[82,95,82,95,82,136,82,82,151,82,82,136,82,82,]),'oplogicos':([36,54,78,102,116,131,132,177,179,],[83,83,83,83,83,83,83,83,83,]),'opsuma':([42,71,100,120,133,135,150,159,162,165,184,],[96,96,96,96,96,96,96,96,96,96,96,]),'opmult':([45,134,],[103,103,]),'argfunc':([112,161,],[145,171,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> import declaracion_sentencias','program',2,'p_inicio','php_parser.py',11),
  ('program -> import','program',1,'p_inicio','php_parser.py',12),
  ('program -> declaracion_sentencias','program',1,'p_inicio','php_parser.py',13),
  ('declaracion_sentencias -> sentencias declaracion_sentencias','declaracion_sentencias',2,'p_declaracion_sentencias','php_parser.py',18),
  ('declaracion_sentencias -> sentencias','declaracion_sentencias',1,'p_declaracion_sentencias','php_parser.py',19),
  ('sentencias -> sentassign','sentencias',1,'p_sentencias','php_parser.py',24),
  ('sentencias -> call_function CIERRE','sentencias',2,'p_sentencias','php_parser.py',25),
  ('sentencias -> sentif','sentencias',1,'p_sentencias','php_parser.py',26),
  ('sentencias -> sentecho','sentencias',1,'p_sentencias','php_parser.py',27),
  ('sentencias -> sentfunc','sentencias',1,'p_sentencias','php_parser.py',28),
  ('sentencias -> sentreturn','sentencias',1,'p_sentencias','php_parser.py',29),
  ('sentencias -> sentfor','sentencias',1,'p_sentencias','php_parser.py',30),
  ('sentencias -> sentwhile','sentencias',1,'p_sentencias','php_parser.py',31),
  ('sentencias -> sentdowhile','sentencias',1,'p_sentencias','php_parser.py',32),
  ('sentreturn -> RETURN type CIERRE','sentreturn',3,'p_sentreturn','php_parser.py',38),
  ('sentreturn -> RETURN cond CIERRE','sentreturn',3,'p_sentreturn','php_parser.py',39),
  ('sentecho -> ECHO typevar CIERRE','sentecho',3,'p_sentecho','php_parser.py',43),
  ('sentecho -> ECHO exp CIERRE','sentecho',3,'p_sentecho','php_parser.py',44),
  ('sentecho -> ECHO cond CIERRE','sentecho',3,'p_sentecho','php_parser.py',45),
  ('sentif -> IF genif auxsentif','sentif',3,'p_sentif','php_parser.py',50),
  ('auxsentif -> ELSE IF genif auxsentif','auxsentif',4,'p_auxsentif','php_parser.py',54),
  ('auxsentif -> ELSE LCURBRACE declaracion_sentencias RCURBRACE','auxsentif',4,'p_auxsentif','php_parser.py',55),
  ('auxsentif -> empty','auxsentif',1,'p_auxsentif','php_parser.py',56),
  ('genif -> LPARENT cond RPARENT LCURBRACE declaracion_sentencias RCURBRACE','genif',6,'p_generatorif','php_parser.py',60),
  ('sentassign -> ID EQUAL exp CIERRE','sentassign',4,'p_sentassign','php_parser.py',65),
  ('sentassign -> ID PLUS PLUS CIERRE','sentassign',4,'p_sentassign','php_parser.py',66),
  ('sentassign -> ID MINUS MINUS CIERRE','sentassign',4,'p_sentassign','php_parser.py',67),
  ('bool -> TRUE','bool',1,'p_booleanos','php_parser.py',75),
  ('bool -> FALSE','bool',1,'p_booleanos','php_parser.py',76),
  ('oplogicos -> AND','oplogicos',1,'p_operadoreslogicos','php_parser.py',80),
  ('oplogicos -> OR','oplogicos',1,'p_operadoreslogicos','php_parser.py',81),
  ('oplogicos -> XOR','oplogicos',1,'p_operadoreslogicos','php_parser.py',82),
  ('oplogicos -> NOT','oplogicos',1,'p_operadoreslogicos','php_parser.py',83),
  ('exp -> expsimple opcomparacion expsimple','exp',3,'p_exp','php_parser.py',91),
  ('exp -> LPARENT expsimple opcomparacion expsimple RPARENT','exp',5,'p_exp','php_parser.py',92),
  ('exp -> expsimple','exp',1,'p_exp','php_parser.py',93),
  ('opcomparacion -> IGUAL','opcomparacion',1,'p_opcomparacion','php_parser.py',98),
  ('opcomparacion -> NOIGUAL','opcomparacion',1,'p_opcomparacion','php_parser.py',99),
  ('opcomparacion -> IDENTICO','opcomparacion',1,'p_opcomparacion','php_parser.py',100),
  ('opcomparacion -> MAYOR','opcomparacion',1,'p_opcomparacion','php_parser.py',101),
  ('opcomparacion -> MAYORIG','opcomparacion',1,'p_opcomparacion','php_parser.py',102),
  ('opcomparacion -> MENOR','opcomparacion',1,'p_opcomparacion','php_parser.py',103),
  ('opcomparacion -> MENORIG','opcomparacion',1,'p_opcomparacion','php_parser.py',104),
  ('expsimple -> expsimple opsuma term','expsimple',3,'p_expression_simple','php_parser.py',110),
  ('expsimple -> term','expsimple',1,'p_expression_simple','php_parser.py',111),
  ('term -> term opmult factor','term',3,'p_term','php_parser.py',115),
  ('term -> factor','term',1,'p_term','php_parser.py',116),
  ('factor -> INTEGER','factor',1,'p_factor','php_parser.py',120),
  ('factor -> ID','factor',1,'p_factor','php_parser.py',121),
  ('factor -> call_function','factor',1,'p_factor','php_parser.py',122),
  ('factor -> LPARENT expsimple RPARENT','factor',3,'p_factor','php_parser.py',123),
  ('typevar -> INTEGER','typevar',1,'p_typevar','php_parser.py',127),
  ('typevar -> STRING','typevar',1,'p_typevar','php_parser.py',128),
  ('typevar -> STRINGG','typevar',1,'p_typevar','php_parser.py',129),
  ('typevar -> TRUE','typevar',1,'p_typevar','php_parser.py',130),
  ('typevar -> FALSE','typevar',1,'p_typevar','php_parser.py',131),
  ('opsuma -> PLUS','opsuma',1,'p_opsuma','php_parser.py',135),
  ('opsuma -> MINUS','opsuma',1,'p_opsuma','php_parser.py',136),
  ('opmult -> TIMES','opmult',1,'p_opmult','php_parser.py',140),
  ('opmult -> DIV','opmult',1,'p_opmult','php_parser.py',141),
  ('opmult -> MODULO','opmult',1,'p_opmult','php_parser.py',142),
  ('opmult -> EXPONENCIACION','opmult',1,'p_opmult','php_parser.py',143),
  ('cond -> type','cond',1,'p_cond','php_parser.py',147),
  ('cond -> cond opcomparacion cond','cond',3,'p_cond','php_parser.py',148),
  ('cond -> cond oplogicos cond','cond',3,'p_cond','php_parser.py',149),
  ('cond -> LPARENT type RPARENT','cond',3,'p_cond','php_parser.py',150),
  ('cond -> LPARENT cond RPARENT','cond',3,'p_cond','php_parser.py',151),
  ('type -> typevar','type',1,'p_type','php_parser.py',156),
  ('type -> var_declaration_gen','type',1,'p_type','php_parser.py',157),
  ('var_declaration_gen -> ID','var_declaration_gen',1,'p_var_declaration_gen','php_parser.py',161),
  ('var_declaration_gen -> ID PLUS PLUS','var_declaration_gen',3,'p_var_declaration_gen','php_parser.py',162),
  ('var_declaration_gen -> ID MINUS MINUS','var_declaration_gen',3,'p_var_declaration_gen','php_parser.py',163),
  ('var_declaration_gen -> MINUS MINUS ID','var_declaration_gen',3,'p_var_declaration_gen','php_parser.py',164),
  ('var_declaration_gen -> PLUS PLUS ID','var_declaration_gen',3,'p_var_declaration_gen','php_parser.py',165),
  ('var_declaration_gen -> typevar','var_declaration_gen',1,'p_var_declaration_gen','php_parser.py',166),
  ('var_declaration_gen -> exp','var_declaration_gen',1,'p_var_declaration_gen','php_parser.py',167),
  ('arg -> var_declaration_gen','arg',1,'p_arg','php_parser.py',171),
  ('arg -> type','arg',1,'p_arg','php_parser.py',172),
  ('arg -> expsimple','arg',1,'p_arg','php_parser.py',173),
  ('arg -> type COMMA arg','arg',3,'p_arg','php_parser.py',174),
  ('arg -> STRING','arg',1,'p_arg','php_parser.py',175),
  ('arg -> STRINGG','arg',1,'p_arg','php_parser.py',176),
  ('arg -> var_declaration_gen COMMA arg','arg',3,'p_arg','php_parser.py',177),
  ('arg -> STRING COMMA arg','arg',3,'p_arg','php_parser.py',178),
  ('arg -> STRINGG COMMA arg','arg',3,'p_arg','php_parser.py',179),
  ('arg -> <empty>','arg',0,'p_arg','php_parser.py',180),
  ('argfunc -> ID','argfunc',1,'p_arg2','php_parser.py',184),
  ('argfunc -> ID COMMA argfunc','argfunc',3,'p_arg2','php_parser.py',185),
  ('argfunc -> <empty>','argfunc',0,'p_arg2','php_parser.py',186),
  ('sentfunc -> FUNCTION NFUNCTION LPARENT argfunc RPARENT LCURBRACE declaracion_sentencias RCURBRACE','sentfunc',8,'p_sentfunc','php_parser.py',192),
  ('call_function -> NFUNCTION','call_function',1,'p_call_function','php_parser.py',197),
  ('call_function -> NFUNCTION LPARENT arg RPARENT','call_function',4,'p_call_function','php_parser.py',198),
  ('sentfor -> FOR LPARENT ID EQUAL expsimple CIERRE cond CIERRE expsimple RPARENT LCURBRACE declaracion_sentencias RCURBRACE','sentfor',13,'p_sentfor','php_parser.py',203),
  ('sentfor -> FOR LPARENT ID EQUAL expsimple CIERRE cond CIERRE ID PLUS PLUS RPARENT LCURBRACE declaracion_sentencias RCURBRACE','sentfor',15,'p_sentfor','php_parser.py',204),
  ('sentfor -> FOR LPARENT ID EQUAL expsimple CIERRE cond CIERRE ID MINUS MINUS RPARENT LCURBRACE declaracion_sentencias RCURBRACE','sentfor',15,'p_sentfor','php_parser.py',205),
  ('sentwhile -> WHILE LPARENT cond RPARENT LCURBRACE declaracion_sentencias RCURBRACE','sentwhile',7,'p_sentwhile','php_parser.py',210),
  ('sentdowhile -> DO LCURBRACE declaracion_sentencias RCURBRACE WHILE LPARENT cond RPARENT CIERRE','sentdowhile',9,'p_sentdowhile','php_parser.py',214),
  ('import -> INCLUDE STRINGG CIERRE','import',3,'p_import','php_parser.py',219),
  ('empty -> <empty>','empty',0,'p_empty','php_parser.py',223),
]