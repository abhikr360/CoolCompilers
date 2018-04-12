
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightGETSleftORleftANDrightNOTnonassocLTEQGTEQLTGTEQUALleftPLUSMINUSleftTIMESDIVIDEMODrightISVOIDrightTILDAleftATleftPERIODIMPORT CLASS INHERITS PUBLIC PRIVATE SEMICOLON COLON ID LSQRBRACKET RSQRBRACKET LPAREN RPAREN LBRACE RBRACE PERIOD DEF RETURN OBJECT CLASS_TYPE INTEGER INTEGER_TYPE BOOL_TYPE STRING_TYPE SELF_TYPE STRING TRUE FALSE MOD TILDA GT LT EQUAL LTEQ GTEQ GETS OR AND NOT IF THEN ELSE FI WHILE LOOP POOL FOR LET TEL IN SELF BREAK CONTINUE ISVOID NEW PLUS MINUS TIMES DIVIDE COMMA ATstart : programprogram : imports classesprogram : classesimports : imports IMPORT ID SEMICOLONimports : IMPORT ID SEMICOLONclasses : classes class SEMICOLONclasses : class SEMICOLONclass : class_header class_bodyclass_header : CLASS CLASS_TYPE INHERITS CLASS_TYPEclass_header : CLASS CLASS_TYPEclass_body : LBRACE RBRACEclass_body : LBRACE features_list RBRACEfeatures_list : features_list feature SEMICOLONfeatures_list : feature SEMICOLONfeature : feature_header feature_bodyfeature_header : DEF modifier ID COLON typefeature_header : DEF ID COLON typefeature_body : LPAREN formal_parameter_list RPAREN LBRACE expression RBRACEfeature_body : LPAREN RPAREN LBRACE expression RBRACEfeature : modifier formalfeature : formalmodifier : PUBLICmodifier : PRIVATEtype : CLASS_TYPEtype : INTEGER_TYPEtype : BOOL_TYPEtype : STRING_TYPEtype : OBJECTtype : SELF_TYPEformal_parameter_list : formal_parameter_list COMMA formal_parameterformal_parameter_list : formal_parameterformal_parameter : ID COLON typeformal_parameter : ID LSQRBRACKET RSQRBRACKET COLON typeformal : ID COLON type GETS expressionformal : ID COLON typeformal : ID COLON type LSQRBRACKET expression RSQRBRACKETexpression : block_expressionblock_expression : LBRACE block_list RBRACEblock_list : block_list expression SEMICOLONblock_list : expression SEMICOLONexpression : ID GETS expressionexpression : ID LSQRBRACKET expression RSQRBRACKET GETS expressionexpression : ID LPAREN argument_list RPARENexpression : ID LPAREN RPARENargument_list : expressionargument_list : argument_list COMMA expressionexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : expression TIMES expressionexpression : expression DIVIDE expressionexpression : expression MOD expressionexpression : expression LT expressionexpression : expression GT expressionexpression : expression LTEQ expressionexpression : expression GTEQ expressionexpression : expression EQUAL expressionexpression : expression OR expressionexpression : expression AND expressionexpression : NOT expressionexpression : TILDA expressionexpression : LPAREN expression RPARENexpression : SELFexpression : IDexpression : ID LSQRBRACKET expression RSQRBRACKETexpression : INTEGERexpression : STRINGexpression : TRUEexpression : FALSEexpression : BREAKexpression : CONTINUEexpression : RETURN expression SEMICOLONexpression : expression PERIOD ID LPAREN argument_list RPARENexpression : expression PERIOD ID LPAREN RPARENexpression : NEW typeexpression : ISVOID expressionexpression : let_expressionlet : LETlet_expression : let formaldehyde IN expression TELexpression : expression AT CLASS_TYPE PERIOD ID LPAREN argument_list RPARENexpression : expression AT CLASS_TYPE PERIOD ID LPAREN RPARENexpression : if_then_elseif_then_else : IF expression THEN expression ELSE expression FIexpression : whilewhile : WHILE expression LOOP expression POOLexpression : forfor : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN LOOP expression POOLformaldehyde : formaldehyde COMMA ID COLON type GETS expressionformaldehyde : formaldehyde COMMA ID COLON typeformaldehyde : formaldehyde COMMA ID COLON type LSQRBRACKET expression RSQRBRACKETformaldehyde : ID COLON type GETS expressionformaldehyde : ID COLON typeformaldehyde : ID COLON type LSQRBRACKET expression RSQRBRACKET'
    
