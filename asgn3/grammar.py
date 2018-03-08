#!/usr/bin/env python

grammar = {
	:['program','imports','classes']
	:['program','classes']
	:['imports','imports','IMPORT','ID','SEMI_COLON']
	:['classes','classes','class','SEMI_COLON']
	:['classes','class','SEMI_COLON']
	:['class':'CLASS','CLASS_TYPE','INHERITS','CLASS_TYPE','LBRACE','features_list_opt','RBRACE']
	:['class','CLASS','CLASS_TYPE','LBRACE','RBRACE']
	:['features_list','features_list','feature']
	:['features_list','feature']

	:['feature','modifier','ID','LPAREN','formal_parameter_list','RPAREN','COLON','type','LBRACE','expression','RBRACE']
	# :['feature','modifier','ID','LPAREN','formal_params_list','RPAREN','COLON','INTEGER_TYPE','LBRACE','expression','RBRACE']
	# :['feature','modifier','ID','LPAREN','formal_params_list','RPAREN','COLON','BOOL_TYPE','LBRACE','expression','RBRACE']
	# :['feature','modifier','ID','LPAREN','formal_params_list','RPAREN','COLON','STRING_TYPE','LBRACE','expression','RBRACE']
	
	:['feature','modifier','ID','LPAREN','RPAREN','COLON','type','LBRACE','expression','RBRACE']
	# :['feature','modifier','ID','LPAREN','RPAREN','COLON','INTEGER_TYPE','LBRACE','expression','RBRACE']
	# :['feature','modifier','ID','LPAREN','RPAREN','COLON','BOOL_TYPE','LBRACE','expression','RBRACE']
	# :['feature','modifier','ID','LPAREN','RPAREN','COLON','STRING_TYPE','LBRACE','expression','RBRACE']

	:['feature','ID','LPAREN','formal_parameter_list','RPAREN','COLON','type','LBRACE','expression','RBRACE']
	# :['feature','ID','LPAREN','formal_params_list','RPAREN','COLON','INTEGER_TYPE','LBRACE','expression','RBRACE']
	# :['feature','ID','LPAREN','formal_params_list','RPAREN','COLON','BOOL_TYPE','LBRACE','expression','RBRACE']
	# :['feature','ID','LPAREN','formal_params_list','RPAREN','COLON','STRING_TYPE','LBRACE','expression','RBRACE']

	:['feature','ID','LPAREN','RPAREN','COLON','type','LBRACE','expression','RBRACE']
	# :['feature','ID','LPAREN','RPAREN','COLON','INTEGER_TYPE','LBRACE','expression','RBRACE']
	# :['feature','ID','LPAREN','RPAREN','COLON','BOOL_TYPE','LBRACE','expression','RBRACE']
	# :['feature','ID','LPAREN','RPAREN','COLON','STRING_TYPE','LBRACE','expression','RBRACE']

	:['feature','modifier','formal']
	:['feature','formal']
	:['modifier','PUBLIC']
	:['modifier','PRIVATE']

	:['type','CLASS_TYPE']
	:['type','BOOL_TYPE']
	:['type','INTEGER_TYPE']
	:['type','STRING_TYPE']
	:['type','SELF_TYPE']


	:['formal_parameter_list','formal_parameter_list','formal_parameter']
	:['formal_parameter_list','formal_parameter']

	:['formal_parameter','ID','COLON','type']
	# :['formal_param','ID','COLON','INTEGER_TYPE']
	# :['formal_param','ID','COLON','BOOL_TYPE']
	# :['formal_param','ID','COLON','STRING_TYPE']

	:['formal_parameter','ID','LSQRBRACKET','RSQRBRACKET','COLON','type']
	# :['formal_param','ID','LSQRBRACKET','RSQRBRACKET','COLON','INTEGER_TYPE']
	# :['formal_param','ID','LSQRBRACKET','RSQRBRACKET','COLON','BOOL_TYPE']
	# :['formal_param','ID','LSQRBRACKET','RSQRBRACKET','COLON','STRING_TYPE']

	:['formal','ID','COLON','type','GETS','expression','SEMI_COLON']
	# :['formal','ID','COLON','INTEGER_TYPE','GETS','expression','SEMI_COLON']
	# :['formal','ID','COLON','BOOL_TYPE','GETS','expression','SEMI_COLON']
	# :['formal','ID','COLON','STRING_TYPE','GETS','expression','SEMI_COLON']

	:['formal','ID','COLON','type','SEMI_COLON']		#no semicolon
	# :['formal','ID','SEMI_COLON','INTEGER_TYPE']
	# :['formal','ID','SEMI_COLON','BOOL_TYPE']
	# :['formal','ID','SEMI_COLON','STRING_TYPE']

	:['formal','ID','COLON','type','LSQRBRACKET','RSQRBRACKET','SEMI_COLON']
	# :['formal','ID','SEMI_COLON','INTEGER_TYPE','LSQRBRACKET','expression','RSQRBRACKET','SEMI_COLON']
	# :['formal','ID','SEMI_COLON','BOOL_TYPE','LSQRBRACKET','expression','RSQRBRACKET','SEMI_COLON']
	# :['formal','ID','SEMI_COLON','STRING_TYPE','LSQRBRACKET','expression','RSQRBRACKET','SEMI_COLON']

	#starting expression ------

	:['expression','ID','GETS','expression']
	:['expression','ID','LSQRBRACKET','expression','RSQRBRACKET','GETS','expression']
	:['expression','expression','PERIOD','ID','LPAREN','argument_lists','RPAREN']
	:['expression','expression','PERIOD','ID','LPAREN','RPAREN']

	:['expression','expression','AT','CLASS_TYPE','PERIOD','ID','LPAREN','argument_list','RPAREN']
	# :['expression','expression','AT','INTEGER_TYPE','PERIOD','ID','LPAREN','argument_lists','RPAREN']
	# :['expression','expression','AT','BOOL_TYPE','PERIOD','ID','LPAREN','argument_lists','RPAREN']
	# :['expression','expression','AT','STRING_TYPE','PERIOD','ID','LPAREN','argument_lists','RPAREN']

	:['expression','expression','AT','CLASS_TYPE','PERIOD','ID','LPAREN','RPAREN']
	# :['expression','expression','AT','INTEGER_TYPE','PERIOD','ID','LPAREN','RPAREN']
	# :['expression','expression','AT','BOOL_TYPE','PERIOD','ID','LPAREN','RPAREN']
	# :['expression','expression','AT','STRING_TYPE','PERIOD','ID','LPAREN','RPAREN']

	:['expression','if_then_else']
	:['expression','while']
	:['expression','for']
	:['expression','block_expression']
	:['expression','let_expression']
	:['expression','NEW type']
	:['expression','ISVOID','expression']
	:['expression','expression','PLUS','expression']
	:['expression','expression','MINUS','expression']
	:['expression','expression','TIMES','expression']
	:['expression','expression','DIVIDE','expression']
	:['expression','expression','MOD','expression']
	:['expression','expression','LT','expression']
	:['expression','expression','GT','expression']
	:['expression','expression','LTEQ','expression']
	:['expression','expression','GTEQ','expression']
	:['expression','expression','EQUAL','expression']
	:['expression','expression','OR','expression']
	:['expression','expression','AND','expression']
	:['expression','NOT','expression']
	:['expression','LPAREN','expression','RPAREN']
	:['expression','SELF']
	:['expression','ID']
	:['expression','ID','LSQRBRACKET','expression','RSQRBRACKET']
	:['expression','INTEGER']
	:['expression','STRING']
	:['expression','TRUE']
	:['expression','FALSE']
	:['expression','BREAK']
	:['expression','CONTINUE']

	:['argument_list','argument_list','expression']
	:['argument_list','expression']
	:['if_then_else','IF','expression','THEN','expression','ELSE','expression','FI']
	:['while','WHILE','expression','LOOP','expression','SEMI_COLON','expression','LOOP','expression','POOL']
	:['block_expression','LBRACE','block_list','RBRACE']
	:['block_list','block_list','expression','SEMI_COLON']
	:['block_list','expression','SEMI_COLON']
	:['let_expression','LET','formal','IN','expression']


}



