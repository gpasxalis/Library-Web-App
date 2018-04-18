# -*- coding: utf-8 -*-
# Indexing based mapping

import json

with open('test.json') as json_file:  
	data = json.load(json_file)
	with open('data.json', 'w', encoding='utf-8') as f:
		for r in data['test']:
			for d in r['fields']:
				if d['tag'] > 9 and d['tag'] < 100:
					for j in d['subfields']:
						jso = {"taggroup":"index10", "value":j['data'], "datagroup":[{"record":d['tag'], "data":j['data'], "code":j['code'], "ind2":d['ind2'], "ind1":d['ind1']}] }
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				elif d['tag'] > 99 and d['tag'] < 200:
					for j in d['subfields']:
						jso = {"taggroup":"index100", "value":j['data'], "datagroup":[{"record":d['tag'], "data":j['data'], "code":j['code'], "ind2":d['ind2'], "ind1":d['ind1']}] }
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				elif d['tag'] > 199 and d['tag'] < 300:
					for j in d['subfields']:
						jso = {"taggroup":"index200", "value":j['data'], "datagroup":[{"record":d['tag'], "data":j['data'], "code":j['code'], "ind2":d['ind2'], "ind1":d['ind1']}] }
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				elif d['tag'] > 299 and d['tag'] < 400:
					for j in d['subfields']:
						jso = {"taggroup":"index300", "value":j['data'], "datagroup":[{"record":d['tag'], "data":j['data'], "code":j['code'], "ind2":d['ind2'], "ind1":d['ind1']}] }
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				elif d['tag'] > 399 and d['tag'] < 500:
					for j in d['subfields']:
						jso = {"taggroup":"index400", "value":j['data'], "datagroup":[{"record":d['tag'], "data":j['data'], "code":j['code'], "ind2":d['ind2'], "ind1":d['ind1']}] }
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				elif d['tag'] > 499 and d['tag'] < 600:
					for j in d['subfields']:
						jso = {"taggroup":"index500", "value":j['data'], "datagroup":[{"record":d['tag'], "data":j['data'], "code":j['code'], "ind2":d['ind2'], "ind1":d['ind1']}] }
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				elif d['tag'] > 599 and d['tag'] < 700:
					for j in d['subfields']:
						jso = {"taggroup":"index600", "value":j['data'], "datagroup":[{"record":d['tag'], "data":j['data'], "code":j['code'], "ind2":d['ind2'], "ind1":d['ind1']}] }
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				elif d['tag'] > 699 and d['tag'] < 800:
					for j in d['subfields']:
						jso = {"taggroup":"index700", "value":j['data'], "datagroup":[{"record":d['tag'], "data":j['data'], "code":j['code'], "ind2":d['ind2'], "ind1":d['ind1']}] }
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				elif d['tag'] > 799 and d['tag'] < 900:
					for j in d['subfields']:
						jso = {"taggroup":"index800", "value":j['data'], "datagroup":[{"record":d['tag'], "data":j['data'], "code":j['code'], "ind2":d['ind2'], "ind1":d['ind1']}] }
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				elif d['tag'] > 899 and d['tag'] < 1000:
					for j in d['subfields']:
						jso = {"taggroup":"index900", "value":j['data'], "datagroup":[{"record":d['tag'], "data":j['data'], "code":j['code'], "ind2":d['ind2'], "ind1":d['ind1']}] }
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))






				#else:
				#	for j in d['subfields']:
				#		
				#		jso = {"data":j['data']}
				#		print(json.dumps({"index":{"_index":"test", "_type":"data"}},ensure_ascii=False,separators=(',', ':')))
				#		print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