_lr_action_items = {'THEN':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,101,102,106,107,114,133,137,140,145,146,149,150,151,152,153,154,155,157,159,160,161,162,166,167,176,181,185,189,194,196,201,206,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,135,-74,-75,-60,-59,-71,-44,-41,-61,-38,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,-64,-43,-84,-78,-73,-42,-72,-82,-80,-79,-86,]),'SELF_TYPE':([39,55,59,63,71,130,144,182,],[47,47,47,47,47,47,47,47,]),'GTEQ':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,115,115,115,115,115,115,115,-74,-75,-60,115,115,115,-71,115,-44,115,115,115,-61,-38,115,None,None,-48,-50,None,-47,None,-49,115,None,115,-51,115,115,-64,-43,115,-84,115,115,-78,-73,115,115,115,115,-72,-82,115,-80,115,115,-79,115,-86,]),'OBJECT':([39,55,59,63,71,130,144,182,],[49,49,49,49,49,49,49,49,]),'STRING_TYPE':([39,55,59,63,71,130,144,182,],[50,50,50,50,50,50,50,50,]),'ELSE':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,102,106,107,114,133,137,140,145,146,149,150,151,152,153,154,155,157,159,160,161,162,165,166,167,176,181,185,189,194,196,201,206,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,-74,-75,-60,-59,-71,-44,-41,-61,-38,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,177,-64,-43,-84,-78,-73,-42,-72,-82,-80,-79,-86,]),'WHILE':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,-40,69,69,-39,69,69,69,69,69,69,69,69,69,69,]),'STRING':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,-40,77,77,-39,77,77,77,77,77,77,77,77,77,77,]),'IF':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-40,70,70,-39,70,70,70,70,70,70,70,70,70,70,]),'NEW':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-40,71,71,-39,71,71,71,71,71,71,71,71,71,71,]),'FI':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,102,106,107,114,133,137,140,145,146,149,150,151,152,153,154,155,157,159,160,161,162,166,167,176,181,185,188,189,194,196,201,206,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,-74,-75,-60,-59,-71,-44,-41,-61,-38,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,-64,-43,-84,-78,-73,196,-42,-72,-82,-80,-79,-86,]),'TRUE':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,-40,72,72,-39,72,72,72,72,72,72,72,72,72,72,]),'MINUS':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,117,117,117,117,117,117,117,-74,-75,-60,117,117,117,-71,117,-44,117,117,117,-61,-38,117,117,117,-48,-50,117,-47,117,-49,117,117,117,-51,117,117,-64,-43,117,-84,117,117,-78,-73,117,117,117,117,-72,-82,117,-80,117,117,-79,117,-86,]),'BOOL_TYPE':([39,55,59,63,71,130,144,182,],[53,53,53,53,53,53,53,53,]),'DIVIDE':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,118,118,118,118,118,118,118,-74,-75,-60,118,118,118,-71,118,-44,118,118,118,-61,-38,118,118,118,118,-50,118,118,118,-49,118,118,118,-51,118,118,-64,-43,118,-84,118,118,-78,-73,118,118,118,118,-72,-82,118,-80,118,118,-79,118,-86,]),'RPAREN':([37,43,45,47,48,49,50,51,53,66,68,72,73,76,77,79,82,83,85,86,87,88,89,93,102,104,106,107,111,114,133,137,138,139,140,145,146,149,150,151,152,153,154,155,157,159,160,161,162,163,166,167,174,176,179,181,185,186,189,194,195,196,197,201,202,206,210,],[44,56,-31,-29,-24,-28,-27,-25,-26,-30,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,-32,-74,137,-75,-60,145,-59,-71,-44,167,-45,-41,-61,-38,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,-33,-64,-43,185,-84,-46,-78,-73,194,-42,-72,201,-82,203,-80,206,-79,-86,]),'SEMICOLON':([3,13,14,16,17,21,22,30,34,35,36,38,47,48,49,50,51,52,53,68,72,73,76,77,79,82,83,85,86,87,88,89,95,99,102,106,107,113,114,122,131,132,133,137,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,166,167,176,180,181,185,189,194,196,201,206,210,],[11,19,20,-8,31,-11,33,-21,-12,42,-15,-20,-29,-24,-28,-27,-25,-35,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,-34,133,-74,-75,-60,148,-59,-19,-36,-18,-71,-44,-41,169,-61,-38,173,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,-64,-43,-84,190,-78,-73,-42,-72,-82,-80,-79,-86,]),'PRIVATE':([15,24,29,33,42,],[23,23,23,-14,-13,]),'ID':([7,10,15,23,24,25,27,29,33,37,40,42,57,58,61,62,65,67,69,70,74,75,80,81,84,90,91,103,104,105,108,112,115,116,117,118,119,120,121,123,124,126,127,128,129,134,135,142,143,148,168,169,173,174,175,177,178,183,184,190,195,198,199,207,],[14,17,28,-23,28,-22,28,41,-14,46,54,-13,46,73,73,73,73,73,73,73,73,73,110,73,73,-77,73,73,73,73,73,73,73,73,73,73,73,73,73,156,73,73,73,73,73,73,73,73,171,-40,73,73,-39,73,187,73,73,73,73,73,73,73,73,73,]),'ISVOID':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,-40,74,74,-39,74,74,74,74,74,74,74,74,74,74,]),'INTEGER_TYPE':([39,55,59,63,71,130,144,182,],[51,51,51,51,51,51,51,51,]),'LT':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,119,119,119,119,119,119,119,-74,-75,-60,119,119,119,-71,119,-44,119,119,119,-61,-38,119,None,None,-48,-50,None,-47,None,-49,119,None,119,-51,119,119,-64,-43,119,-84,119,119,-78,-73,119,119,119,119,-72,-82,119,-80,119,119,-79,119,-86,]),'TILDA':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,-40,75,75,-39,75,75,75,75,75,75,75,75,75,75,]),'COLON':([28,41,46,54,94,110,171,],[39,55,59,63,130,144,182,]),'DEF':([15,24,33,42,],[29,29,-14,-13,]),'IMPORT':([0,2,20,31,],[7,10,-5,-4,]),'IN':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,102,106,107,109,114,133,137,140,145,146,149,150,151,152,153,154,155,157,159,160,161,162,166,167,172,176,181,185,189,191,192,194,196,200,201,205,206,208,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,-74,-75,-60,142,-59,-71,-44,-41,-61,-38,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,-64,-43,-91,-84,-78,-73,-42,-88,-90,-72,-82,-92,-80,-87,-79,-89,-86,]),'GETS':([47,48,49,50,51,52,53,73,166,172,191,],[-29,-24,-28,-27,-25,61,-26,105,178,183,199,]),'CLASS':([0,2,6,9,11,19,20,31,],[5,5,5,5,-7,-6,-5,-4,]),'$end':([1,4,6,9,11,19,],[-1,0,-3,-2,-7,-6,]),'INHERITS':([12,],[18,]),'GT':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,121,121,121,121,121,121,121,-74,-75,-60,121,121,121,-71,121,-44,121,121,121,-61,-38,121,None,None,-48,-50,None,-47,None,-49,121,None,121,-51,121,121,-64,-43,121,-84,121,121,-78,-73,121,121,121,121,-72,-82,121,-80,121,121,-79,121,-86,]),'RBRACE':([15,24,33,42,47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,98,102,106,107,112,114,133,137,140,145,146,148,149,150,151,152,153,154,155,157,159,160,161,162,166,167,173,176,181,185,189,194,196,201,206,210,],[21,34,-14,-13,-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,122,132,-74,-75,-60,146,-59,-71,-44,-41,-61,-38,-40,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,-64,-43,-39,-84,-78,-73,-42,-72,-82,-80,-79,-86,]),'FOR':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,-40,78,78,-39,78,78,78,78,78,78,78,78,78,78,]),'PERIOD':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,158,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,123,123,123,123,123,123,123,-74,123,123,123,123,123,-71,123,-44,123,123,123,-61,-38,123,123,123,123,123,123,123,123,123,175,123,123,123,123,123,123,-64,-43,123,-84,123,123,-78,-73,123,123,123,123,-72,-82,123,-80,123,123,-79,123,-86,]),'EQUAL':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,116,116,116,116,116,116,116,-74,-75,-60,116,116,116,-71,116,-44,116,116,116,-61,-38,116,None,None,-48,-50,None,-47,None,-49,116,None,116,-51,116,116,-64,-43,116,-84,116,116,-78,-73,116,116,116,116,-72,-82,116,-80,116,116,-79,116,-86,]),'AT':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,125,125,125,125,125,125,125,-74,125,125,125,125,125,-71,125,-44,125,125,125,-61,-38,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,-64,-43,125,-84,125,125,-78,-73,125,125,125,125,-72,-82,125,-80,125,125,-79,125,-86,]),'LPAREN':([26,47,48,49,50,51,53,58,61,62,64,65,67,69,70,73,74,75,78,81,84,91,97,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,156,168,169,173,174,177,178,183,184,187,190,195,198,199,207,],[37,-29,-24,-28,-27,-25,-26,81,81,81,-17,81,81,81,81,104,81,81,108,81,81,81,-16,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,-40,174,81,81,-39,81,81,81,81,81,195,81,81,81,81,81,]),'RSQRBRACKET':([47,48,49,50,51,53,60,68,72,73,76,77,79,82,83,85,86,87,88,89,96,102,106,107,114,133,136,137,140,145,146,149,150,151,152,153,154,155,157,159,160,161,162,166,167,176,181,185,189,193,194,196,201,204,206,210,],[-29,-24,-28,-27,-25,-26,94,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,131,-74,-75,-60,-59,-71,166,-44,-41,-61,-38,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,-64,-43,-84,-78,-73,-42,200,-72,-82,-80,208,-79,-86,]),'TEL':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,102,106,107,114,133,137,140,145,146,149,150,151,152,153,154,155,157,159,160,161,162,166,167,170,176,181,185,189,194,196,201,206,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,-74,-75,-60,-59,-71,-44,-41,-61,-38,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,-64,-43,181,-84,-78,-73,-42,-72,-82,-80,-79,-86,]),'TIMES':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,124,124,124,124,124,124,124,-74,-75,-60,124,124,124,-71,124,-44,124,124,124,-61,-38,124,124,124,124,-50,124,124,124,-49,124,124,124,-51,124,124,-64,-43,124,-84,124,124,-78,-73,124,124,124,124,-72,-82,124,-80,124,124,-79,124,-86,]),'LSQRBRACKET':([46,47,48,49,50,51,52,53,73,172,191,],[60,-29,-24,-28,-27,-25,62,-26,103,184,198,]),'POOL':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,102,106,107,114,133,137,140,145,146,149,150,151,152,153,154,155,157,159,160,161,162,164,166,167,176,181,185,189,194,196,201,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,-74,-75,-60,-59,-71,-44,-41,-61,-38,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,176,-64,-43,-84,-78,-73,-42,-72,-82,-80,-79,210,-86,]),'PLUS':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,120,120,120,120,120,120,120,-74,-75,-60,120,120,120,-71,120,-44,120,120,120,-61,-38,120,120,120,-48,-50,120,-47,120,-49,120,120,120,-51,120,120,-64,-43,120,-84,120,120,-78,-73,120,120,120,120,-72,-82,120,-80,120,120,-79,120,-86,]),'AND':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,126,126,126,126,126,126,126,-74,-75,-60,126,126,-59,-71,126,-44,126,126,126,-61,-38,126,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,126,-51,126,126,-64,-43,126,-84,126,126,-78,-73,126,126,126,126,-72,-82,126,-80,126,126,-79,126,-86,]),'RETURN':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-40,67,67,-39,67,67,67,67,67,67,67,67,67,67,]),'LBRACE':([8,12,32,44,56,58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[15,-10,-9,58,65,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,-40,84,84,-39,84,84,84,84,84,84,84,84,84,84,]),'FALSE':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,-40,85,85,-39,85,85,85,85,85,85,85,85,85,85,]),'CLASS_TYPE':([5,18,39,55,59,63,71,125,130,144,182,],[12,32,48,48,48,48,48,158,48,48,48,]),'INTEGER':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,-40,76,76,-39,76,76,76,76,76,76,76,76,76,76,]),'LTEQ':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,127,127,127,127,127,127,127,-74,-75,-60,127,127,127,-71,127,-44,127,127,127,-61,-38,127,None,None,-48,-50,None,-47,None,-49,127,None,127,-51,127,127,-64,-43,127,-84,127,127,-78,-73,127,127,127,127,-72,-82,127,-80,127,127,-79,127,-86,]),'OR':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,128,128,128,128,128,128,128,-74,-75,-60,128,128,-59,-71,128,-44,128,128,128,-61,-38,128,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,128,128,-64,-43,128,-84,128,128,-78,-73,128,128,128,128,-72,-82,128,-80,128,128,-79,128,-86,]),'BREAK':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,-40,86,86,-39,86,86,86,86,86,86,86,86,86,86,]),'SELF':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,-40,87,87,-39,87,87,87,87,87,87,87,87,87,87,]),'CONTINUE':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,-40,89,89,-39,89,89,89,89,89,89,89,89,89,89,]),'LET':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,-40,90,90,-39,90,90,90,90,90,90,90,90,90,90,]),'NOT':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,148,168,169,173,174,177,178,183,184,190,195,198,199,207,],[91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,-40,91,91,-39,91,91,91,91,91,91,91,91,91,91,]),'COMMA':([43,45,47,48,49,50,51,53,66,68,72,73,76,77,79,82,83,85,86,87,88,89,93,102,106,107,109,114,133,137,138,139,140,145,146,149,150,151,152,153,154,155,157,159,160,161,162,163,166,167,172,176,179,181,185,186,189,191,192,194,196,200,201,202,205,206,208,210,],[57,-31,-29,-24,-28,-27,-25,-26,-30,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,-32,-74,-75,-60,143,-59,-71,-44,168,-45,-41,-61,-38,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,-33,-64,-43,-91,-84,-46,-78,-73,168,-42,-88,-90,-72,-82,-92,-80,168,-87,-79,-89,-86,]),'PUBLIC':([15,24,29,33,42,],[25,25,25,-14,-13,]),'LOOP':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,100,102,106,107,114,133,137,140,145,146,149,150,151,152,153,154,155,157,159,160,161,162,166,167,176,181,185,189,194,196,201,203,206,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,134,-74,-75,-60,-59,-71,-44,-41,-61,-38,-55,-56,-48,-50,-52,-47,-53,-49,-58,-54,-57,-51,-64,-43,-84,-78,-73,-42,-72,-82,-80,207,-79,-86,]),'MOD':([47,48,49,50,51,53,68,72,73,76,77,79,82,83,85,86,87,88,89,92,95,96,98,99,100,101,102,106,107,111,113,114,133,136,137,139,140,141,145,146,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,166,167,170,176,179,180,181,185,188,189,192,193,194,196,197,201,204,205,206,209,210,],[-29,-24,-28,-27,-25,-26,-76,-67,-63,-65,-66,-85,-37,-81,-68,-69,-62,-83,-70,129,129,129,129,129,129,129,-74,-75,-60,129,129,129,-71,129,-44,129,129,129,-61,-38,129,129,129,129,-50,129,129,129,-49,129,129,129,-51,129,129,-64,-43,129,-84,129,129,-78,-73,129,129,129,129,-72,-82,129,-80,129,129,-79,129,-86,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'imports':([0,],[2,]),'let_expression':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,168,169,174,177,178,183,184,190,195,198,199,207,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'block_list':([84,],[112,]),'feature_body':([26,],[36,]),'feature_header':([15,24,],[26,26,]),'for':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,168,169,174,177,178,183,184,190,195,198,199,207,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'feature':([15,24,],[22,35,]),'start':([0,],[4,]),'program':([0,],[1,]),'argument_list':([104,174,195,],[138,186,202,]),'if_then_else':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,168,169,174,177,178,183,184,190,195,198,199,207,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'type':([39,55,59,63,71,130,144,182,],[52,64,93,97,102,163,172,191,]),'formal_parameter_list':([37,],[43,]),'class_body':([8,],[16,]),'let':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,168,169,174,177,178,183,184,190,195,198,199,207,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'block_expression':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,168,169,174,177,178,183,184,190,195,198,199,207,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'class_header':([0,2,6,9,],[8,8,8,8,]),'class':([0,2,6,9,],[3,3,13,13,]),'formal':([15,24,27,],[30,30,38,]),'formal_parameter':([37,57,],[45,66,]),'features_list':([15,],[24,]),'while':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,168,169,174,177,178,183,184,190,195,198,199,207,],[88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,]),'classes':([0,2,],[6,9,]),'formaldehyde':([80,],[109,]),'modifier':([15,24,29,],[27,27,40,]),'expression':([58,61,62,65,67,69,70,74,75,81,84,91,103,104,105,108,112,115,116,117,118,119,120,121,124,126,127,128,129,134,135,142,168,169,174,177,178,183,184,190,195,198,199,207,],[92,95,96,98,99,100,101,106,107,111,113,114,136,139,140,141,147,149,150,151,152,153,154,155,157,159,160,161,162,164,165,170,179,180,139,188,189,192,193,197,139,204,205,209,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> program','start',1,'p_start','miniirgen.py',57),
  ('program -> imports classes','program',2,'p_program_with_imports','miniirgen.py',75),
  ('program -> classes','program',1,'p_program','miniirgen.py',82),
  ('imports -> imports IMPORT ID SEMICOLON','imports',4,'p_imports_multiple','miniirgen.py',87),
  ('imports -> IMPORT ID SEMICOLON','imports',3,'p_imports','miniirgen.py',92),
  ('classes -> classes class SEMICOLON','classes',3,'p_classes_multiple','miniirgen.py',98),
  ('classes -> class SEMICOLON','classes',2,'p_classes','miniirgen.py',109),
  ('class -> class_header class_body','class',2,'p_class_header_body','miniirgen.py',117),
  ('class_header -> CLASS CLASS_TYPE INHERITS CLASS_TYPE','class_header',4,'p_class_header_with_inheritance','miniirgen.py',127),
  ('class_header -> CLASS CLASS_TYPE','class_header',2,'p_class_header','miniirgen.py',146),
  ('class_body -> LBRACE RBRACE','class_body',2,'p_class_body_empty','miniirgen.py',160),
  ('class_body -> LBRACE features_list RBRACE','class_body',3,'p_class_body','miniirgen.py',163),
  ('features_list -> features_list feature SEMICOLON','features_list',3,'p_features_list_mult','miniirgen.py',208),
  ('features_list -> feature SEMICOLON','features_list',2,'p_features_list','miniirgen.py',218),
  ('feature -> feature_header feature_body','feature',2,'p_feature_header_body','miniirgen.py',224),
  ('feature_header -> DEF modifier ID COLON type','feature_header',5,'p_feature_header_with_modifier','miniirgen.py',234),
  ('feature_header -> DEF ID COLON type','feature_header',4,'p_feature_header','miniirgen.py',249),
  ('feature_body -> LPAREN formal_parameter_list RPAREN LBRACE expression RBRACE','feature_body',6,'p_feature_body_with_formal_parameter_list','miniirgen.py',264),
  ('feature_body -> LPAREN RPAREN LBRACE expression RBRACE','feature_body',5,'p_feature_body','miniirgen.py',276),
  ('feature -> modifier formal','feature',2,'p_feature_modifier_formal','miniirgen.py',338),
  ('feature -> formal','feature',1,'p_feature_formal','miniirgen.py',345),
  ('modifier -> PUBLIC','modifier',1,'p_modifier_public','miniirgen.py',351),
  ('modifier -> PRIVATE','modifier',1,'p_modifier_private','miniirgen.py',357),
  ('type -> CLASS_TYPE','type',1,'p_type_class_type','miniirgen.py',364),
  ('type -> INTEGER_TYPE','type',1,'p_type_integer_type','miniirgen.py',374),
  ('type -> BOOL_TYPE','type',1,'p_type_bool_type','miniirgen.py',379),
  ('type -> STRING_TYPE','type',1,'p_type_string_type','miniirgen.py',384),
  ('type -> OBJECT','type',1,'p_type_object','miniirgen.py',389),
  ('type -> SELF_TYPE','type',1,'p_type_self_type','miniirgen.py',394),
  ('formal_parameter_list -> formal_parameter_list COMMA formal_parameter','formal_parameter_list',3,'p_formal_parameter_list_many','miniirgen.py',400),
  ('formal_parameter_list -> formal_parameter','formal_parameter_list',1,'p_formal_parameter_list','miniirgen.py',409),
  ('formal_parameter -> ID COLON type','formal_parameter',3,'p_formal_parameter','miniirgen.py',419),
  ('formal_parameter -> ID LSQRBRACKET RSQRBRACKET COLON type','formal_parameter',5,'p_formal_parameter_arr','miniirgen.py',432),
  ('formal -> ID COLON type GETS expression','formal',5,'p_formal_with_assign','miniirgen.py',447),
  ('formal -> ID COLON type','formal',3,'p_formal','miniirgen.py',463),
  ('formal -> ID COLON type LSQRBRACKET expression RSQRBRACKET','formal',6,'p_formal_arr','miniirgen.py',480),
  ('expression -> block_expression','expression',1,'p_expression_block_expression','miniirgen.py',496),
  ('block_expression -> LBRACE block_list RBRACE','block_expression',3,'p_block_expression','miniirgen.py',504),
  ('block_list -> block_list expression SEMICOLON','block_list',3,'p_block_list_many','miniirgen.py',510),
  ('block_list -> expression SEMICOLON','block_list',2,'p_block_list','miniirgen.py',517),
  ('expression -> ID GETS expression','expression',3,'p_expression_assign','miniirgen.py',525),
  ('expression -> ID LSQRBRACKET expression RSQRBRACKET GETS expression','expression',6,'p_expression_assign_arr','miniirgen.py',545),
  ('expression -> ID LPAREN argument_list RPAREN','expression',4,'p_expression_function_call_with_arguments_2','miniirgen.py',563),
  ('expression -> ID LPAREN RPAREN','expression',3,'p_expression_function_call_2','miniirgen.py',574),
  ('argument_list -> expression','argument_list',1,'p_argument_list','miniirgen.py',588),
  ('argument_list -> argument_list COMMA expression','argument_list',3,'p_argument_list_many','miniirgen.py',601),
  ('expression -> expression PLUS expression','expression',3,'p_expression_plus','miniirgen.py',616),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','miniirgen.py',638),
  ('expression -> expression TIMES expression','expression',3,'p_expression_times','miniirgen.py',653),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_divide','miniirgen.py',668),
  ('expression -> expression MOD expression','expression',3,'p_expression_mod','miniirgen.py',683),
  ('expression -> expression LT expression','expression',3,'p_expression_lt','miniirgen.py',698),
  ('expression -> expression GT expression','expression',3,'p_expression_gt','miniirgen.py',724),
  ('expression -> expression LTEQ expression','expression',3,'p_expression_lteq','miniirgen.py',749),
  ('expression -> expression GTEQ expression','expression',3,'p_expression_gteq','miniirgen.py',773),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_equal','miniirgen.py',799),
  ('expression -> expression OR expression','expression',3,'p_expression_or','miniirgen.py',825),
  ('expression -> expression AND expression','expression',3,'p_expression_and','miniirgen.py',854),
  ('expression -> NOT expression','expression',2,'p_expression_not','miniirgen.py',876),
  ('expression -> TILDA expression','expression',2,'p_expression_tilda','miniirgen.py',896),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','miniirgen.py',909),
  ('expression -> SELF','expression',1,'p_expression_self','miniirgen.py',920),
  ('expression -> ID','expression',1,'p_expression_id','miniirgen.py',928),
  ('expression -> ID LSQRBRACKET expression RSQRBRACKET','expression',4,'p_expression_arr','miniirgen.py',937),
  ('expression -> INTEGER','expression',1,'p_expression_integer','miniirgen.py',949),
  ('expression -> STRING','expression',1,'p_expression_string','miniirgen.py',956),
  ('expression -> TRUE','expression',1,'p_expression_true','miniirgen.py',961),
  ('expression -> FALSE','expression',1,'p_expression_false','miniirgen.py',966),
  ('expression -> BREAK','expression',1,'p_expression_break','miniirgen.py',971),
  ('expression -> CONTINUE','expression',1,'p_expression_continue','miniirgen.py',976),
  ('expression -> RETURN expression SEMICOLON','expression',3,'p_expression_return','miniirgen.py',981),
  ('expression -> expression PERIOD ID LPAREN argument_list RPAREN','expression',6,'p_expression_function_call_with_arguments','miniirgen.py',990),
  ('expression -> expression PERIOD ID LPAREN RPAREN','expression',5,'p_expression_function_call','miniirgen.py',1002),
  ('expression -> NEW type','expression',2,'p_expression_new','miniirgen.py',1015),
  ('expression -> ISVOID expression','expression',2,'p_expression_isvoid','miniirgen.py',1023),
  ('expression -> let_expression','expression',1,'p_expression_let_expression','miniirgen.py',1030),
  ('let -> LET','let',1,'p_let_to_let','miniirgen.py',1036),
  ('let_expression -> let formaldehyde IN expression TEL','let_expression',5,'p_let_expression','miniirgen.py',1050),
  ('expression -> expression AT CLASS_TYPE PERIOD ID LPAREN argument_list RPAREN','expression',8,'p_expression_at_function_with_arguments','miniirgen.py',1065),
  ('expression -> expression AT CLASS_TYPE PERIOD ID LPAREN RPAREN','expression',7,'p_expression_at_function','miniirgen.py',1075),
  ('expression -> if_then_else','expression',1,'p_expression_if_then_else','miniirgen.py',1085),
  ('if_then_else -> IF expression THEN expression ELSE expression FI','if_then_else',7,'p_if_then_else','miniirgen.py',1091),
  ('expression -> while','expression',1,'p_expression_while','miniirgen.py',1107),
  ('while -> WHILE expression LOOP expression POOL','while',5,'p_while','miniirgen.py',1114),
  ('expression -> for','expression',1,'p_expression_for','miniirgen.py',1136),
  ('for -> FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN LOOP expression POOL','for',11,'p_for','miniirgen.py',1142),
  ('formaldehyde -> formaldehyde COMMA ID COLON type GETS expression','formaldehyde',7,'p_formaldehyde_with_assign_many','miniirgen.py',1172),
  ('formaldehyde -> formaldehyde COMMA ID COLON type','formaldehyde',5,'p_formaldehyde_many','miniirgen.py',1190),
  ('formaldehyde -> formaldehyde COMMA ID COLON type LSQRBRACKET expression RSQRBRACKET','formaldehyde',8,'p_formaldehyde_arr_many','miniirgen.py',1205),
  ('formaldehyde -> ID COLON type GETS expression','formaldehyde',5,'p_formaldehyde_with_assign','miniirgen.py',1219),
  ('formaldehyde -> ID COLON type','formaldehyde',3,'p_formaldehyde','miniirgen.py',1234),
  ('formaldehyde -> ID COLON type LSQRBRACKET expression RSQRBRACKET','formaldehyde',6,'p_formaldehyde_arr','miniirgen.py',1247),
]
