# -*- coding: utf-8 -*-
import json

with open('test.json') as json_file:  
	data = json.load(json_file)
	with open('test123.json', 'w', encoding='utf-8') as f:
		for r in data['test']:
			for d in r['fields']:
				#if d['tag'] > 10:
				if d['tag'] > 599 and d['tag'] < 700:
					#json_data = {"index":{"_index":"test", "_type":"data"}},{"data":d['data']}
					for j in d['subfields']:
						print(j['data'])
						#json_data = {"index":{"_index":"test", "_type":"data"}},{"data":j['data']}
						#json_str = json.dumps(json_data)
					#print(d['data'])
					
						
				#else:
				#	json_data = {"index":{"_index":"test", "_type":"data"}},{"data":d['data']}
				#	print(d['data'])
				#json.dump(json_data, f, indent=2, ensure_ascii=False)





#		for r in data['test']:
#			for d in r['fields']:
#				if d['tag'] < 10:
#					#json_data = {{"index":{"_index":"test", "_type":"data"}},{"data":d['data']}}
#					jso = {"data":d['data']}
#					print(json.dumps({"index":{"_index":"test", "_type":"data"}},ensure_ascii=False,separators=(',', ':')))
#					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
#				else:
#					for j in d['subfields']:
#						#print(j['data'])
#						#json_data = {{"index":{"_index":"test", "_type":"data"}},{"data":j['data']}}
#						#json_str = json.dumps(json_data)
#						jso = {"data":j['data']}
#						print(json.dumps({"index":{"_index":"test", "_type":"data"}},ensure_ascii=False,separators=(',', ':')))
#						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
#				#json.dump(json_data1, f)
#				#json.dump(json_data2, f)
