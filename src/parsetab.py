
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightNOTleftORleftANDleftQUESTIONCOLONnonassocLESS_THANGREATER_THANLESS_EQUALGREATER_EQUALEQUALNOT_EQUALleftPLUSMINUSleftTIMESDIVIDEMODULOrightUMINUSADD_ASSIGN AND ASSIGN BOOLEAN BREAK COLON COMMA CONTINUE DEF DIVIDE DIV_ASSIGN ELIF ELSE EQUAL FLOAT FOR GREATER_EQUAL GREATER_THAN IDENTIFIER IF IN INDENT INTEGER LBRACKET LESS_EQUAL LESS_THAN LPAREN MINUS MODULO MOD_ASSIGN MUL_ASSIGN NEWLINE NOT NOT_EQUAL NUMBER OR OUTDENT PLUS PRINT QUESTION RANGE RBRACKET RPAREN STRING STRING_LITERAL SUB_ASSIGN TIMES WHILE\n    program : statements\n    \n    statements : statements statement\n               | statement\n    \n    statement : assignment\n              | expression\n              | control_flow\n              | function_definition\n              | PRINT LPAREN expression RPAREN\n    \n    expression : expression PLUS expression\n               | expression MINUS expression\n               | expression TIMES expression\n               | expression DIVIDE expression\n               | expression MODULO expression\n               | expression GREATER_THAN expression\n               | expression LESS_THAN expression\n               | expression GREATER_EQUAL expression\n               | expression LESS_EQUAL expression\n               | expression EQUAL expression\n               | expression NOT_EQUAL expression\n    \n    expression : LPAREN expression RPAREN\n    \n    expression : INTEGER\n               | FLOAT\n    \n    expression : IDENTIFIER\n    \n    expression : STRING_LITERAL\n    \n    expression : BOOLEAN\n    \n    expression : MINUS expression %prec UMINUS\n               | NOT expression %prec NOT\n    \n    expression : expression QUESTION expression COLON expression\n    \n    assignment : IDENTIFIER ASSIGN expression\n               | IDENTIFIER ADD_ASSIGN expression\n               | IDENTIFIER SUB_ASSIGN expression\n               | IDENTIFIER MUL_ASSIGN expression\n               | IDENTIFIER DIV_ASSIGN expression\n               | IDENTIFIER MOD_ASSIGN expression\n    \n    expression : LBRACKET list_elements RBRACKET\n    \n    list_elements : list_elements COMMA expression\n                  | expression\n    \n    expression : expression LBRACKET slice RBRACKET\n    \n    slice : expression COLON expression COLON expression\n    \n    slice : expression COLON COLON expression\n    \n    slice : expression COLON expression\n    \n    slice : expression COLON\n    \n    slice : COLON COLON expression\n    \n    slice : COLON expression\n    \n    slice : COLON\n    \n    slice : expression\n    \n    expression : RANGE LPAREN range_args RPAREN\n    \n    range_args : expression COMMA expression COMMA expression\n    \n    range_args : expression COMMA expression\n    \n    range_args : expression\n    \n    control_flow : if_statement\n                 | while_statement\n                 | for_statement\n    \n    if_statement : IF expression COLON block ELSE COLON block\n                 | IF expression COLON block\n    \n    while_statement : WHILE expression COLON block\n    \n    for_statement : FOR IDENTIFIER IN expression COLON block\n    \n    block : INDENT statements OUTDENT\n    \n    function_definition : DEF IDENTIFIER LPAREN params RPAREN COLON block\n    \n    params : params COMMA IDENTIFIER\n           | IDENTIFIER\n           | empty\n    \n    empty :\n    \n    expression : IDENTIFIER LPAREN arguments RPAREN\n    \n    arguments : arguments COMMA expression\n              | expression\n              | empty\n    '
    
