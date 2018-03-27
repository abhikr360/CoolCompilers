#!/usr/bin/env python

from grammar import *

hello_world_rule = [27, 64, 43, 41, 17, 13, 8, 7, 3, 1]
cool_file_name = "hello_world.cl"

def changed_non_terminal(previous_rule,current_rule):
	non_terminal = current_rule[:current_rule.find("->")-1]
	# print non_terminal
	# print previous_rule.rfind(non_terminal)
	t1 = previous_rule[previous_rule.rfind(non_terminal):]
	# print t1
	idx = t1.find(' ')
	if(idx == -1):
		t1=t1
	else:
		t1 = t1[:idx]

	# t1 = t1[t1.find(' '):]
	# print t1

	return t1


def convert_to_HTML(rule_list,input_file):


	# f = open('html_output.txt','w+')
	file_name = input_file[input_file.find('/')+1:]
	# print file_name
	file_name = file_name[:file_name.find('.')]
	file_name = file_name+'.html'
	# print file_name
	f = open(file_name,'w+')
	previous_rule = None

	with open(input_file) as file:
		code = file.read()

	# print code

	f.write(html_start("Parser",code))

	i = 0
	for x in reversed(rule_list):
		i = i+1
		current_rule = grammar[x]
		
		if(previous_rule == None):
			# f.write("<p>S\' -> start </p>\n")
			# print "@"+current_rule
			previous_rule = current_rule
			rhs = current_rule[current_rule.find("->")+3:]
			previous_rhs = rhs
			continue


		# print "@"+current_rule
		changed = changed_non_terminal(previous_rule,current_rule)
		html_previous_rule = rreplace(previous_rule,previous_rhs,"<u1>"+previous_rhs+"</u1>")
		html_previous_rule = rreplace(html_previous_rule,changed,"<mark>"+changed+"</mark>")
		print current_rule
		rhs = current_rule[current_rule.find("->")+3:]
		print html_previous_rule
		f.write("<p>"+ html_previous_rule+"</p>\n")
		print rhs
		# print previous_rule
		# print changed
		previous_rhs = rhs
		current_rule = rreplace(previous_rule,changed,rhs)
		if(i==len(rule_list)):
			f.write("<p>"+ current_rule+"</p>\n")
			print current_rule
		print current_rule

		previous_rule = current_rule
		# quit()

		print "------------------------"
		# print 


	f.write(html_end())
	f.close()




if __name__ == '__main__':
	convert_to_HTML(hello_world_rule,cool_file_name)