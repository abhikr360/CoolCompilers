#!/usr/bin/env python
import csv
import time
class Instruction3AC():
	def __init__(self):
		self.instr_type = None
		self.in1 = None
		self.in2 = None
		self.out = None
		self.target = None
		self.operation = None
		self.is_mem = False
		self.line_no = 0
	def print_instr(self):
		print "line number : ",line_no
		print "Instruction Type : ",instr_type
		print "input symbol 1 : ",in1
		print "input symbo 2 : ",in2
		print "output symbol",out
		print "target label : ",target
		print "operation : ",operation
		print "Is in memory : ",is_mem


def take_3AC(filename):
	with open(filename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		# print spamreader
		# spamreader.next()
		# print spamreader.fieldnames
		for row in spamreader:
			row = ', '.join(row)
			idx = row.find(',')
			row[:idx]
			quit()
if __name__ == '__main__':
	take_3AC("3ac1.csv")