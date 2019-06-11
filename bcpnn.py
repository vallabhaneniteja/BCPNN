import bcpnn_data as bd 
import bcpnn_parameters as bp 
import time
import tensorflow as tf
import csv
from tensorflow.keras import layers
from collections import defaultdict
import sys

def func():
	return(1)

def func1():
	a={}
	a['alp']=2
	a['alp1']=1
	return(a)
def func2():
	b={}
	b['bet']=2
	b['bet1']=1
	return(b)

def read_parameters(alp_fname,bet_fname,g_fname):
	g_parameter_matrix=defaultdict(lambda:defaultdict(func))
	a_parameter_matrix=defaultdict(func1)
	b_parameter_matrix=defaultdict(func2)
	with open(g_fname,'rt') as f:
		data=csv.reader(f)
		for row in data:
			g_parameter_matrix[row[0]][row[1]]=float(row[2])
	with open(alp_fname,'rt') as f:
		data=csv.reader(f)
		for row in data:
			a_parameter_matrix[row[0]]={}
			a_parameter_matrix[row[0]]['alp']=float(row[1])
			a_parameter_matrix[row[0]]['alp1']=float(row[2])
	with open(bet_fname,'rt') as f:
		data=csv.reader(f)
		for row in data:
			b_parameter_matrix[row[0]]={}
			b_parameter_matrix[row[0]]['bet']=float(row[1])
			b_parameter_matrix[row[0]]['bet1']=float(row[2])

	return a_parameter_matrix,b_parameter_matrix,g_parameter_matrix

def write_out(a_parameters,b_parameters,g_parameters,alp_fname,bet_fname,g_fname):
	with open(alp_fname,'w') as file:
		writer=csv.writer(file,delimiter=',')
		for key in a_parameters.keys():
			writer.writerow([key,a_parameters[key]['alp'],a_parameters[key]['alp1']])
	with open(bet_fname,'w') as file:
		writer=csv.writer(file,delimiter=',')
		for key in b_parameters.keys():
			writer.writerow([key,b_parameters[key]['bet'],b_parameters[key]['bet1']])
	with open(g_fname,'w') as file:
		writer=csv.writer(file,delimiter=',')
		for drug in g_parameters.keys():
			for adr in g_parameters[drug].keys():
				writer.writerow([drug,adr,g_parameters[drug][adr]])

start=time.time()
drug_reports=bd.drug_data("data/ascii/DRUG19Q1.txt")
adr_reports=bd.adr_data("data/ascii/REAC19Q1.txt")
drug_set=set()
adr_set=set()

for key in drug_reports.keys():
	for drug in drug_reports[key]:
		drug_set.add(drug)

for key in adr_reports.keys():
	for adr in adr_reports[key]:
		adr_set.add(adr)

count=0
drug_matrix=defaultdict(lambda:defaultdict(int))
drug_counts=defaultdict(int)
adr_counts=defaultdict(int)
N=0
for key in drug_reports.keys():
	for drug in drug_reports[key]:
		for adr in adr_reports[key]:	
			drug_matrix[drug][adr]+=1
			adr_counts[adr]+=1
			drug_counts[drug]+=1
			N+=1
			
# N=len(drug_reports.keys())
# for drug in drug_matrix.keys():
# 	if(len(drug_matrix[drug].keys())<5):
# 		print(drug)
# 		print(drug_matrix[drug])
# 		input()
a_parameters,b_parameters,g_parameters=read_parameters("alpha.csv","beta.csv","gamma.csv")

tuple_set=set()
for drug in drug_matrix.keys():
	for adr in drug_matrix[drug].keys():
		tuple_set.add((drug,adr))
for drug in g_parameters.keys():
	for adr in g_parameters[drug].keys():
		tuple_set.add((drug,adr))

new_signals=[]
# for drug in drug_matrix.keys():
# 	for adr in drug_matrix[drug].keys():
c1=0
c2=0
c3=0
for t in list(tuple_set):
		adr=t[1]
		drug=t[0]
		count+=1
		a=drug_matrix[drug][adr]
		b=drug_counts[drug]-a
		c=adr_counts[adr]-a
		d=N-(a+b+c)
		if(adr=='Anaemia' and drug=='ALFADIOL'):
			print(a)
			print(b)
			print(c)
			print(d)
		g11=g_parameters[drug][adr]
		alp=a_parameters[drug]['alp']
		alp1=a_parameters[drug]['alp1']
		bet=b_parameters[adr]['bet']
		bet1=b_parameters[adr]['bet1']
		# print(a)
		# print(b)
		# print(c)
		# print(d)
		# print(alp)
		# print(alp1)
		# print(bet)
		# print(bet1)
		# print(g11)
		signal_generated=bp.signal_output(a,b,c,d,g11,alp,bet,alp1,bet1)
		if(signal_generated=='Weak Signal'):
			c1+=1
		elif(signal_generated=='Medium Signal'):
			c2+=1
		elif(signal_generated=='Strong Signal'):
			c3+=1
print(c1,c2,c3)
print("new signals="+str(len(new_signals)))	
for key in adr_counts.keys():
	b_parameters[key]['bet']+=N
	b_parameters[key]['bet1']+=adr_counts[key]
for key in drug_counts.keys():
	a_parameters[key]['alp']+=N
	a_parameters[key]['alp1']+=drug_counts[key]
for drug in drug_matrix.keys():
	for adr in drug_matrix[drug].keys():
		g_parameters[drug][adr]+=drug_matrix[drug][adr]
 
write_out(a_parameters,b_parameters,g_parameters,"alpha.csv","beta.csv","gamma.csv")
print(count)
print(time.time()-start)