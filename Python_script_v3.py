# -*- coding: utf-8 -*-
import json

with open('test.json') as json_file:  
	data = json.load(json_file)
	flag_array = []
	
	for r in data['test']:

		for d in r['fields']:
			#flag = 0	
			#fields_flag = False
			subfields_flag = False
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
					
					subfields_flag = False
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False:
						counter = 0
						jso = {"datagroup":[{"taggroup":"index200","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#jso['datagroup'].append({"taggroup":"flag","value":j1['data']})
											counter += 1
										#else:
										#	counter += 1
													
						flag_array.append(j['data'])
												#logical_flag = False
												#print("\nFound duplicate ",j1['data']," with ",jso['datagroup'][0]['value'])
						for p in range(0,counter-1):
							jso['datagroup'].append({"taggroup":"flag","value":j['data']})

						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 299 and d['tag'] < 400:
				
				for j in d['subfields']:
					
					subfields_flag = False
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False:
						counter = 0
						jso = {"datagroup":[{"taggroup":"index300","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#jso['datagroup'].append({"taggroup":"flag","value":j1['data']})
											counter += 1
										#else:
										#	counter += 1
													
						flag_array.append(j['data'])
												#logical_flag = False
												#print("\nFound duplicate ",j1['data']," with ",jso['datagroup'][0]['value'])
						for p in range(0,counter-1):
							jso['datagroup'].append({"taggroup":"flag","value":j['data']})
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))
				
			elif d['tag'] > 399 and d['tag'] < 500:
				
				for j in d['subfields']:
					
					subfields_flag = False
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False:
						counter = 0 
						jso = {"datagroup":[{"taggroup":"index400","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#jso['datagroup'].append({"taggroup":"flag","value":j1['data']})
											counter += 1
										#else:
										#	counter += 1
													
						flag_array.append(j['data'])
												#logical_flag = False
												#print("\nFound duplicate ",j1['data']," with ",jso['datagroup'][0]['value'])
						for p in range(0,counter-1):
							jso['datagroup'].append({"taggroup":"flag","value":j['data']})
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 499 and d['tag'] < 600:
				
				for j in d['subfields']:
					
					subfields_flag = False
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False:
						counter = 0
						jso = {"datagroup":[{"taggroup":"index500","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#jso['datagroup'].append({"taggroup":"flag","value":j1['data']})
											counter += 1
										#else:
										#	counter += 1
													
						flag_array.append(j['data'])
												#logical_flag = False
												#print("\nFound duplicate ",j1['data']," with ",jso['datagroup'][0]['value'])
						for p in range(0,counter-1):
							jso['datagroup'].append({"taggroup":"flag","value":j['data']})
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 599 and d['tag'] < 700:
				
				for j in d['subfields']:
					
					subfields_flag = False
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False:
						counter = 0 
						jso = {"datagroup":[{"taggroup":"index600","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#jso['datagroup'].append({"taggroup":"flag","value":j1['data']})
											counter += 1
										#else:
										#	counter += 1
													
						flag_array.append(j['data'])
												#logical_flag = False
												#print("\nFound duplicate ",j1['data']," with ",jso['datagroup'][0]['value'])
						for p in range(0,counter-1):
							jso['datagroup'].append({"taggroup":"flag","value":j['data']})
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 699 and d['tag'] < 800:
				
				for j in d['subfields']:
					
					subfields_flag = False
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False:
						counter = 0 
						jso = {"datagroup":[{"taggroup":"index700","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#jso['datagroup'].append({"taggroup":"flag","value":j1['data']})
											counter += 1
										#else:
										#	counter += 1
													
						flag_array.append(j['data'])
												#logical_flag = False
												#print("\nFound duplicate ",j1['data']," with ",jso['datagroup'][0]['value'])
						for p in range(0,counter-1):
							jso['datagroup'].append({"taggroup":"flag","value":j['data']})
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))



			elif d['tag'] > 799 and d['tag'] < 900:
				
				for j in d['subfields']:
					counter = 0
					subfields_flag = False
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False: 
						jso = {"datagroup":[{"taggroup":"index800","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#jso['datagroup'].append({"taggroup":"flag","value":j1['data']})
											counter += 1
										#else:
										#	counter += 1
													
						flag_array.append(j['data'])
												#logical_flag = False
												#print("\nFound duplicate ",j1['data']," with ",jso['datagroup'][0]['value'])
						for p in range(0,counter-1):
							jso['datagroup'].append({"taggroup":"flag","value":j['data']})

						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))

			elif d['tag'] > 899 and d['tag'] < 1000:
				
				for j in d['subfields']:
					counter = 0
					subfields_flag = False
					for flag in flag_array:
						if j['data'] == flag:
							subfields_flag = True	
					if subfields_flag == False: 
						jso = {"datagroup":[{"taggroup":"index900","value":j['data']}], "record":r['fields']}
						for r1 in data['test']:
							for d1 in r1['fields']:
								if d1['tag'] > 9:
									for j1 in d1['subfields']:
										if j1['data'] == jso['datagroup'][0]['value']:
											#jso['datagroup'].append({"taggroup":"flag","value":j1['data']})
											counter += 1
										#else:
										#	counter += 1
													
						flag_array.append(j['data'])
												#logical_flag = False
												#print("\nFound duplicate ",j1['data']," with ",jso['datagroup'][0]['value'])
						for p in range(0,counter-1):
							jso['datagroup'].append({"taggroup":"flag","value":j['data']})
						print(json.dumps({"index":{"_index":"lib-index", "_type":"lib-data"}},ensure_ascii=False,separators=(',', ':')))					
						print(json.dumps(jso,ensure_ascii=False,separators=(',', ':')))


			
		

