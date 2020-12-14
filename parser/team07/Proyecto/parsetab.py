
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTnonassocISISNULLNOTNULLnonassocMENOR_QUEMENOR_IGUALMAYOR_QUEMAYOR_IGUALIGUALDISTINTOnonassocBETWEENINLIKEILIKESIMILARTOleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOleftPOTENCIAleftTYPECASTleftPUNTOABS ACOS ACOSD ACOSH ADD ALL ALTER AND ANY AS ASC ASIN ASIND ASINH AT ATAN ATAN2 ATAN2d ATAND ATANH AVG BETWEEN BIGINIT BOOLEAN BY CADENA CASE CBRT CEIL CEILING CENTURY CHARACTER CHECK COMA CONSTRAINT CONVERT COS COSD COSH COT COTD COUNT CREATE CURRENT_DATE CURRENT_TIME CURRENT_TIMESTAMP DATABASE DATABASES DATE DECADE DECIMAL DECIMAL_ DECODE DEFAULT DEGREES DELETE DESC DISTINCT DISTINTO DIV DIVISION DOUBLE DOW DOY DROP ELSE ENCODE END ENTERO ENUM EPOCH ESPACIO EXCEPT EXISTS EXP EXTRACT FACTORIAL FALSE FLOOR FOREIGN FROM FULL GCD GET_BYTE GREATEST GROUP HAVING HOUR ID IF IGUAL ILIKE IN INHERITS INNER INSERT INTEGER INTERSECT INTERVAL INTO IS ISNULL ISODOWN ISOYEAR JOIN KEY LCM LEAST LEFT LENGTH LIKE LIMIT LLAVEDER LLAVEIZQ LN LOCALTIME LOCALTIMESTAMP LOG LOG10 MAS MAX MAYOR_IGUAL MAYOR_QUE MD5 MENOR_IGUAL MENOR_QUE MENOS MICROSECONDS MILENNIUM MILLISECONDS MIN MINUTE MIN_SCALE MOD MODE MODULO MONEY MONTH MULTIPLICACION NOT NOTNULL NULL NUMERIC OR ORDER OUTER OWNER PARDERECHO PARIZQUIERDO PG_SLEEP PG_SLEEP_FOR PG_SLEEP_UNTIL PI POTENCIA POWER PRECISION PRIMARY PTCOMA PUNTO QUARTER RADIANS RANDOM REAL REFERENCES RENAME REPLACE RIGHT ROUND SCALE SECOND SELECT SET SETSEED SET_BYTE SHA256 SHOW SIGN SIMILAR SIN SIND SINH SMALLINT SOME SQRT SUBSTR SUBSTRING SUM TABLE TAN TAND TANH TEXT THEN TIME TIMESTAMP TIMEZONE TIMEZONE_HOUR TIMEZONE_MINUTE TO TRIM TRIM_SCALE TRUC TRUE TYPE TYPECAST UNION UNIQUE UPDATE VALUES VARCHAR WEEK WHEN WHERE WIDTH_BUCKET WITH WITHOUT YEAR ZONE dayinit   :   instruccionesinstrucciones  :   instrucciones instruccioninstrucciones  :   instruccioninstruccion  :   crear_enum\n                    |   insert_table\n                    |   delete_table\n                    |   update_tablecrear_enum     :   CREATE TYPE ID AS ENUM PARIZQUIERDO ID PARDERECHO PTCOMAinsert_table   :   INSERT INTO ID VALUES lista_valores PTCOMA\n                      |   INSERT INTO ID PARIZQUIERDO  lista_columnas  PARDERECHO VALUES lista_valores PTCOMA\n                      |   INSERT INTO ID DEFAULT VALUES PTCOMA\n                      |   INSERT INTO ID PARIZQUIERDO lista_columnas PARDERECHO DEFAULT VALUES PTCOMAlista_columnas     :   lista_columnas COMA ID\n                          |   IDlista_valores  :   lista_valores COMA tupla\n                      |   tuplatupla  :   PARIZQUIERDO lista_expresiones PARDERECHOlista_expresiones  :   lista_expresiones COMA expresionlista_expresiones  :   expresionexpresion  :   CADENAexpresion  :   ENTEROexpresion  :   DECIMALdelete_table   :   DELETE FROM ID PTCOMA\n                      |   DELETE FROM ID WHERE exp_operacion PTCOMAexp_operacion  :  exp_logicaexp_logica     :   exp_logica OR exp_logica\n                      |   exp_logica AND exp_logica\n                      |   NOT exp_logica\n                      |   exp_relacionalexp_relacional   :   exp_relacional MENOR_QUE exp_relacional\n                        |   exp_relacional MENOR_IGUAL exp_relacional\n                        |   exp_relacional MAYOR_QUE exp_relacional\n                        |   exp_relacional MAYOR_IGUAL exp_relacional\n                        |   exp_relacional DISTINTO exp_relacional\n                        |   exp_relacional IGUAL exp_relacional\n                        |   exp_aritmeticaexp_aritmetica   :   exp_aritmetica MAS exp_aritmetica\n                        |   exp_aritmetica MENOS exp_aritmetica\n                        |   exp_aritmetica MULTIPLICACION exp_aritmetica\n                        |   exp_aritmetica DIVISION exp_aritmetica\n                        |   exp_aritmetica MODULO exp_aritmetica\n                        |   exp_aritmetica POTENCIA exp_aritmetica\n                        |   exp_aritmetica BETWEEN exp_aritmetica AND exp_aritmetica\n                        |   exp_aritmetica NOT BETWEEN exp_aritmetica AND exp_aritmetica\n                        |   exp_aritmetica IN PARIZQUIERDO lista_expresiones PARDERECHO\n                        |   exp_aritmetica NOT IN PARIZQUIERDO lista_expresiones PARDERECHO\n                        |   exp_aritmetica LIKE exp_aritmetica\n                        |   exp_aritmetica NOT LIKE exp_aritmetica\n                        |   exp_aritmetica ILIKE exp_aritmetica\n                        |   exp_aritmetica NOT ILIKE exp_aritmetica\n                        |   exp_aritmetica SIMILAR TO exp_aritmetica\n                        |   exp_aritmetica IS NULL\n                        |   exp_aritmetica IS NOT NULL\n                        |   primitivoprimitivo  :   IDprimitivo    :   MAS primitivo\n                    |   MENOS primitivo\n                    |   PARIZQUIERDO exp_operacion PARDERECHOprimitivo  :   ENTEROprimitivo    :   DECIMALprimitivo  :   CADENAprimitivo  :   TRUE\n                  |   FALSEupdate_table     :   UPDATE ID SET lista_seteos PTCOMA\n                        |   UPDATE ID SET lista_seteos WHERE exp_operacion PTCOMAlista_seteos     :   lista_seteos COMA set_columna\n                        |   set_columnaset_columna    :   ID IGUAL exp_operacion'
    
