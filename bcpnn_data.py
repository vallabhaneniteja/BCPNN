import csv

def drug_data(fname):
	drug_reports={}
	with open(fname,mode='r') as f:
		csv_reader = csv.reader(f,delimiter='$')
		next(csv_reader)
		for l in csv_reader:
			if l[1] in drug_reports:
				drug_reports[l[1]].append(l[4])
			else:
				drug_reports[l[1]]=[]
				drug_reports[l[1]].append(l[4])
		return drug_reports

def adr_data(fname):
	adr_reports={}
	with open(fname,mode='r') as f:
		csv_reader = csv.reader(f,delimiter='$')
		next(csv_reader)
		for l in csv_reader:
			if l[1] in adr_reports:
				adr_reports[l[1]].append(l[2])
			else:
				adr_reports[l[1]]=[]
				adr_reports[l[1]].append(l[2])
	return adr_reports
