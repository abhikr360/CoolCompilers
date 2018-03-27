
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightGETSleftORleftANDrightNOTnonassocLTEQGTEQLTGTEQUALleftPLUSMINUSleftTIMESDIVIDEMODrightISVOIDrightTILDAleftATleftPERIODIMPORT CLASS INHERITS PUBLIC PRIVATE SEMICOLON COLON ID LSQRBRACKET RSQRBRACKET LPAREN RPAREN LBRACE RBRACE PERIOD OBJECT CLASS_TYPE INTEGER INTEGER_TYPE BOOL_TYPE STRING_TYPE SELF_TYPE STRING TRUE FALSE MOD TILDA GT LT EQUAL LTEQ GTEQ GETS OR AND NOT IF THEN ELSE FI WHILE LOOP POOL FOR LET TEL IN SELF BREAK CONTINUE ISVOID NEW PLUS MINUS TIMES DIVIDE COMMA ATstart : programprogram : imports classesprogram : classesimports : imports IMPORT ID SEMICOLONimports : IMPORT ID SEMICOLONclasses : classes class SEMICOLONclasses : class SEMICOLONclass : CLASS CLASS_TYPE INHERITS CLASS_TYPE LBRACE features_list RBRACEclass : CLASS CLASS_TYPE LBRACE features_list RBRACEclass : CLASS CLASS_TYPE INHERITS CLASS_TYPE LBRACE RBRACEclass : CLASS CLASS_TYPE LBRACE RBRACEfeatures_list : features_list feature SEMICOLONfeatures_list : feature SEMICOLONfeature : modifier ID LPAREN formal_parameter_list RPAREN COLON type LBRACE expression RBRACEfeature : modifier ID LPAREN RPAREN COLON type LBRACE expression RBRACEfeature : ID LPAREN formal_parameter_list RPAREN COLON type LBRACE expression RBRACEfeature : ID LPAREN RPAREN COLON type LBRACE expression RBRACEfeature : modifier formalfeature : formalmodifier : PUBLICmodifier : PRIVATEtype : CLASS_TYPEtype : INTEGER_TYPEtype : BOOL_TYPEtype : STRING_TYPEtype : OBJECTtype : SELF_TYPEformal_parameter_list : formal_parameter_list COMMA formal_parameterformal_parameter_list : formal_parameterformal_parameter : ID COLON typeformal_parameter : ID LSQRBRACKET RSQRBRACKET COLON typeformal : ID COLON type GETS expressionformal : ID COLON typeformal : ID COLON type LSQRBRACKET RSQRBRACKETexpression : block_expressionblock_expression : LBRACE block_list RBRACEblock_list : block_list expression SEMICOLONblock_list : expression SEMICOLONexpression : ID GETS expressionexpression : ID LSQRBRACKET expression RSQRBRACKET GETS expressionexpression : ID LPAREN argument_list RPARENexpression : ID LPAREN RPARENargument_list : expressionargument_list : argument_list COMMA expressionexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : expression TIMES expressionexpression : expression DIVIDE expressionexpression : expression MOD expressionexpression : expression LT expressionexpression : expression GT expressionexpression : expression LTEQ expressionexpression : expression GTEQ expressionexpression : expression EQUAL expressionexpression : expression OR expressionexpression : expression AND expressionexpression : NOT expressionexpression : TILDA expressionexpression : LPAREN expression RPARENexpression : SELFexpression : IDexpression : ID LSQRBRACKET expression RSQRBRACKETexpression : INTEGERexpression : STRINGexpression : TRUEexpression : FALSEexpression : BREAKexpression : CONTINUEexpression : expression PERIOD ID LPAREN argument_list RPARENexpression : expression PERIOD ID LPAREN RPARENexpression : NEW typeexpression : ISVOID expressionexpression : let_expressionlet_expression : LET formal IN expression TELexpression : expression AT CLASS_TYPE PERIOD ID LPAREN argument_list RPARENexpression : expression AT CLASS_TYPE PERIOD ID LPAREN RPARENexpression : if_then_elseif_then_else : IF expression THEN expression ELSE expression FIexpression : whilewhile : WHILE expression LOOP expression POOLexpression : forfor : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN LOOP expression POOL'
    
