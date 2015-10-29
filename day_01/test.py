#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
print "welcome login"

import getpass 
name=raw_input("enter your name :")
pwd=getpass.getpass("enter your pwd:")
if name == 'hansz' or name == "hansz1" or name == "han":
	if pwd == '123':
		print "欢迎 %s" %(name)
		if name == 'hansz':
			print "good"
		elif name == 'hansz1':
			print "better"
		elif name == 'han':
			print "best"
		else:
			print "other.."
	else:
		print "you pwd is wrong"
	
else:
	print  "you are not in this list "