_lr_action_items = {'CREATE':([0,2,3,4,5,6,7,12,25,53,57,66,67,129,142,143,144,],[8,8,-3,-4,-5,-6,-7,-2,-23,-64,-9,-11,-24,-65,-8,-10,-12,]),'INSERT':([0,2,3,4,5,6,7,12,25,53,57,66,67,129,142,143,144,],[9,9,-3,-4,-5,-6,-7,-2,-23,-64,-9,-11,-24,-65,-8,-10,-12,]),'DELETE':([0,2,3,4,5,6,7,12,25,53,57,66,67,129,142,143,144,],[10,10,-3,-4,-5,-6,-7,-2,-23,-64,-9,-11,-24,-65,-8,-10,-12,]),'UPDATE':([0,2,3,4,5,6,7,12,25,53,57,66,67,129,142,143,144,],[11,11,-3,-4,-5,-6,-7,-2,-23,-64,-9,-11,-24,-65,-8,-10,-12,]),'$end':([1,2,3,4,5,6,7,12,25,53,57,66,67,129,142,143,144,],[0,-1,-3,-4,-5,-6,-7,-2,-23,-64,-9,-11,-24,-65,-8,-10,-12,]),'TYPE':([8,],[13,]),'INTO':([9,],[14,]),'FROM':([10,],[15,]),'ID':([11,13,14,15,20,23,26,40,43,44,45,52,54,55,56,65,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,86,87,118,120,121,125,134,146,],[16,17,18,19,27,34,37,37,37,37,37,37,37,27,96,102,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'SET':([16,],[20,]),'AS':([17,],[21,]),'VALUES':([18,24,64,101,],[22,36,100,133,]),'PARIZQUIERDO':([18,22,26,30,40,43,44,45,52,54,58,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,85,86,87,100,118,119,120,121,125,134,146,],[23,33,45,56,45,45,45,45,45,45,33,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,122,45,45,33,45,136,45,45,45,45,45,]),'DEFAULT':([18,64,],[24,101,]),'PTCOMA':([19,28,29,31,32,36,37,38,39,41,42,46,47,48,49,50,51,70,90,91,93,94,95,97,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,123,124,126,128,130,132,133,137,138,140,141,145,148,149,150,],[25,53,-67,57,-16,66,-55,67,-25,-29,-36,-54,-59,-60,-61,-62,-63,-28,-56,-57,-68,129,-66,-15,-17,-26,-27,-30,-31,-32,-33,-34,-35,-37,-38,-39,-40,-41,-42,-47,-49,-52,-58,142,143,144,-48,-50,-51,-53,-43,-45,-44,-46,]),'WHERE':([19,28,29,37,39,41,42,46,47,48,49,50,51,70,90,91,93,95,103,104,105,106,107,108,109,110,111,112,113,114,115,116,123,124,126,128,137,138,140,141,145,148,149,150,],[26,54,-67,-55,-25,-29,-36,-54,-59,-60,-61,-62,-63,-28,-56,-57,-68,-66,-26,-27,-30,-31,-32,-33,-34,-35,-37,-38,-39,-40,-41,-42,-47,-49,-52,-58,-48,-50,-51,-53,-43,-45,-44,-46,]),'ENUM':([21,],[30,]),'NOT':([26,37,40,42,45,46,47,48,49,50,51,52,54,68,69,89,90,91,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[40,-55,40,84,40,-54,-59,-60,-61,-62,-63,40,40,40,40,127,-56,-57,-37,-38,-39,-40,-41,-42,84,-47,-49,-52,-58,84,-48,-50,-51,-53,84,-45,84,-46,]),'MAS':([26,37,40,42,43,44,45,46,47,48,49,50,51,52,54,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,86,87,90,91,111,112,113,114,115,116,117,118,120,121,123,124,125,126,128,134,135,137,138,140,141,145,146,148,149,150,],[43,-55,43,77,43,43,43,-54,-59,-60,-61,-62,-63,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-56,-57,-37,-38,-39,-40,-41,-42,77,43,43,43,77,77,43,-52,-58,43,77,77,77,77,-53,77,43,-45,77,-46,]),'MENOS':([26,37,40,42,43,44,45,46,47,48,49,50,51,52,54,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,86,87,90,91,111,112,113,114,115,116,117,118,120,121,123,124,125,126,128,134,135,137,138,140,141,145,146,148,149,150,],[44,-55,44,78,44,44,44,-54,-59,-60,-61,-62,-63,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-56,-57,-37,-38,-39,-40,-41,-42,78,44,44,44,78,78,44,-52,-58,44,78,78,78,78,-53,78,44,-45,78,-46,]),'ENTERO':([26,33,40,43,44,45,52,54,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,86,87,99,118,120,121,122,125,134,136,146,],[47,62,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,62,47,47,47,62,47,47,62,47,]),'DECIMAL':([26,33,40,43,44,45,52,54,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,86,87,99,118,120,121,122,125,134,136,146,],[48,63,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,63,48,48,48,63,48,48,63,48,]),'CADENA':([26,33,40,43,44,45,52,54,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,86,87,99,118,120,121,122,125,134,136,146,],[49,61,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,61,49,49,49,61,49,49,61,49,]),'TRUE':([26,40,43,44,45,52,54,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,86,87,118,120,121,125,134,146,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'FALSE':([26,40,43,44,45,52,54,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,86,87,118,120,121,125,134,146,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'IGUAL':([27,37,41,42,46,47,48,49,50,51,90,91,105,106,107,108,109,110,111,112,113,114,115,116,123,124,126,128,137,138,140,141,145,148,149,150,],[52,-55,76,-36,-54,-59,-60,-61,-62,-63,-56,-57,None,None,None,None,None,None,-37,-38,-39,-40,-41,-42,-47,-49,-52,-58,-48,-50,-51,-53,-43,-45,-44,-46,]),'COMA':([28,29,31,32,34,35,37,39,41,42,46,47,48,49,50,51,59,60,61,62,63,70,90,91,93,95,97,98,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,123,124,126,128,131,132,137,138,139,140,141,145,147,148,149,150,],[55,-67,58,-16,-14,65,-55,-25,-29,-36,-54,-59,-60,-61,-62,-63,99,-19,-20,-21,-22,-28,-56,-57,-68,-66,-15,-17,-13,-26,-27,-30,-31,-32,-33,-34,-35,-37,-38,-39,-40,-41,-42,-47,-49,-52,-58,-18,58,-48,-50,99,-51,-53,-43,99,-45,-44,-46,]),'PARDERECHO':([34,35,37,39,41,42,46,47,48,49,50,51,59,60,61,62,63,70,90,91,92,96,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,123,124,126,128,131,137,138,139,140,141,145,147,148,149,150,],[-14,64,-55,-25,-29,-36,-54,-59,-60,-61,-62,-63,98,-19,-20,-21,-22,-28,-56,-57,128,130,-13,-26,-27,-30,-31,-32,-33,-34,-35,-37,-38,-39,-40,-41,-42,-47,-49,-52,-58,-18,-48,-50,148,-51,-53,-43,150,-45,-44,-46,]),'MULTIPLICACION':([37,42,46,47,48,49,50,51,90,91,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[-55,79,-54,-59,-60,-61,-62,-63,-56,-57,79,79,-39,-40,-41,-42,79,79,79,-52,-58,79,79,79,79,-53,79,-45,79,-46,]),'DIVISION':([37,42,46,47,48,49,50,51,90,91,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[-55,80,-54,-59,-60,-61,-62,-63,-56,-57,80,80,-39,-40,-41,-42,80,80,80,-52,-58,80,80,80,80,-53,80,-45,80,-46,]),'MODULO':([37,42,46,47,48,49,50,51,90,91,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[-55,81,-54,-59,-60,-61,-62,-63,-56,-57,81,81,-39,-40,-41,-42,81,81,81,-52,-58,81,81,81,81,-53,81,-45,81,-46,]),'POTENCIA':([37,42,46,47,48,49,50,51,90,91,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[-55,82,-54,-59,-60,-61,-62,-63,-56,-57,82,82,82,82,82,-42,82,82,82,-52,-58,82,82,82,82,-53,82,-45,82,-46,]),'BETWEEN':([37,42,46,47,48,49,50,51,84,90,91,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[-55,83,-54,-59,-60,-61,-62,-63,118,-56,-57,-37,-38,-39,-40,-41,-42,83,None,None,-52,-58,83,None,None,None,-53,83,-45,83,-46,]),'IN':([37,42,46,47,48,49,50,51,84,90,91,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[-55,85,-54,-59,-60,-61,-62,-63,119,-56,-57,-37,-38,-39,-40,-41,-42,85,None,None,-52,-58,85,None,None,None,-53,85,-45,85,-46,]),'LIKE':([37,42,46,47,48,49,50,51,84,90,91,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[-55,86,-54,-59,-60,-61,-62,-63,120,-56,-57,-37,-38,-39,-40,-41,-42,86,None,None,-52,-58,86,None,None,None,-53,86,-45,86,-46,]),'ILIKE':([37,42,46,47,48,49,50,51,84,90,91,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[-55,87,-54,-59,-60,-61,-62,-63,121,-56,-57,-37,-38,-39,-40,-41,-42,87,None,None,-52,-58,87,None,None,None,-53,87,-45,87,-46,]),'SIMILAR':([37,42,46,47,48,49,50,51,90,91,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[-55,88,-54,-59,-60,-61,-62,-63,-56,-57,-37,-38,-39,-40,-41,-42,88,None,None,-52,-58,88,None,None,None,-53,88,-45,88,-46,]),'IS':([37,42,46,47,48,49,50,51,90,91,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[-55,89,-54,-59,-60,-61,-62,-63,-56,-57,-37,-38,-39,-40,-41,-42,89,-47,-49,-52,-58,89,-48,-50,-51,-53,89,-45,89,-46,]),'MENOR_QUE':([37,41,42,46,47,48,49,50,51,90,91,105,106,107,108,109,110,111,112,113,114,115,116,123,124,126,128,137,138,140,141,145,148,149,150,],[-55,71,-36,-54,-59,-60,-61,-62,-63,-56,-57,None,None,None,None,None,None,-37,-38,-39,-40,-41,-42,-47,-49,-52,-58,-48,-50,-51,-53,-43,-45,-44,-46,]),'MENOR_IGUAL':([37,41,42,46,47,48,49,50,51,90,91,105,106,107,108,109,110,111,112,113,114,115,116,123,124,126,128,137,138,140,141,145,148,149,150,],[-55,72,-36,-54,-59,-60,-61,-62,-63,-56,-57,None,None,None,None,None,None,-37,-38,-39,-40,-41,-42,-47,-49,-52,-58,-48,-50,-51,-53,-43,-45,-44,-46,]),'MAYOR_QUE':([37,41,42,46,47,48,49,50,51,90,91,105,106,107,108,109,110,111,112,113,114,115,116,123,124,126,128,137,138,140,141,145,148,149,150,],[-55,73,-36,-54,-59,-60,-61,-62,-63,-56,-57,None,None,None,None,None,None,-37,-38,-39,-40,-41,-42,-47,-49,-52,-58,-48,-50,-51,-53,-43,-45,-44,-46,]),'MAYOR_IGUAL':([37,41,42,46,47,48,49,50,51,90,91,105,106,107,108,109,110,111,112,113,114,115,116,123,124,126,128,137,138,140,141,145,148,149,150,],[-55,74,-36,-54,-59,-60,-61,-62,-63,-56,-57,None,None,None,None,None,None,-37,-38,-39,-40,-41,-42,-47,-49,-52,-58,-48,-50,-51,-53,-43,-45,-44,-46,]),'DISTINTO':([37,41,42,46,47,48,49,50,51,90,91,105,106,107,108,109,110,111,112,113,114,115,116,123,124,126,128,137,138,140,141,145,148,149,150,],[-55,75,-36,-54,-59,-60,-61,-62,-63,-56,-57,None,None,None,None,None,None,-37,-38,-39,-40,-41,-42,-47,-49,-52,-58,-48,-50,-51,-53,-43,-45,-44,-46,]),'OR':([37,39,41,42,46,47,48,49,50,51,70,90,91,103,104,105,106,107,108,109,110,111,112,113,114,115,116,123,124,126,128,137,138,140,141,145,148,149,150,],[-55,68,-29,-36,-54,-59,-60,-61,-62,-63,-28,-56,-57,-26,-27,-30,-31,-32,-33,-34,-35,-37,-38,-39,-40,-41,-42,-47,-49,-52,-58,-48,-50,-51,-53,-43,-45,-44,-46,]),'AND':([37,39,41,42,46,47,48,49,50,51,70,90,91,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,123,124,126,128,135,137,138,140,141,145,148,149,150,],[-55,69,-29,-36,-54,-59,-60,-61,-62,-63,-28,-56,-57,69,-27,-30,-31,-32,-33,-34,-35,-37,-38,-39,-40,-41,-42,134,-47,-49,-52,-58,146,-48,-50,-51,-53,-43,-45,-44,-46,]),'TO':([88,],[125,]),'NULL':([89,127,],[126,141,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,12,]),'crear_enum':([0,2,],[4,4,]),'insert_table':([0,2,],[5,5,]),'delete_table':([0,2,],[6,6,]),'update_table':([0,2,],[7,7,]),'lista_seteos':([20,],[28,]),'set_columna':([20,55,],[29,95,]),'lista_valores':([22,100,],[31,132,]),'tupla':([22,58,100,],[32,97,32,]),'lista_columnas':([23,],[35,]),'exp_operacion':([26,45,52,54,],[38,92,93,94,]),'exp_logica':([26,40,45,52,54,68,69,],[39,70,39,39,39,103,104,]),'exp_relacional':([26,40,45,52,54,68,69,71,72,73,74,75,76,],[41,41,41,41,41,41,41,105,106,107,108,109,110,]),'exp_aritmetica':([26,40,45,52,54,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,86,87,118,120,121,125,134,146,],[42,42,42,42,42,42,42,42,42,42,42,42,42,111,112,113,114,115,116,117,123,124,135,137,138,140,145,149,]),'primitivo':([26,40,43,44,45,52,54,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,86,87,118,120,121,125,134,146,],[46,46,90,91,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'lista_expresiones':([33,122,136,],[59,139,147,]),'expresion':([33,99,122,136,],[60,131,60,60,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',380),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_lista_instrucciones','gramatica.py',384),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',389),
  ('instruccion -> crear_enum','instruccion',1,'p_instruccion','gramatica.py',393),
  ('instruccion -> insert_table','instruccion',1,'p_instruccion','gramatica.py',394),
  ('instruccion -> delete_table','instruccion',1,'p_instruccion','gramatica.py',395),
  ('instruccion -> update_table','instruccion',1,'p_instruccion','gramatica.py',396),
  ('crear_enum -> CREATE TYPE ID AS ENUM PARIZQUIERDO ID PARDERECHO PTCOMA','crear_enum',9,'p_instr_crear_enum','gramatica.py',400),
  ('insert_table -> INSERT INTO ID VALUES lista_valores PTCOMA','insert_table',6,'p_instr_insert','gramatica.py',415),
  ('insert_table -> INSERT INTO ID PARIZQUIERDO lista_columnas PARDERECHO VALUES lista_valores PTCOMA','insert_table',9,'p_instr_insert','gramatica.py',416),
  ('insert_table -> INSERT INTO ID DEFAULT VALUES PTCOMA','insert_table',6,'p_instr_insert','gramatica.py',417),
  ('insert_table -> INSERT INTO ID PARIZQUIERDO lista_columnas PARDERECHO DEFAULT VALUES PTCOMA','insert_table',9,'p_instr_insert','gramatica.py',418),
  ('lista_columnas -> lista_columnas COMA ID','lista_columnas',3,'p_lista_columnas','gramatica.py',459),
  ('lista_columnas -> ID','lista_columnas',1,'p_lista_columnas','gramatica.py',460),
  ('lista_valores -> lista_valores COMA tupla','lista_valores',3,'p_lista_valores','gramatica.py',477),
  ('lista_valores -> tupla','lista_valores',1,'p_lista_valores','gramatica.py',478),
  ('tupla -> PARIZQUIERDO lista_expresiones PARDERECHO','tupla',3,'p_tupla','gramatica.py',490),
  ('lista_expresiones -> lista_expresiones COMA expresion','lista_expresiones',3,'p_lista_expresiones','gramatica.py',497),
  ('lista_expresiones -> expresion','lista_expresiones',1,'p_lista_expresiones_expresion','gramatica.py',503),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','gramatica.py',511),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','gramatica.py',520),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','gramatica.py',529),
  ('delete_table -> DELETE FROM ID PTCOMA','delete_table',4,'p_instr_delete','gramatica.py',538),
  ('delete_table -> DELETE FROM ID WHERE exp_operacion PTCOMA','delete_table',6,'p_instr_delete','gramatica.py',539),
  ('exp_operacion -> exp_logica','exp_operacion',1,'p_instr_condicion_where','gramatica.py',560),
  ('exp_logica -> exp_logica OR exp_logica','exp_logica',3,'p_exp_logica','gramatica.py',566),
  ('exp_logica -> exp_logica AND exp_logica','exp_logica',3,'p_exp_logica','gramatica.py',567),
  ('exp_logica -> NOT exp_logica','exp_logica',2,'p_exp_logica','gramatica.py',568),
  ('exp_logica -> exp_relacional','exp_logica',1,'p_exp_logica','gramatica.py',569),
  ('exp_relacional -> exp_relacional MENOR_QUE exp_relacional','exp_relacional',3,'p_exp_relacional','gramatica.py',572),
  ('exp_relacional -> exp_relacional MENOR_IGUAL exp_relacional','exp_relacional',3,'p_exp_relacional','gramatica.py',573),
  ('exp_relacional -> exp_relacional MAYOR_QUE exp_relacional','exp_relacional',3,'p_exp_relacional','gramatica.py',574),
  ('exp_relacional -> exp_relacional MAYOR_IGUAL exp_relacional','exp_relacional',3,'p_exp_relacional','gramatica.py',575),
  ('exp_relacional -> exp_relacional DISTINTO exp_relacional','exp_relacional',3,'p_exp_relacional','gramatica.py',576),
  ('exp_relacional -> exp_relacional IGUAL exp_relacional','exp_relacional',3,'p_exp_relacional','gramatica.py',577),
  ('exp_relacional -> exp_aritmetica','exp_relacional',1,'p_exp_relacional','gramatica.py',578),
  ('exp_aritmetica -> exp_aritmetica MAS exp_aritmetica','exp_aritmetica',3,'p_exp_aritmetica','gramatica.py',581),
  ('exp_aritmetica -> exp_aritmetica MENOS exp_aritmetica','exp_aritmetica',3,'p_exp_aritmetica','gramatica.py',582),
  ('exp_aritmetica -> exp_aritmetica MULTIPLICACION exp_aritmetica','exp_aritmetica',3,'p_exp_aritmetica','gramatica.py',583),
  ('exp_aritmetica -> exp_aritmetica DIVISION exp_aritmetica','exp_aritmetica',3,'p_exp_aritmetica','gramatica.py',584),
  ('exp_aritmetica -> exp_aritmetica MODULO exp_aritmetica','exp_aritmetica',3,'p_exp_aritmetica','gramatica.py',585),
  ('exp_aritmetica -> exp_aritmetica POTENCIA exp_aritmetica','exp_aritmetica',3,'p_exp_aritmetica','gramatica.py',586),
  ('exp_aritmetica -> exp_aritmetica BETWEEN exp_aritmetica AND exp_aritmetica','exp_aritmetica',5,'p_exp_aritmetica','gramatica.py',587),
  ('exp_aritmetica -> exp_aritmetica NOT BETWEEN exp_aritmetica AND exp_aritmetica','exp_aritmetica',6,'p_exp_aritmetica','gramatica.py',588),
  ('exp_aritmetica -> exp_aritmetica IN PARIZQUIERDO lista_expresiones PARDERECHO','exp_aritmetica',5,'p_exp_aritmetica','gramatica.py',589),
  ('exp_aritmetica -> exp_aritmetica NOT IN PARIZQUIERDO lista_expresiones PARDERECHO','exp_aritmetica',6,'p_exp_aritmetica','gramatica.py',590),
  ('exp_aritmetica -> exp_aritmetica LIKE exp_aritmetica','exp_aritmetica',3,'p_exp_aritmetica','gramatica.py',591),
  ('exp_aritmetica -> exp_aritmetica NOT LIKE exp_aritmetica','exp_aritmetica',4,'p_exp_aritmetica','gramatica.py',592),
  ('exp_aritmetica -> exp_aritmetica ILIKE exp_aritmetica','exp_aritmetica',3,'p_exp_aritmetica','gramatica.py',593),
  ('exp_aritmetica -> exp_aritmetica NOT ILIKE exp_aritmetica','exp_aritmetica',4,'p_exp_aritmetica','gramatica.py',594),
  ('exp_aritmetica -> exp_aritmetica SIMILAR TO exp_aritmetica','exp_aritmetica',4,'p_exp_aritmetica','gramatica.py',595),
  ('exp_aritmetica -> exp_aritmetica IS NULL','exp_aritmetica',3,'p_exp_aritmetica','gramatica.py',596),
  ('exp_aritmetica -> exp_aritmetica IS NOT NULL','exp_aritmetica',4,'p_exp_aritmetica','gramatica.py',597),
  ('exp_aritmetica -> primitivo','exp_aritmetica',1,'p_exp_aritmetica','gramatica.py',598),
  ('primitivo -> ID','primitivo',1,'p_primitivo_columna','gramatica.py',601),
  ('primitivo -> MAS primitivo','primitivo',2,'p_primitivo_primitivo','gramatica.py',616),
  ('primitivo -> MENOS primitivo','primitivo',2,'p_primitivo_primitivo','gramatica.py',617),
  ('primitivo -> PARIZQUIERDO exp_operacion PARDERECHO','primitivo',3,'p_primitivo_primitivo','gramatica.py',618),
  ('primitivo -> ENTERO','primitivo',1,'p_primitivo_entero','gramatica.py',648),
  ('primitivo -> DECIMAL','primitivo',1,'p_primitivo_decimal','gramatica.py',657),
  ('primitivo -> CADENA','primitivo',1,'p_primitivo_cadena','gramatica.py',669),
  ('primitivo -> TRUE','primitivo',1,'p_primitivo_booleano','gramatica.py',679),
  ('primitivo -> FALSE','primitivo',1,'p_primitivo_booleano','gramatica.py',680),
  ('update_table -> UPDATE ID SET lista_seteos PTCOMA','update_table',5,'p_instr_update_table','gramatica.py',698),
  ('update_table -> UPDATE ID SET lista_seteos WHERE exp_operacion PTCOMA','update_table',7,'p_instr_update_table','gramatica.py',699),
  ('lista_seteos -> lista_seteos COMA set_columna','lista_seteos',3,'p_lista_seteos','gramatica.py',722),
  ('lista_seteos -> set_columna','lista_seteos',1,'p_lista_seteos','gramatica.py',723),
  ('set_columna -> ID IGUAL exp_operacion','set_columna',3,'p_set_columna','gramatica.py',736),
]
