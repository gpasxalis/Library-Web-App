# -*- coding: utf-8 -*-
import json

with open('test.json') as json_file:  
	data = json.load(json_file)
	with open('data.json', 'w', encoding='utf-8') as f:
		for r in data['test']:
			for d in r['fields']:
				if d['tag'] < 10:
					json_data = {'index':{'_index':'test', '_type':'data'}},{'data':d['data']}
					#print(d['data'])
				else:
					for j in d['subfields']:
						#print(j['data'])
						json_data = {'index':{'_index':'test', '_type':'data'}},{'data':j['data']}
						json_str = json.dumps(json_data)
				json.dump(json_data, f, indent=2, ensure_ascii=False)