_lr_action_items = {'THEN':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,95,96,100,101,108,131,134,136,137,141,142,143,144,145,146,147,149,151,152,153,154,162,163,174,179,180,187,189,192,194,197,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,129,-71,-72,-58,-57,-42,-39,-59,-36,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,-62,-41,-80,-74,-70,-40,-69,-78,-76,-75,-82,]),'SELF_TYPE':([33,57,58,65,87,93,125,126,],[40,40,40,40,40,40,40,40,]),'GTEQ':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,109,109,109,-71,-72,-58,109,109,109,109,-42,109,109,109,-59,-36,109,None,None,-46,None,-45,None,-48,-47,109,None,109,-49,109,109,109,-62,-41,109,109,109,-80,109,109,-74,-70,109,109,109,-69,-78,109,-76,-75,109,-82,]),'OBJECT':([33,57,58,65,87,93,125,126,],[42,42,42,42,42,42,42,42,]),'STRING_TYPE':([33,57,58,65,87,93,125,126,],[43,43,43,43,43,43,43,43,]),'ELSE':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,96,100,101,108,131,134,136,137,141,142,143,144,145,146,147,149,151,152,153,154,161,162,163,174,179,180,187,189,192,194,197,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,-71,-72,-58,-57,-42,-39,-59,-36,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,175,-62,-41,-80,-74,-70,-40,-69,-78,-76,-75,-82,]),'WHILE':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-38,63,63,63,63,63,-37,63,63,63,63,63,63,63,]),'STRING':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-38,67,67,67,67,67,-37,67,67,67,67,67,67,67,]),'NEW':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,-38,65,65,65,65,65,-37,65,65,65,65,65,65,65,]),'FI':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,96,100,101,108,131,134,136,137,141,142,143,144,145,146,147,149,151,152,153,154,162,163,174,179,180,186,187,189,192,194,197,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,-71,-72,-58,-57,-42,-39,-59,-36,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,-62,-41,-80,-74,-70,192,-40,-69,-78,-76,-75,-82,]),'TRUE':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,-38,66,66,66,66,66,-37,66,66,66,66,66,66,66,]),'MINUS':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,111,111,111,-71,-72,-58,111,111,111,111,-42,111,111,111,-59,-36,111,111,111,-46,111,-45,111,-48,-47,111,111,111,-49,111,111,111,-62,-41,111,111,111,-80,111,111,-74,-70,111,111,111,-69,-78,111,-76,-75,111,-82,]),'BOOL_TYPE':([33,57,58,65,87,93,125,126,],[46,46,46,46,46,46,46,46,]),'DIVIDE':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,115,115,115,-71,-72,-58,115,115,115,115,-42,115,115,115,-59,-36,115,115,115,115,115,115,115,-48,-47,115,115,115,-49,115,115,115,-62,-41,115,115,115,-80,115,115,-74,-70,115,115,115,-69,-78,115,-76,-75,115,-82,]),'RPAREN':([34,40,41,42,43,44,46,47,49,51,60,62,66,67,68,69,74,75,77,78,79,80,81,82,88,90,96,98,100,101,103,108,131,132,133,134,136,137,141,142,143,144,145,146,147,149,151,152,153,154,157,162,163,168,174,177,179,180,181,187,189,190,192,193,194,195,197,200,],[48,-27,-22,-26,-25,-23,-24,55,-29,61,92,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,-28,-30,-71,131,-72,-58,136,-57,-42,163,-43,-39,-59,-36,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,-31,-62,-41,180,-80,-44,-74,-70,189,-40,-69,194,-78,196,-76,197,-75,-82,]),'SEMICOLON':([3,12,13,14,21,22,23,31,32,36,37,40,41,42,43,44,45,46,52,62,66,67,68,69,74,75,77,78,79,80,81,82,85,86,96,100,101,105,108,131,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,162,163,171,174,178,179,180,183,185,187,189,191,192,194,197,200,],[10,17,18,19,-11,-19,30,-9,39,-18,-10,-27,-22,-26,-25,-23,-33,-24,-8,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,-32,-34,-71,-72,-58,139,-57,-42,-39,165,-59,-36,166,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,-62,-41,-17,-80,188,-74,-70,-16,-15,-40,-69,-14,-78,-76,-75,-82,]),'PRIVATE':([16,25,29,30,38,39,],[24,24,24,-13,24,-12,]),'PLUS':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,113,113,113,-71,-72,-58,113,113,113,113,-42,113,113,113,-59,-36,113,113,113,-46,113,-45,113,-48,-47,113,113,113,-49,113,113,113,-62,-41,113,113,113,-80,113,113,-74,-70,113,113,113,-69,-78,113,-76,-75,113,-82,]),'ISVOID':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-38,70,70,70,70,70,-37,70,70,70,70,70,70,70,]),'INTEGER_TYPE':([33,57,58,65,87,93,125,126,],[44,44,44,44,44,44,44,44,]),'LT':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,112,112,112,-71,-72,-58,112,112,112,112,-42,112,112,112,-59,-36,112,None,None,-46,None,-45,None,-48,-47,112,None,112,-49,112,112,112,-62,-41,112,112,112,-80,112,112,-74,-70,112,112,112,-69,-78,112,-76,-75,112,-82,]),'TILDA':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-38,71,71,71,71,71,-37,71,71,71,71,71,71,71,]),'COLON':([27,35,48,50,55,61,91,92,106,],[33,33,57,58,87,93,125,126,33,]),'IMPORT':([0,2,18,19,],[7,9,-5,-4,]),'IN':([40,41,42,43,44,45,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,86,96,100,101,107,108,131,134,136,137,141,142,143,144,145,146,147,149,151,152,153,154,162,163,174,179,180,187,189,192,194,197,200,],[-27,-22,-26,-25,-23,-33,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,-32,-34,-71,-72,-58,140,-57,-42,-39,-59,-36,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,-62,-41,-80,-74,-70,-40,-69,-78,-76,-75,-82,]),'GETS':([40,41,42,43,44,45,46,69,162,],[-27,-22,-26,-25,-23,53,-24,99,176,]),'CLASS':([0,2,6,8,10,17,18,19,],[5,5,5,5,-7,-6,-5,-4,]),'$end':([1,4,6,8,10,17,],[-1,0,-3,-2,-7,-6,]),'INHERITS':([11,],[15,]),'AND':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,119,119,119,-71,-72,-58,119,119,-57,119,-42,119,119,119,-59,-36,119,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,119,-49,119,119,119,-62,-41,119,119,119,-80,119,119,-74,-70,119,119,119,-69,-78,119,-76,-75,119,-82,]),'GT':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,114,114,114,-71,-72,-58,114,114,114,114,-42,114,114,114,-59,-36,114,None,None,-46,None,-45,None,-48,-47,114,None,114,-49,114,114,114,-62,-41,114,114,114,-80,114,114,-74,-70,114,114,114,-69,-78,114,-76,-75,114,-82,]),'RBRACE':([16,25,29,30,38,39,40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,96,100,101,104,108,131,134,136,137,139,141,142,143,144,145,146,147,149,151,152,153,154,156,162,163,166,170,173,174,179,180,184,187,189,192,194,197,200,],[21,31,37,-13,52,-12,-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,-71,-72,-58,137,-57,-42,-39,-59,-36,-38,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,171,-62,-41,-37,183,185,-80,-74,-70,191,-40,-69,-78,-76,-75,-82,]),'FOR':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,-38,72,72,72,72,72,-37,72,72,72,72,72,72,72,]),'PERIOD':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,150,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,116,116,116,-71,116,116,116,116,116,116,-42,116,116,116,-59,-36,116,116,116,116,116,116,116,116,116,169,116,116,116,116,116,116,116,-62,-41,116,116,116,-80,116,116,-74,-70,116,116,116,-69,-78,116,-76,-75,116,-82,]),'EQUAL':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,110,110,110,-71,-72,-58,110,110,110,110,-42,110,110,110,-59,-36,110,None,None,-46,None,-45,None,-48,-47,110,None,110,-49,110,110,110,-62,-41,110,110,110,-80,110,110,-74,-70,110,110,110,-69,-78,110,-76,-75,110,-82,]),'AT':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,118,118,118,-71,118,118,118,118,118,118,-42,118,118,118,-59,-36,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,-62,-41,118,118,118,-80,118,118,-74,-70,118,118,118,-69,-78,118,-76,-75,118,-82,]),'LPAREN':([27,35,53,63,64,69,70,71,72,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,148,155,159,164,165,166,168,172,175,176,182,188,190,198,],[34,51,73,73,73,98,73,73,102,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,-38,73,168,73,73,73,73,-37,73,73,73,73,190,73,73,73,]),'RSQRBRACKET':([40,41,42,43,44,46,54,59,62,66,67,68,69,74,75,77,78,79,80,81,82,96,100,101,108,130,131,134,136,137,141,142,143,144,145,146,147,149,151,152,153,154,162,163,174,179,180,187,189,192,194,197,200,],[-27,-22,-26,-25,-23,-24,86,91,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,-71,-72,-58,-57,162,-42,-39,-59,-36,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,-62,-41,-80,-74,-70,-40,-69,-78,-76,-75,-82,]),'TEL':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,96,100,101,108,131,134,136,137,141,142,143,144,145,146,147,149,151,152,153,154,162,163,167,174,179,180,187,189,192,194,197,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,-71,-72,-58,-57,-42,-39,-59,-36,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,-62,-41,179,-80,-74,-70,-40,-69,-78,-76,-75,-82,]),'TIMES':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,117,117,117,-71,-72,-58,117,117,117,117,-42,117,117,117,-59,-36,117,117,117,117,117,117,117,-48,-47,117,117,117,-49,117,117,117,-62,-41,117,117,117,-80,117,117,-74,-70,117,117,117,-69,-78,117,-76,-75,117,-82,]),'ID':([7,9,16,24,25,26,28,29,30,34,38,39,51,53,56,63,64,70,71,73,76,83,84,97,98,99,102,104,109,110,111,112,113,114,115,116,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,169,172,175,176,188,190,198,],[13,14,27,-21,27,-20,35,27,-13,50,27,-12,50,69,50,69,69,69,69,69,69,106,69,69,69,69,69,69,69,69,69,69,69,69,69,148,69,69,69,69,69,69,69,69,-38,69,69,69,69,69,-37,69,182,69,69,69,69,69,69,]),'POOL':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,96,100,101,108,131,134,136,137,141,142,143,144,145,146,147,149,151,152,153,154,160,162,163,174,179,180,187,189,192,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,-71,-72,-58,-57,-42,-39,-59,-36,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,174,-62,-41,-80,-74,-70,-40,-69,-78,-76,-75,200,-82,]),'IF':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-38,64,64,64,64,64,-37,64,64,64,64,64,64,64,]),'LSQRBRACKET':([40,41,42,43,44,45,46,50,69,],[-27,-22,-26,-25,-23,54,-24,59,97,]),'LBRACE':([11,20,40,41,42,43,44,46,53,63,64,70,71,73,76,84,89,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,123,124,127,128,129,139,140,155,158,159,164,165,166,168,172,175,176,188,190,198,],[16,29,-27,-22,-26,-25,-23,-24,76,76,76,76,76,76,76,76,124,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,155,76,159,76,76,-38,76,76,172,76,76,76,-37,76,76,76,76,76,76,76,]),'FALSE':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,-38,77,77,77,77,77,-37,77,77,77,77,77,77,77,]),'CLASS_TYPE':([5,15,33,57,58,65,87,93,118,125,126,],[11,20,41,41,41,41,41,41,150,41,41,]),'INTEGER':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,-38,78,78,78,78,78,-37,78,78,78,78,78,78,78,]),'LTEQ':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,120,120,120,-71,-72,-58,120,120,120,120,-42,120,120,120,-59,-36,120,None,None,-46,None,-45,None,-48,-47,120,None,120,-49,120,120,120,-62,-41,120,120,120,-80,120,120,-74,-70,120,120,120,-69,-78,120,-76,-75,120,-82,]),'OR':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,121,121,121,-71,-72,-58,121,121,-57,121,-42,121,121,121,-59,-36,121,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,121,121,121,-62,-41,121,121,121,-80,121,121,-74,-70,121,121,121,-69,-78,121,-76,-75,121,-82,]),'BREAK':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,-38,79,79,79,79,79,-37,79,79,79,79,79,79,79,]),'SELF':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,-38,80,80,80,80,80,-37,80,80,80,80,80,80,80,]),'CONTINUE':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,-38,82,82,82,82,82,-37,82,82,82,82,82,82,82,]),'LET':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,-38,83,83,83,83,83,-37,83,83,83,83,83,83,83,]),'NOT':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,139,140,155,159,164,165,166,168,172,175,176,188,190,198,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,-38,84,84,84,84,84,-37,84,84,84,84,84,84,84,]),'COMMA':([40,41,42,43,44,46,47,49,60,62,66,67,68,69,74,75,77,78,79,80,81,82,88,90,96,100,101,108,131,132,133,134,136,137,141,142,143,144,145,146,147,149,151,152,153,154,157,162,163,174,177,179,180,181,187,189,192,194,195,197,200,],[-27,-22,-26,-25,-23,-24,56,-29,56,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,-28,-30,-71,-72,-58,-57,-42,164,-43,-39,-59,-36,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,-31,-62,-41,-80,-44,-74,-70,164,-40,-69,-78,-76,164,-75,-82,]),'PUBLIC':([16,25,29,30,38,39,],[26,26,26,-13,26,-12,]),'LOOP':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,94,96,100,101,108,131,134,136,137,141,142,143,144,145,146,147,149,151,152,153,154,162,163,174,179,180,187,189,192,194,196,197,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,128,-71,-72,-58,-57,-42,-39,-59,-36,-53,-54,-46,-50,-45,-51,-48,-47,-56,-52,-55,-49,-62,-41,-80,-74,-70,-40,-69,-78,-76,198,-75,-82,]),'MOD':([40,41,42,43,44,46,62,66,67,68,69,74,75,77,78,79,80,81,82,85,94,95,96,100,101,103,105,108,130,131,133,134,135,136,137,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,162,163,167,170,173,174,177,178,179,180,184,186,187,189,192,193,194,197,199,200,],[-27,-22,-26,-25,-23,-24,-73,-65,-64,-81,-61,-35,-77,-66,-63,-67,-60,-79,-68,122,122,122,-71,-72,-58,122,122,122,122,-42,122,122,122,-59,-36,122,122,122,122,122,122,122,-48,-47,122,122,122,-49,122,122,122,-62,-41,122,122,122,-80,122,122,-74,-70,122,122,122,-69,-78,122,-76,-75,122,-82,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'block_list':([76,],[104,]),'formal_parameter_list':([34,51,],[47,60,]),'modifier':([16,25,29,38,],[28,28,28,28,]),'for':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,140,155,159,164,165,168,172,175,176,188,190,198,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'formal_parameter':([34,51,56,],[49,49,88,]),'imports':([0,],[2,]),'let_expression':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,140,155,159,164,165,168,172,175,176,188,190,198,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'features_list':([16,29,],[25,38,]),'if_then_else':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,140,155,159,164,165,168,172,175,176,188,190,198,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'feature':([16,25,29,38,],[23,32,23,32,]),'argument_list':([98,168,190,],[132,181,195,]),'start':([0,],[4,]),'while':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,140,155,159,164,165,168,172,175,176,188,190,198,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'program':([0,],[1,]),'expression':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,140,155,159,164,165,168,172,175,176,188,190,198,],[85,94,95,100,101,103,105,108,130,133,134,135,138,141,142,143,144,145,146,147,149,151,152,153,154,156,160,161,167,170,173,177,178,133,184,186,187,193,133,199,]),'block_expression':([53,63,64,70,71,73,76,84,97,98,99,102,104,109,110,111,112,113,114,115,117,119,120,121,122,124,128,129,140,155,159,164,165,168,172,175,176,188,190,198,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'classes':([0,2,],[6,8,]),'type':([33,57,58,65,87,93,125,126,],[45,89,90,96,123,127,157,158,]),'class':([0,2,6,8,],[3,3,12,12,]),'formal':([16,25,28,29,38,83,],[22,22,36,22,22,107,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> program','start',1,'p_start','parser',25),
  ('program -> imports classes','program',2,'p_program_with_imports','parser',29),
  ('program -> classes','program',1,'p_program','parser',33),
  ('imports -> imports IMPORT ID SEMICOLON','imports',4,'p_imports_multiple','parser',37),
  ('imports -> IMPORT ID SEMICOLON','imports',3,'p_imports','parser',41),
  ('classes -> classes class SEMICOLON','classes',3,'p_classes_multiple','parser',46),
  ('classes -> class SEMICOLON','classes',2,'p_classes','parser',51),
  ('class -> CLASS CLASS_TYPE INHERITS CLASS_TYPE LBRACE features_list RBRACE','class',7,'p_class_with_inheritance_with_features_list','parser',55),
  ('class -> CLASS CLASS_TYPE LBRACE features_list RBRACE','class',5,'p_class_with_features_list','parser',59),
  ('class -> CLASS CLASS_TYPE INHERITS CLASS_TYPE LBRACE RBRACE','class',6,'p_class_with_features_inheritance','parser',63),
  ('class -> CLASS CLASS_TYPE LBRACE RBRACE','class',4,'p_class','parser',67),
  ('features_list -> features_list feature SEMICOLON','features_list',3,'p_features_list_mult','parser',71),
  ('features_list -> feature SEMICOLON','features_list',2,'p_features_list','parser',75),
  ('feature -> modifier ID LPAREN formal_parameter_list RPAREN COLON type LBRACE expression RBRACE','feature',10,'p_feature_with_modifier_with_formal_parameter_list','parser',79),
  ('feature -> modifier ID LPAREN RPAREN COLON type LBRACE expression RBRACE','feature',9,'p_feature_with_modifier','parser',83),
  ('feature -> ID LPAREN formal_parameter_list RPAREN COLON type LBRACE expression RBRACE','feature',9,'p_feature_with_formal_parameter_list','parser',87),
  ('feature -> ID LPAREN RPAREN COLON type LBRACE expression RBRACE','feature',8,'p_feature','parser',91),
  ('feature -> modifier formal','feature',2,'p_feature_modifier_formal','parser',95),
  ('feature -> formal','feature',1,'p_feature_formal','parser',99),
  ('modifier -> PUBLIC','modifier',1,'p_modifier_public','parser',103),
  ('modifier -> PRIVATE','modifier',1,'p_modifier_private','parser',107),
  ('type -> CLASS_TYPE','type',1,'p_type_class_type','parser',111),
  ('type -> INTEGER_TYPE','type',1,'p_type_integer_type','parser',115),
  ('type -> BOOL_TYPE','type',1,'p_type_bool_type','parser',119),
  ('type -> STRING_TYPE','type',1,'p_type_string_type','parser',123),
  ('type -> OBJECT','type',1,'p_type_object','parser',127),
  ('type -> SELF_TYPE','type',1,'p_type_self_type','parser',131),
  ('formal_parameter_list -> formal_parameter_list COMMA formal_parameter','formal_parameter_list',3,'p_formal_parameter_list_many','parser',135),
  ('formal_parameter_list -> formal_parameter','formal_parameter_list',1,'p_formal_parameter_list','parser',139),
  ('formal_parameter -> ID COLON type','formal_parameter',3,'p_formal_parameter','parser',143),
  ('formal_parameter -> ID LSQRBRACKET RSQRBRACKET COLON type','formal_parameter',5,'p_formal_parameter_arr','parser',147),
  ('formal -> ID COLON type GETS expression','formal',5,'p_formal_with_assign','parser',151),
  ('formal -> ID COLON type','formal',3,'p_formal','parser',155),
  ('formal -> ID COLON type LSQRBRACKET RSQRBRACKET','formal',5,'p_formal_arr','parser',159),
  ('expression -> block_expression','expression',1,'p_expression_block_expression','parser',164),
  ('block_expression -> LBRACE block_list RBRACE','block_expression',3,'p_block_expression','parser',169),
  ('block_list -> block_list expression SEMICOLON','block_list',3,'p_block_list_many','parser',173),
  ('block_list -> expression SEMICOLON','block_list',2,'p_block_list','parser',177),
  ('expression -> ID GETS expression','expression',3,'p_expression_assign','parser',182),
  ('expression -> ID LSQRBRACKET expression RSQRBRACKET GETS expression','expression',6,'p_expression_assign_arr','parser',186),
  ('expression -> ID LPAREN argument_list RPAREN','expression',4,'p_expression_function_call_with_arguments_2','parser',190),
  ('expression -> ID LPAREN RPAREN','expression',3,'p_expression_function_call_2','parser',194),
  ('argument_list -> expression','argument_list',1,'p_argument_list','parser',199),
  ('argument_list -> argument_list COMMA expression','argument_list',3,'p_argument_list_many','parser',203),
  ('expression -> expression PLUS expression','expression',3,'p_expression_plus','parser',208),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','parser',212),
  ('expression -> expression TIMES expression','expression',3,'p_expression_times','parser',216),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_divide','parser',220),
  ('expression -> expression MOD expression','expression',3,'p_expression_mod','parser',224),
  ('expression -> expression LT expression','expression',3,'p_expression_lt','parser',228),
  ('expression -> expression GT expression','expression',3,'p_expression_gt','parser',232),
  ('expression -> expression LTEQ expression','expression',3,'p_expression_lteq','parser',236),
  ('expression -> expression GTEQ expression','expression',3,'p_expression_gteq','parser',240),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_equal','parser',244),
  ('expression -> expression OR expression','expression',3,'p_expression_or','parser',248),
  ('expression -> expression AND expression','expression',3,'p_expression_and','parser',252),
  ('expression -> NOT expression','expression',2,'p_expression_not','parser',256),
  ('expression -> TILDA expression','expression',2,'p_expression_tilda','parser',260),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','parser',264),
  ('expression -> SELF','expression',1,'p_expression_self','parser',268),
  ('expression -> ID','expression',1,'p_expression_id','parser',272),
  ('expression -> ID LSQRBRACKET expression RSQRBRACKET','expression',4,'p_expression_arr','parser',276),
  ('expression -> INTEGER','expression',1,'p_expression_integer','parser',280),
  ('expression -> STRING','expression',1,'p_expression_string','parser',284),
  ('expression -> TRUE','expression',1,'p_expression_true','parser',288),
  ('expression -> FALSE','expression',1,'p_expression_false','parser',292),
  ('expression -> BREAK','expression',1,'p_expression_break','parser',296),
  ('expression -> CONTINUE','expression',1,'p_expression_continue','parser',300),
  ('expression -> expression PERIOD ID LPAREN argument_list RPAREN','expression',6,'p_expression_function_call_with_arguments','parser',304),
  ('expression -> expression PERIOD ID LPAREN RPAREN','expression',5,'p_expression_function_call','parser',308),
  ('expression -> NEW type','expression',2,'p_expression_new','parser',312),
  ('expression -> ISVOID expression','expression',2,'p_expression_isvoid','parser',316),
  ('expression -> let_expression','expression',1,'p_expression_let_expression','parser',320),
  ('let_expression -> LET formal IN expression TEL','let_expression',5,'p_let_expression','parser',324),
  ('expression -> expression AT CLASS_TYPE PERIOD ID LPAREN argument_list RPAREN','expression',8,'p_expression_at_function_with_arguments','parser',330),
  ('expression -> expression AT CLASS_TYPE PERIOD ID LPAREN RPAREN','expression',7,'p_expression_at_function','parser',334),
  ('expression -> if_then_else','expression',1,'p_expression_if_then_else','parser',339),
  ('if_then_else -> IF expression THEN expression ELSE expression FI','if_then_else',7,'p_if_then_else','parser',343),
  ('expression -> while','expression',1,'p_expression_while','parser',347),
  ('while -> WHILE expression LOOP expression POOL','while',5,'p_while','parser',351),
  ('expression -> for','expression',1,'p_expression_for','parser',355),
  ('for -> FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN LOOP expression POOL','for',11,'p_for','parser',359),
]
