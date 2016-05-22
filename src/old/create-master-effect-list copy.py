import json 

import utils as tech 

from awesome_print import ap 

taxonomy = json.load(open('../data/drug-taxonomy.json','rb'))

effects = set(tech.flatten([taxonomy[drug]["effects"] for drug in taxonomy]))

with open('../data/master-effect-list','wb') as fid:
	for effect in effects:
		print>>fid,effect