_lr_action_items = {'PRINT':([0,2,3,4,5,6,7,10,12,13,14,15,19,20,21,26,42,50,51,59,60,61,62,63,64,65,66,67,68,69,75,76,77,78,79,80,81,85,95,98,99,102,107,108,109,111,120,128,129,132,133,],[8,8,-3,-4,-5,-6,-7,-23,-21,-22,-24,-25,-51,-52,-53,-2,-23,-26,-27,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-29,-30,-31,-32,-33,-34,-35,-38,-8,-64,-47,-55,8,-56,-28,8,-58,-57,-59,-54,]),'IDENTIFIER':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,54,59,60,61,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,85,86,89,92,93,94,95,96,98,99,100,102,103,107,108,109,111,113,118,120,122,124,128,129,132,133,],[10,10,-3,-4,-5,-6,-7,42,-23,42,-21,-22,-24,-25,42,42,-51,-52,-53,55,42,42,58,-2,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-23,42,42,42,42,42,42,42,-26,-27,42,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,42,-20,-29,-30,-31,-32,-33,-34,-35,42,104,42,42,42,-38,42,-8,-64,42,-47,42,-55,10,-56,-28,42,126,10,42,42,-58,-57,-59,-54,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,54,55,59,60,61,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,85,86,92,93,94,95,96,98,99,100,102,103,107,108,109,111,113,120,122,124,128,129,132,133,],[9,9,-3,-4,-5,-6,-7,40,9,49,9,-21,-22,-24,-25,9,9,54,-51,-52,-53,9,9,-2,9,9,9,9,9,9,9,9,9,9,9,9,9,9,49,9,9,9,9,9,9,9,-26,-27,9,89,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,9,-20,-29,-30,-31,-32,-33,-34,-35,9,9,9,9,-38,9,-8,-64,9,-47,9,-55,9,-56,-28,9,9,9,9,-58,-57,-59,-54,]),'INTEGER':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,21,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,54,59,60,61,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,85,86,92,93,94,95,96,98,99,100,102,103,107,108,109,111,113,120,122,124,128,129,132,133,],[12,12,-3,-4,-5,-6,-7,12,-23,12,-21,-22,-24,-25,12,12,-51,-52,-53,12,12,-2,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-23,12,12,12,12,12,12,12,-26,-27,12,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,12,-20,-29,-30,-31,-32,-33,-34,-35,12,12,12,12,-38,12,-8,-64,12,-47,12,-55,12,-56,-28,12,12,12,12,-58,-57,-59,-54,]),'FLOAT':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,21,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,54,59,60,61,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,85,86,92,93,94,95,96,98,99,100,102,103,107,108,109,111,113,120,122,124,128,129,132,133,],[13,13,-3,-4,-5,-6,-7,13,-23,13,-21,-22,-24,-25,13,13,-51,-52,-53,13,13,-2,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-23,13,13,13,13,13,13,13,-26,-27,13,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,13,-20,-29,-30,-31,-32,-33,-34,-35,13,13,13,13,-38,13,-8,-64,13,-47,13,-55,13,-56,-28,13,13,13,13,-58,-57,-59,-54,]),'STRING_LITERAL':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,21,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,54,59,60,61,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,85,86,92,93,94,95,96,98,99,100,102,103,107,108,109,111,113,120,122,124,128,129,132,133,],[14,14,-3,-4,-5,-6,-7,14,-23,14,-21,-22,-24,-25,14,14,-51,-52,-53,14,14,-2,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-23,14,14,14,14,14,14,14,-26,-27,14,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,14,-20,-29,-30,-31,-32,-33,-34,-35,14,14,14,14,-38,14,-8,-64,14,-47,14,-55,14,-56,-28,14,14,14,14,-58,-57,-59,-54,]),'BOOLEAN':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,21,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,54,59,60,61,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,85,86,92,93,94,95,96,98,99,100,102,103,107,108,109,111,113,120,122,124,128,129,132,133,],[15,15,-3,-4,-5,-6,-7,15,-23,15,-21,-22,-24,-25,15,15,-51,-52,-53,15,15,-2,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-23,15,15,15,15,15,15,15,-26,-27,15,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,15,-20,-29,-30,-31,-32,-33,-34,-35,15,15,15,15,-38,15,-8,-64,15,-47,15,-55,15,-56,-28,15,15,15,15,-58,-57,-59,-54,]),'MINUS':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,21,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,75,76,77,78,79,80,81,83,85,86,88,92,93,94,95,96,97,98,99,100,101,102,103,107,108,109,110,111,112,113,114,115,116,120,122,123,124,128,129,130,131,132,133,],[11,11,-3,-4,28,-6,-7,11,-23,11,-21,-22,-24,-25,11,11,-51,-52,-53,11,11,-2,11,11,11,11,11,11,11,11,11,11,11,11,11,11,28,-23,11,11,11,11,11,11,11,-26,28,28,11,28,28,-9,-10,-11,-12,-13,28,28,28,28,28,28,28,28,11,28,-20,28,28,28,28,28,28,28,-35,11,28,11,11,11,-38,11,28,-8,-64,11,28,-47,11,-55,11,-56,28,28,28,11,28,28,28,11,11,28,11,-58,-57,28,28,-59,-54,]),'NOT':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,21,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,54,59,60,61,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,85,86,92,93,94,95,96,98,99,100,102,103,107,108,109,111,113,120,122,124,128,129,132,133,],[16,16,-3,-4,-5,-6,-7,16,-23,16,-21,-22,-24,-25,16,16,-51,-52,-53,16,16,-2,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-23,16,16,16,16,16,16,16,-26,-27,16,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,16,-20,-29,-30,-31,-32,-33,-34,-35,16,16,16,16,-38,16,-8,-64,16,-47,16,-55,16,-56,-28,16,16,16,16,-58,-57,-59,-54,]),'LBRACKET':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,21,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,75,76,77,78,79,80,81,83,85,86,88,92,93,94,95,96,97,98,99,100,101,102,103,107,108,109,110,111,112,113,114,115,116,120,122,123,124,128,129,130,131,132,133,],[17,17,-3,-4,39,-6,-7,17,-23,17,-21,-22,-24,-25,17,17,-51,-52,-53,17,17,-2,17,17,17,17,17,17,17,17,17,17,17,17,17,17,39,-23,17,17,17,17,17,17,17,-26,-27,39,17,39,39,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,39,39,17,39,-20,39,39,39,39,39,39,39,-35,17,39,17,17,17,-38,17,39,-8,-64,17,39,-47,17,-55,17,-56,39,-28,39,17,39,39,39,17,17,39,17,-58,-57,39,39,-59,-54,]),'RANGE':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,21,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,54,59,60,61,62,63,64,65,66,67,68,69,73,75,76,77,78,79,80,81,85,86,92,93,94,95,96,98,99,100,102,103,107,108,109,111,113,120,122,124,128,129,132,133,],[18,18,-3,-4,-5,-6,-7,18,-23,18,-21,-22,-24,-25,18,18,-51,-52,-53,18,18,-2,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-23,18,18,18,18,18,18,18,-26,-27,18,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,18,-20,-29,-30,-31,-32,-33,-34,-35,18,18,18,18,-38,18,-8,-64,18,-47,18,-55,18,-56,-28,18,18,18,18,-58,-57,-59,-54,]),'DEF':([0,2,3,4,5,6,7,10,12,13,14,15,19,20,21,26,42,50,51,59,60,61,62,63,64,65,66,67,68,69,75,76,77,78,79,80,81,85,95,98,99,102,107,108,109,111,120,128,129,132,133,],[22,22,-3,-4,-5,-6,-7,-23,-21,-22,-24,-25,-51,-52,-53,-2,-23,-26,-27,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-29,-30,-31,-32,-33,-34,-35,-38,-8,-64,-47,-55,22,-56,-28,22,-58,-57,-59,-54,]),'IF':([0,2,3,4,5,6,7,10,12,13,14,15,19,20,21,26,42,50,51,59,60,61,62,63,64,65,66,67,68,69,75,76,77,78,79,80,81,85,95,98,99,102,107,108,109,111,120,128,129,132,133,],[23,23,-3,-4,-5,-6,-7,-23,-21,-22,-24,-25,-51,-52,-53,-2,-23,-26,-27,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-29,-30,-31,-32,-33,-34,-35,-38,-8,-64,-47,-55,23,-56,-28,23,-58,-57,-59,-54,]),'WHILE':([0,2,3,4,5,6,7,10,12,13,14,15,19,20,21,26,42,50,51,59,60,61,62,63,64,65,66,67,68,69,75,76,77,78,79,80,81,85,95,98,99,102,107,108,109,111,120,128,129,132,133,],[24,24,-3,-4,-5,-6,-7,-23,-21,-22,-24,-25,-51,-52,-53,-2,-23,-26,-27,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-29,-30,-31,-32,-33,-34,-35,-38,-8,-64,-47,-55,24,-56,-28,24,-58,-57,-59,-54,]),'FOR':([0,2,3,4,5,6,7,10,12,13,14,15,19,20,21,26,42,50,51,59,60,61,62,63,64,65,66,67,68,69,75,76,77,78,79,80,81,85,95,98,99,102,107,108,109,111,120,128,129,132,133,],[25,25,-3,-4,-5,-6,-7,-23,-21,-22,-24,-25,-51,-52,-53,-2,-23,-26,-27,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-29,-30,-31,-32,-33,-34,-35,-38,-8,-64,-47,-55,25,-56,-28,25,-58,-57,-59,-54,]),'$end':([1,2,3,4,5,6,7,10,12,13,14,15,19,20,21,26,42,50,51,59,60,61,62,63,64,65,66,67,68,69,75,76,77,78,79,80,81,85,95,98,99,102,107,109,111,128,129,132,133,],[0,-1,-3,-4,-5,-6,-7,-23,-21,-22,-24,-25,-51,-52,-53,-2,-23,-26,-27,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-29,-30,-31,-32,-33,-34,-35,-38,-8,-64,-47,-55,-56,-28,-58,-57,-59,-54,]),'OUTDENT':([3,4,5,6,7,10,12,13,14,15,19,20,21,26,42,50,51,59,60,61,62,63,64,65,66,67,68,69,75,76,77,78,79,80,81,85,95,98,99,102,107,109,111,120,128,129,132,133,],[-3,-4,-5,-6,-7,-23,-21,-22,-24,-25,-51,-52,-53,-2,-23,-26,-27,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-29,-30,-31,-32,-33,-34,-35,-38,-8,-64,-47,-55,-56,-28,128,-58,-57,-59,-54,]),'PLUS':([5,10,12,13,14,15,41,42,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,85,88,95,97,99,101,102,110,111,112,114,115,116,123,130,131,],[27,-23,-21,-22,-24,-25,27,-23,-26,27,27,27,27,-9,-10,-11,-12,-13,27,27,27,27,27,27,27,27,27,-20,27,27,27,27,27,27,27,-35,27,-38,27,-64,27,-47,27,27,27,27,27,27,27,27,27,]),'TIMES':([5,10,12,13,14,15,41,42,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,85,88,95,97,99,101,102,110,111,112,114,115,116,123,130,131,],[29,-23,-21,-22,-24,-25,29,-23,-26,29,29,29,29,29,29,-11,-12,-13,29,29,29,29,29,29,29,29,29,-20,29,29,29,29,29,29,29,-35,29,-38,29,-64,29,-47,29,29,29,29,29,29,29,29,29,]),'DIVIDE':([5,10,12,13,14,15,41,42,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,85,88,95,97,99,101,102,110,111,112,114,115,116,123,130,131,],[30,-23,-21,-22,-24,-25,30,-23,-26,30,30,30,30,30,30,-11,-12,-13,30,30,30,30,30,30,30,30,30,-20,30,30,30,30,30,30,30,-35,30,-38,30,-64,30,-47,30,30,30,30,30,30,30,30,30,]),'MODULO':([5,10,12,13,14,15,41,42,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,85,88,95,97,99,101,102,110,111,112,114,115,116,123,130,131,],[31,-23,-21,-22,-24,-25,31,-23,-26,31,31,31,31,31,31,-11,-12,-13,31,31,31,31,31,31,31,31,31,-20,31,31,31,31,31,31,31,-35,31,-38,31,-64,31,-47,31,31,31,31,31,31,31,31,31,]),'GREATER_THAN':([5,10,12,13,14,15,41,42,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,85,88,95,97,99,101,102,110,111,112,114,115,116,123,130,131,],[32,-23,-21,-22,-24,-25,32,-23,-26,32,32,32,32,-9,-10,-11,-12,-13,None,None,None,None,None,None,32,32,32,-20,32,32,32,32,32,32,32,-35,32,-38,32,-64,32,-47,32,32,32,32,32,32,32,32,32,]),'LESS_THAN':([5,10,12,13,14,15,41,42,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,85,88,95,97,99,101,102,110,111,112,114,115,116,123,130,131,],[33,-23,-21,-22,-24,-25,33,-23,-26,33,33,33,33,-9,-10,-11,-12,-13,None,None,None,None,None,None,33,33,33,-20,33,33,33,33,33,33,33,-35,33,-38,33,-64,33,-47,33,33,33,33,33,33,33,33,33,]),'GREATER_EQUAL':([5,10,12,13,14,15,41,42,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,85,88,95,97,99,101,102,110,111,112,114,115,116,123,130,131,],[34,-23,-21,-22,-24,-25,34,-23,-26,34,34,34,34,-9,-10,-11,-12,-13,None,None,None,None,None,None,34,34,34,-20,34,34,34,34,34,34,34,-35,34,-38,34,-64,34,-47,34,34,34,34,34,34,34,34,34,]),'LESS_EQUAL':([5,10,12,13,14,15,41,42,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,85,88,95,97,99,101,102,110,111,112,114,115,116,123,130,131,],[35,-23,-21,-22,-24,-25,35,-23,-26,35,35,35,35,-9,-10,-11,-12,-13,None,None,None,None,None,None,35,35,35,-20,35,35,35,35,35,35,35,-35,35,-38,35,-64,35,-47,35,35,35,35,35,35,35,35,35,]),'EQUAL':([5,10,12,13,14,15,41,42,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,85,88,95,97,99,101,102,110,111,112,114,115,116,123,130,131,],[36,-23,-21,-22,-24,-25,36,-23,-26,36,36,36,36,-9,-10,-11,-12,-13,None,None,None,None,None,None,36,36,36,-20,36,36,36,36,36,36,36,-35,36,-38,36,-64,36,-47,36,36,36,36,36,36,36,36,36,]),'NOT_EQUAL':([5,10,12,13,14,15,41,42,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,85,88,95,97,99,101,102,110,111,112,114,115,116,123,130,131,],[37,-23,-21,-22,-24,-25,37,-23,-26,37,37,37,37,-9,-10,-11,-12,-13,None,None,None,None,None,None,37,37,37,-20,37,37,37,37,37,37,37,-35,37,-38,37,-64,37,-47,37,37,37,37,37,37,37,37,37,]),'QUESTION':([5,10,12,13,14,15,41,42,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,85,88,95,97,99,101,102,110,111,112,114,115,116,123,130,131,],[38,-23,-21,-22,-24,-25,38,-23,-26,38,38,38,38,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,38,38,38,-20,38,38,38,38,38,38,38,-35,38,-38,38,-64,38,-47,38,-28,38,38,38,38,38,38,38,]),'ASSIGN':([10,],[43,]),'ADD_ASSIGN':([10,],[44,]),'SUB_ASSIGN':([10,],[45,]),'MUL_ASSIGN':([10,],[46,]),'DIV_ASSIGN':([10,],[47,]),'MOD_ASSIGN':([10,],[48,]),'RPAREN':([12,13,14,15,41,42,49,50,51,59,60,61,62,63,64,65,66,67,68,69,74,75,82,83,84,85,87,88,89,95,99,102,104,105,106,111,115,116,126,131,],[-21,-22,-24,-25,75,-23,-63,-26,-27,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,98,-20,99,-66,-67,-35,102,-50,-63,-38,-64,-47,-61,117,-62,-28,-65,-49,-60,-48,]),'RBRACKET':([12,13,14,15,42,50,51,52,53,59,60,61,62,63,64,65,66,67,68,69,71,72,73,75,85,94,95,97,99,101,102,111,112,114,123,130,],[-21,-22,-24,-25,-23,-26,-27,85,-37,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-46,95,-45,-20,-35,-42,-38,-44,-64,-36,-47,-28,-41,-43,-40,-39,]),'COMMA':([12,13,14,15,42,49,50,51,52,53,59,60,61,62,63,64,65,66,67,68,69,75,82,83,84,85,88,89,95,99,101,102,104,105,106,111,115,116,126,],[-21,-22,-24,-25,-23,-63,-26,-27,86,-37,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,100,-66,-67,-35,103,-63,-38,-64,-36,-47,-61,118,-62,-28,-65,124,-60,]),'COLON':([12,13,14,15,39,42,50,51,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,73,75,85,94,95,99,102,110,111,112,117,119,],[-21,-22,-24,-25,73,-23,-26,-27,90,91,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,93,94,96,-20,-35,113,-38,-64,-47,121,-28,122,125,127,]),'IN':([58,],[92,]),'INDENT':([90,91,121,125,127,],[108,108,108,108,108,]),'ELSE':([107,128,],[119,-58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,108,],[2,120,]),'statement':([0,2,108,120,],[3,26,3,26,]),'assignment':([0,2,108,120,],[4,4,4,4,]),'expression':([0,2,9,11,16,17,23,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,45,46,47,48,49,54,73,86,92,93,94,96,100,103,108,113,120,122,124,],[5,5,41,50,51,53,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,74,76,77,78,79,80,81,83,88,97,101,110,111,112,114,115,116,5,123,5,130,131,]),'control_flow':([0,2,108,120,],[6,6,6,6,]),'function_definition':([0,2,108,120,],[7,7,7,7,]),'if_statement':([0,2,108,120,],[19,19,19,19,]),'while_statement':([0,2,108,120,],[20,20,20,20,]),'for_statement':([0,2,108,120,],[21,21,21,21,]),'list_elements':([17,],[52,]),'slice':([39,],[72,]),'arguments':([49,],[82,]),'empty':([49,89,],[84,106,]),'range_args':([54,],[87,]),'params':([89,],[105,]),'block':([90,91,121,125,127,],[107,109,129,132,133,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','parse.py',54),
  ('statements -> statements statement','statements',2,'p_statements','parse.py',61),
  ('statements -> statement','statements',1,'p_statements','parse.py',62),
  ('statement -> assignment','statement',1,'p_statement','parse.py',73),
  ('statement -> expression','statement',1,'p_statement','parse.py',74),
  ('statement -> control_flow','statement',1,'p_statement','parse.py',75),
  ('statement -> function_definition','statement',1,'p_statement','parse.py',76),
  ('statement -> PRINT LPAREN expression RPAREN','statement',4,'p_statement','parse.py',77),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parse.py',87),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parse.py',88),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parse.py',89),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parse.py',90),
  ('expression -> expression MODULO expression','expression',3,'p_expression_binop','parse.py',91),
  ('expression -> expression GREATER_THAN expression','expression',3,'p_expression_binop','parse.py',92),
  ('expression -> expression LESS_THAN expression','expression',3,'p_expression_binop','parse.py',93),
  ('expression -> expression GREATER_EQUAL expression','expression',3,'p_expression_binop','parse.py',94),
  ('expression -> expression LESS_EQUAL expression','expression',3,'p_expression_binop','parse.py',95),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_binop','parse.py',96),
  ('expression -> expression NOT_EQUAL expression','expression',3,'p_expression_binop','parse.py',97),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parse.py',104),
  ('expression -> INTEGER','expression',1,'p_expression_number','parse.py',111),
  ('expression -> FLOAT','expression',1,'p_expression_number','parse.py',112),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parse.py',119),
  ('expression -> STRING_LITERAL','expression',1,'p_expression_string','parse.py',126),
  ('expression -> BOOLEAN','expression',1,'p_expression_boolean','parse.py',133),
  ('expression -> MINUS expression','expression',2,'p_expression_negate','parse.py',140),
  ('expression -> NOT expression','expression',2,'p_expression_negate','parse.py',141),
  ('expression -> expression QUESTION expression COLON expression','expression',5,'p_expression_ternary','parse.py',150),
  ('assignment -> IDENTIFIER ASSIGN expression','assignment',3,'p_assignment','parse.py',157),
  ('assignment -> IDENTIFIER ADD_ASSIGN expression','assignment',3,'p_assignment','parse.py',158),
  ('assignment -> IDENTIFIER SUB_ASSIGN expression','assignment',3,'p_assignment','parse.py',159),
  ('assignment -> IDENTIFIER MUL_ASSIGN expression','assignment',3,'p_assignment','parse.py',160),
  ('assignment -> IDENTIFIER DIV_ASSIGN expression','assignment',3,'p_assignment','parse.py',161),
  ('assignment -> IDENTIFIER MOD_ASSIGN expression','assignment',3,'p_assignment','parse.py',162),
  ('expression -> LBRACKET list_elements RBRACKET','expression',3,'p_expression_list','parse.py',169),
  ('list_elements -> list_elements COMMA expression','list_elements',3,'p_list_elements','parse.py',176),
  ('list_elements -> expression','list_elements',1,'p_list_elements','parse.py',177),
  ('expression -> expression LBRACKET slice RBRACKET','expression',4,'p_expression_index_or_slicing','parse.py',188),
  ('slice -> expression COLON expression COLON expression','slice',5,'p_slice_full','parse.py',195),
  ('slice -> expression COLON COLON expression','slice',4,'p_slice_start_step','parse.py',202),
  ('slice -> expression COLON expression','slice',3,'p_slice_stop_step','parse.py',209),
  ('slice -> expression COLON','slice',2,'p_slice_start','parse.py',216),
  ('slice -> COLON COLON expression','slice',3,'p_slice_step','parse.py',223),
  ('slice -> COLON expression','slice',2,'p_slice_stop','parse.py',230),
  ('slice -> COLON','slice',1,'p_slice_empty','parse.py',237),
  ('slice -> expression','slice',1,'p_simple_index','parse.py',244),
  ('expression -> RANGE LPAREN range_args RPAREN','expression',4,'p_expression_range','parse.py',251),
  ('range_args -> expression COMMA expression COMMA expression','range_args',5,'p_range_args_three','parse.py',258),
  ('range_args -> expression COMMA expression','range_args',3,'p_range_args_two','parse.py',265),
  ('range_args -> expression','range_args',1,'p_range_args_one','parse.py',272),
  ('control_flow -> if_statement','control_flow',1,'p_control_flow','parse.py',279),
  ('control_flow -> while_statement','control_flow',1,'p_control_flow','parse.py',280),
  ('control_flow -> for_statement','control_flow',1,'p_control_flow','parse.py',281),
  ('if_statement -> IF expression COLON block ELSE COLON block','if_statement',7,'p_if_statement','parse.py',288),
  ('if_statement -> IF expression COLON block','if_statement',4,'p_if_statement','parse.py',289),
  ('while_statement -> WHILE expression COLON block','while_statement',4,'p_while_statement','parse.py',299),
  ('for_statement -> FOR IDENTIFIER IN expression COLON block','for_statement',6,'p_for_statement','parse.py',306),
  ('block -> INDENT statements OUTDENT','block',3,'p_block','parse.py',313),
  ('function_definition -> DEF IDENTIFIER LPAREN params RPAREN COLON block','function_definition',7,'p_function_definition','parse.py',320),
  ('params -> params COMMA IDENTIFIER','params',3,'p_params','parse.py',327),
  ('params -> IDENTIFIER','params',1,'p_params','parse.py',328),
  ('params -> empty','params',1,'p_params','parse.py',329),
  ('empty -> <empty>','empty',0,'p_empty','parse.py',339),
  ('expression -> IDENTIFIER LPAREN arguments RPAREN','expression',4,'p_expression_function_call','parse.py',346),
  ('arguments -> arguments COMMA expression','arguments',3,'p_arguments','parse.py',353),
  ('arguments -> expression','arguments',1,'p_arguments','parse.py',354),
  ('arguments -> empty','arguments',1,'p_arguments','parse.py',355),
]
