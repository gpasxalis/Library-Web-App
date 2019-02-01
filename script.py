# -*- coding: utf-8 -*-
import json

with open('test.json') as json_file:  
	data = json.load(json_file)
	flag_array = []
	c=0
	
	for r in data['test']:
		for d in r['fields']:
			#flag = 0
			subfields_flag = False			
			if d['tag'] > 9 and d['tag'] < 100:
				for j in d['subfields']:		
					jso = {"datagroup":[{"taggroup":"index10","value":j['data']}], "record":r['fields']}
					#print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 99 and d['tag'] < 200:
				for j in d['subfields']:
					jso = {"datagroup":[{"taggroup":"index100","value":j['data']}], "record":r['fields']}
					#print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 199 and d['tag'] < 300:
				for j in d['subfields']:
					subfields_flag = False
					for flag in flag_array:
						print(flag)
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False: 
							
						#for json_value in jso['datagroup']:
						#if j['data'] == jso['datagroup'][0]['value']:
						jso = {"datagroup":[{"taggroup":"index200","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#print("flag!")
											c = c+1
						flag_array.append(j['data'])
										#print(j1['data'])
										
					
					#print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
					#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 299 and d['tag'] < 400:
				for j in d['subfields']:
					subfields_flag = False
					for flag in flag_array:
						print(flag)
					#for json_value in jso['datagroup']:
					#if j['data'] == jso['datagroup'][0]['value']:
					subfields_flag = False
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False: 
						jso = {"datagroup":[{"taggroup":"index300","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#print("flag!")
											c = c+1
						flag_array.append(j['data'])
										#print(j1['data'])
										#print(jso['datagroup'][0]['value'],"->",j1['data'])
					
					
					#print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))
					#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				
			if d['tag'] > 399 and d['tag'] < 500:
				for j in d['subfields']:
					subfields_flag = False
					for flag in flag_array:
						print(flag)
					#for json_value in jso['datagroup']:
					#if j['data'] == jso['datagroup'][0]['value']:
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False: 
						jso = {"datagroup":[{"taggroup":"index400","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#print("flag!")
											c = c+1
						flag_array.append(j['data'])
										#print(jso['datagroup'][0]['value'],"->",j1['data'])

					
					#print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 499 and d['tag'] < 600:
				for j in d['subfields']:
					subfields_flag = False
					for flag in flag_array:
						print(flag)
					#for json_value in jso['datagroup']:
					#if j['data'] == jso['datagroup'][0]['value']:
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False: 
						jso = {"datagroup":[{"taggroup":"index500","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#print("flag!")
											c = c+1
						flag_array.append(j['data'])
										#print(jso['datagroup'][0]['value'],"->",j1['data'])
					
					#print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 599 and d['tag'] < 700:
				for j in d['subfields']:
					subfields_flag = False
					for flag in flag_array:
						print(flag)
					#for json_value in jso['datagroup']:
					#if j['data'] == jso['datagroup'][0]['value']:
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False: 
						jso = {"datagroup":[{"taggroup":"index600","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#print("flag!")
											c = c+1
						flag_array.append(j['data'])
										#print(jso['datagroup'][0]['value'],"->",j1['data'])
					
					#print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 699 and d['tag'] < 800:
				for j in d['subfields']:
					subfields_flag = False
					for flag in flag_array:
						print(flag)
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False: 
						jso = {"datagroup":[{"taggroup":"index700","value":j['data']}], "record":r['fields']}
						#for json_value in jso['datagroup']:
						#if j['data'] == jso['datagroup'][0]['value']:
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#print("flag!")
											c = c+1
						flag_array.append(j['data'])
										#print(jso['datagroup'][0]['value'],"->",j1['data'])
					
					#print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 799 and d['tag'] < 900:
				for j in d['subfields']:
					subfields_flag = False
					for flag in flag_array:
						print(flag)
					#for json_value in jso['datagroup']:
					#if j['data'] == jso['datagroup'][0]['value']:
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False: 
						jso = {"datagroup":[{"taggroup":"index800","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value'] and j1['data'] != j['data']:
											#print("flag!")
											c = c+1
						flag_array.append(j['data'])
										#print(jso['datagroup'][0]['value'],"->",j1['data'])
					
					#print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 899 and d['tag'] < 1000:
				for j in d['subfields']:
					subfields_flag = False
					for flag in flag_array:
						print(flag)
					#for json_value in jso['datagroup']:
					#if j['data'] == jso['datagroup'][0]['value']:
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False: 
						jso = {"datagroup":[{"taggroup":"index900","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value'] and j1['data'] != j['data']:
											#print("flag!")
											c = c+1
						flag_array.append(j['data'])
										#print(jso['datagroup'][0]['value'],"->",j1['data'])
					
					#print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
					#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
			#print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

