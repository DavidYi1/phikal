import json, itertools
import utils as tech
from awesome_print import ap 
#Are there any standardized drug names not in the taxonomy?
READ = 'rb'

taxonomy = json.load(open('drug-taxonomy.json',READ))
standardized_names = json.load(open('drug_misnaming.json',READ))

if len(set(tech.flatten(standardized_names.values())) - set(taxonomy.keys())) == 0:
	ap("All standardized drug names are in the taxonomy.")