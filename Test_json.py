# -*- coding: utf-8 -*-
import json

with open('test.json') as json_file:  
	data = json.load(json_file)
	with open('data.json', 'w', encoding='utf-8') as f:
		for r in data['test']:
			for d in r['fields']:
				if d['tag'] < 10:
					jso = {"data":d['data']}
					print(json.dumps({"index":{"_index":"test", "_type":"data"}},ensure_ascii=False,separators=(',', ':')))
					print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				else:
					for j in d['subfields']:
						jso = {"data":j['data']}
						print(json.dumps({"index":{"_index":"test", "_type":"data"}},ensure_ascii=False,separators=(',', ':')))
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				
