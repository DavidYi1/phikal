import json
import utils as tech 

READ = 'rb'
WRITE = 'wb'

drugs = json.load(open('drug_misnaming.json',READ))
drugs = list(set(list(tech.flatten(drugs.values()))))

with open('master-drug-list',WRITE) as fid:
	for drug in drugs:
		print>>fid,drug