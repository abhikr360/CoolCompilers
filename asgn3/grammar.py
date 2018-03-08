#!/usr/bin/env python

grammar = {
	:['program','imports','classes']
	:['imports','imports','IMPORT','ID','SEMI_COLON']
	:['imports','empty']
	:['classes','classes','class','SEMI_COLON']
	:['classes','class','SEMI_COLON']
	:['class':'CLASS','CLASS_TYPE','inheritance','LBRACE','features_list_opt','RBRACE','SEMI_COLON']
	:['inheritance','INHERITS','CLASS_TYPE',]
	:['inheritance','empty']
	:['features_list','features_list','feature']
	:['features_list','feature']

	:['feature','modifier','ID','LPAREN','formal_params_list','RPAREN','COLON','CLASS_TYPE','LBRACE','expression','RBRACE']
	:['feature','modifier','ID','LPAREN','formal_params_list','RPAREN','COLON','INTEGER_TYPE','LBRACE','expression','RBRACE']
	:['feature','modifier','ID','LPAREN','formal_params_list','RPAREN','COLON','BOOL_TYPE','LBRACE','expression','RBRACE']
	:['feature','modifier','ID','LPAREN','formal_params_list','RPAREN','COLON','STRING_TYPE','LBRACE','expression','RBRACE']
	
	:['feature','modifier','ID','LPAREN','RPAREN','COLON','CLASS_TYPE','LBRACE','expression','RBRACE']
	:['feature','modifier','ID','LPAREN','RPAREN','COLON','INTEGER_TYPE','LBRACE','expression','RBRACE']
	:['feature','modifier','ID','LPAREN','RPAREN','COLON','BOOL_TYPE','LBRACE','expression','RBRACE']
	:['feature','modifier','ID','LPAREN','RPAREN','COLON','STRING_TYPE','LBRACE','expression','RBRACE']

	:['feature','ID','LPAREN','formal_params_list','RPAREN','COLON','CLASS_TYPE','LBRACE','expression','RBRACE']
	:['feature','ID','LPAREN','formal_params_list','RPAREN','COLON','INTEGER_TYPE','LBRACE','expression','RBRACE']
	:['feature','ID','LPAREN','formal_params_list','RPAREN','COLON','BOOL_TYPE','LBRACE','expression','RBRACE']
	:['feature','ID','LPAREN','formal_params_list','RPAREN','COLON','STRING_TYPE','LBRACE','expression','RBRACE']

	:['feature','ID','LPAREN','RPAREN','COLON','CLASS_TYPE','LBRACE','expression','RBRACE']
	:['feature','ID','LPAREN','RPAREN','COLON','INTEGER_TYPE','LBRACE','expression','RBRACE']
	:['feature','ID','LPAREN','RPAREN','COLON','BOOL_TYPE','LBRACE','expression','RBRACE']
	:['feature','ID','LPAREN','RPAREN','COLON','STRING_TYPE','LBRACE','expression','RBRACE']

	:['feature','modifier','formal']
	:['feature','formal']
	:['modifier','PUBLIC','PRIVATE']

	:['formal_params_list','formal_params_list','formal_param']
	:['formal_params_list','formal_param']

	:['formal_param','ID','COLON','CLASS_TYPE']
	:['formal_param','ID','COLON','INTEGER_TYPE']
	:['formal_param','ID','COLON','BOOL_TYPE']
	:['formal_param','ID','COLON','STRING_TYPE']

	:['formal_param','ID','LSQRBRACKET','RSQRBRACKET','COLON','CLASS_TYPE']
	:['formal_param','ID','LSQRBRACKET','RSQRBRACKET','COLON','INTEGER_TYPE']
	:['formal_param','ID','LSQRBRACKET','RSQRBRACKET','COLON','BOOL_TYPE']
	:['formal_param','ID','LSQRBRACKET','RSQRBRACKET','COLON','STRING_TYPE']

	:['formal','ID','COLON','CLASS_TYPE','GETS','expression','SEMI_COLON']
	:['formal','ID','COLON','INTEGER_TYPE','GETS','expression','SEMI_COLON']
	:['formal','ID','COLON','BOOL_TYPE','GETS','expression','SEMI_COLON']
	:['formal','ID','COLON','STRING_TYPE','GETS','expression','SEMI_COLON']

	:['formal','ID','SEMI_COLON','CLASS_TYPE']		#no semicolon
	:['formal','ID','SEMI_COLON','INTEGER_TYPE']
	:['formal','ID','SEMI_COLON','BOOL_TYPE']
	:['formal','ID','SEMI_COLON','STRING_TYPE']

	:['formal','ID','SEMI_COLON','CLASS_TYPE','LSQRBRACKET','expression','RSQRBRACKET','SEMI_COLON']
	:['formal','ID','SEMI_COLON','INTEGER_TYPE','LSQRBRACKET','expression','RSQRBRACKET','SEMI_COLON']
	:['formal','ID','SEMI_COLON','BOOL_TYPE','LSQRBRACKET','expression','RSQRBRACKET','SEMI_COLON']
	:['formal','ID','SEMI_COLON','STRING_TYPE','LSQRBRACKET','expression','RSQRBRACKET','SEMI_COLON']

	#starting expression ------

	:['expression','ID','GETS','expression']
	:['expression','ID','LSQRBRACKET','expression','RSQRBRACKET','GETS','expression']
	:['expression','expression','PERIOD','ID','LPAREN','argument_lists','RPAREN']

	:['expression','expression','AT','CLASS_TYPE','PERIOD','ID','LPAREN','argument_lists','RPAREN']
	:['expression','expression','AT','INTEGER_TYPE','PERIOD','ID','LPAREN','argument_lists','RPAREN']
	:['expression','expression','AT','BOOL_TYPE','PERIOD','ID','LPAREN','argument_lists','RPAREN']
	:['expression','expression','AT','STRING_TYPE','PERIOD','ID','LPAREN','argument_lists','RPAREN']

	:['expression','expression','AT','CLASS_TYPE','PERIOD','ID','LPAREN','RPAREN']
	:['expression','expression','AT','INTEGER_TYPE','PERIOD','ID','LPAREN','RPAREN']
	:['expression','expression','AT','BOOL_TYPE','PERIOD','ID','LPAREN','RPAREN']
	:['expression','expression','AT','STRING_TYPE','PERIOD','ID','LPAREN','RPAREN']

	:['expression','if_then_else']
	:['expression','while']
	:['expression','for']
	:['expression','block_expression']
	:['expression','let_expression']
	


}



