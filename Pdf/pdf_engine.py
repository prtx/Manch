#/usr/bin/python
# -*- coding: utf-8 -*-

import os, subprocess, sys
from json import dumps, loads
reload(sys)
sys.setdefaultencoding("utf-8")

def word_count(text):
	
	
	punctuations = [';',',','.','!','(',')','\t','\n','=','  ','\xc2\xa0']
	
	for punctuation in punctuations:
		text = text.replace(punctuation,' ')

	words = text.lower().split(' ')
	
	
	while '' in words:
		words.pop(words.index(''))
	word_cloud = {}

	for word in list(set(words)):
		word_cloud[word] = words.count(word)
	
	return word_cloud
	


def word_cloud(pdf):

	aa = word_count(subprocess.check_output(['less \'static/pdf/'+pdf+'\''], shell=True))
	a = open('static/json/'+pdf.replace('.pdf','.json'),'a')
	a.write(dumps(aa))
	a.close()
	
	
def probe_corpus():
	
	json = {}
	for path, subdirs, files in os.walk('static/json/'):
		for name in files:
			json[name] = loads(open('static/json/'+name).read())
			
	return json
