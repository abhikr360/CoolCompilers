#!/usr/bin/env python


grammar = {
0 :"S' -> start ",
1 :"start -> program ",
2 :"program -> imports classes ",
3 :"program -> classes ",
4 :"imports -> imports IMPORT ID SEMICOLON ",
5 :"imports -> IMPORT ID SEMICOLON ",
6 :"classes -> classes class SEMICOLON ",
7 :"classes -> class SEMICOLON ",
8 :"class -> CLASS CLASS_TYPE INHERITS CLASS_TYPE LBRACE features_list RBRACE ",
9 :"class -> CLASS CLASS_TYPE LBRACE features_list RBRACE ",
10:"class -> CLASS CLASS_TYPE INHERITS CLASS_TYPE LBRACE RBRACE ",
11:"class -> CLASS CLASS_TYPE LBRACE RBRACE ",
12:"features_list -> features_list feature SEMICOLON ",
13:"features_list -> feature SEMICOLON ",
14:"feature -> modifier ID LPAREN formal_parameter_list RPAREN COLON type LBRACE expression RBRACE ",
15:"feature -> modifier ID LPAREN RPAREN COLON type LBRACE expression RBRACE ",
16:"feature -> ID LPAREN formal_parameter_list RPAREN COLON type LBRACE expression RBRACE ",
17:"feature -> ID LPAREN RPAREN COLON type LBRACE expression RBRACE ",
18:"feature -> modifier formal ",
19:"feature -> formal ",
20:"modifier -> PUBLIC ",
21:"modifier -> PRIVATE ",
22:"type -> CLASS_TYPE ",
23:"type -> INTEGER_TYPE ",
24:"type -> BOOL_TYPE ",
25:"type -> STRING_TYPE ",
26:"type -> OBJECT ",
27:"type -> SELF_TYPE ",
28:"formal_parameter_list -> formal_parameter_list COMMA formal_parameter ",
29:"formal_parameter_list -> formal_parameter ",
30:"formal_parameter -> ID COLON type ",
31:"formal_parameter -> ID LSQRBRACKET RSQRBRACKET COLON type ",
32:"formal -> ID COLON type GETS expression ",
33:"formal -> ID COLON type ",
34:"formal -> ID COLON type LSQRBRACKET RSQRBRACKET ",
35:"expression -> block_expression ",
36:"block_expression -> LBRACE block_list RBRACE ",
37:"block_list -> block_list expression SEMICOLON ",
38:"block_list -> expression SEMICOLON ",
39:"expression -> ID GETS expression ",
40:"expression -> ID LSQRBRACKET expression RSQRBRACKET GETS expression ",
41:"expression -> ID LPAREN argument_list RPAREN ",
42:"expression -> ID LPAREN RPAREN ",
43:"argument_list -> expression ",
44:"argument_list -> argument_list COMMA expression ",
45:"expression -> expression PLUS expression ",
46:"expression -> expression MINUS expression ",
47:"expression -> expression TIMES expression ",
48:"expression -> expression DIVIDE expression ",
49:"expression -> expression MOD expression ",
50:"expression -> expression LT expression ",
51:"expression -> expression GT expression ",
52:"expression -> expression LTEQ expression ",
53:"expression -> expression GTEQ expression ",
54:"expression -> expression EQUAL expression ",
55:"expression -> expression OR expression ",
56:"expression -> expression AND expression ",
57:"expression -> NOT expression ",
58:"expression -> TILDA expression ",
59:"expression -> LPAREN expression RPAREN ",
60:"expression -> SELF ",
61:"expression -> ID ",
62:"expression -> ID LSQRBRACKET expression RSQRBRACKET ",
63:"expression -> INTEGER ",
64:"expression -> STRING ",
65:"expression -> TRUE ",
66:"expression -> FALSE ",
67:"expression -> BREAK ",
68:"expression -> CONTINUE ",
69:"expression -> expression PERIOD ID LPAREN argument_list RPAREN ",
70:"expression -> expression PERIOD ID LPAREN RPAREN ",
71:"expression -> NEW type ",
72:"expression -> ISVOID expression ",
73:"expression -> let_expression ",
74:"let_expression -> LET formal IN expression TEL ",
75:"expression -> expression AT CLASS_TYPE PERIOD ID LPAREN argument_list RPAREN ",
76:"expression -> expression AT CLASS_TYPE PERIOD ID LPAREN RPAREN ",
77:"expression -> if_then_else ",
78:"if_then_else -> IF expression THEN expression ELSE expression FI ",
79:"expression -> while ",
80:"while -> WHILE expression LOOP expression POOL ",
81:"expression -> for ",
82:"for -> FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN LOOP expression POOL ",
}

# print grammar[82]
def html_start(title_name,code):
	html_start = "<!DOCTYPE html>\n<html>\n<head>\n<link rel=\"stylesheet\" href=\"html_output.css\">\n<title>%s</title>\n</head>\n<body>\n"%title_name
	html_start += "<h1>Code Snippet is -</h1>\n"
	html_start += "<pre>\n<code>\n%s\n</code>\n</pre>\n"%code
		
	html_start += "<p><mark>red</mark> represent non-terminal expanded in next rule\n</p>"
	html_start += "<p><u1>Underline</u1> represent rule into which non-terminal has expanded</p>"
	html_start += "<p>.</p>"
	html_start += "<p>.</p>"
	html_start += "<p>.</p>"

	return html_start

def html_end():
	html_end = "</body>\n</html>\n"
	return html_end

def rreplace(s, old, new):
    return (s[::-1].replace(old[::-1],new[::-1], 1))[::-1]

