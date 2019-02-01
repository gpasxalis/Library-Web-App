# -*- coding: utf-8 -*-
import json

with open('test.json') as json_file:  
	data = json.load(json_file)
	
	for r in data['test']:
		for d in r['fields']:
			#flag = 0			
			if d['tag'] > 9 and d['tag'] < 100:
				for j in d['subfields']:		
					jso = {"datagroup":[{"taggroup":"index10","value":j['data']}], "record":r['fields']}
					print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 99 and d['tag'] < 200:
				for j in d['subfields']:
					jso = {"datagroup":[{"taggroup":"index100","value":j['data']}], "record":r['fields']}
					print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 199 and d['tag'] < 300:
				for j in d['subfields']:

					#for json_value in jso['datagroup']:
					if j['data'] == jso['datagroup'][0]['value']: 
						jso['datagroup'].append({"taggroup":"index200","value":j['data']})
					jso = {"datagroup":[{"taggroup":"index200","value":j['data']}], "record":r['fields']}
					print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 299 and d['tag'] < 400:
				for j in d['subfields']:

					#for json_value in jso['datagroup']:
					if j['data'] == jso['datagroup'][0]['value']:
						jso['datagroup'].append({"taggroup":"index300","value":j['data']})
					
					jso = {"datagroup":[{"taggroup":"index300","value":j['data']}], "record":r['fields']}
					print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				
			if d['tag'] > 399 and d['tag'] < 500:
				for j in d['subfields']:
					
					#for json_value in jso['datagroup']:
					if j['data'] == jso['datagroup'][0]['value']:
						jso['datagroup'].append({"taggroup":"index400","value":j['data']})

					jso = {"datagroup":[{"taggroup":"index400","value":j['data']}], "record":r['fields']}
					print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 499 and d['tag'] < 600:
				for j in d['subfields']:

					#for json_value in jso['datagroup']:
					if j['data'] == jso['datagroup'][0]['value']:
						jso['datagroup'].append({"taggroup":"index500","value":j['data']})
					jso = {"datagroup":[{"taggroup":"index500","value":j['data']}], "record":r['fields']}
					print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 599 and d['tag'] < 700:
				for j in d['subfields']:

					#for json_value in jso['datagroup']:
					if j['data'] == jso['datagroup'][0]['value']:
						jso['datagroup'].append({"taggroup":"index600","value":j['data']})
					jso = {"datagroup":[{"taggroup":"index600","value":j['data']}], "record":r['fields']}
					print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 699 and d['tag'] < 800:
				for j in d['subfields']:

					#for json_value in jso['datagroup']:
					if j['data'] == jso['datagroup'][0]['value']:
						jso['datagroup'].append({"taggroup":"index700","value":j['data']})
					jso = {"datagroup":[{"taggroup":"index700","value":j['data']}], "record":r['fields']}
					print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 799 and d['tag'] < 900:
				for j in d['subfields']:

					#for json_value in jso['datagroup']:
					if j['data'] == jso['datagroup'][0]['value']:
						jso['datagroup'].append({"taggroup":"index800","value":j['data']})	
					jso = {"datagroup":[{"taggroup":"index800","value":j['data']}], "record":r['fields']}
					print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 899 and d['tag'] < 1000:
				for j in d['subfields']:

					#for json_value in jso['datagroup']:
					if j['data'] == jso['datagroup'][0]['value']:
						jso['datagroup'].append({"taggroup":"index900","value":j['data']})
					jso = {"datagroup":[{"taggroup":"index900","value":j['data']}], "record":r['fields']}
					print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
			#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

