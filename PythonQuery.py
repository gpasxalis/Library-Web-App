from elasticsearch import Elasticsearch
es = Elasticsearch()

res = es.search(index="test", body={"query": {"match": {"data": "viaf"}}})
res1 = es.search(index="test", body={"query": {"match": {"data": "mitsos"}}})
res2 = es.search(index="test", body={"query": {"match": {"data": "GRANT DUFF"}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(data)s" % hit["_source"])
#for doc in res['hits']['hits']:
   # print("ID: %s, %s" % (doc['_id'], doc['_source']['data']))
	
print("Got %d Hits:" % res1['hits']['total'])
for hit in res1['hits']['hits']:
    print("%(data)s" % hit["_source"])
#for doc in res1['hits']['hits']:
   # print("ID: %s, %s" % (doc['_id'], doc['_source']['data']))

print("Got %d Hits:" % res2['hits']['total'])
for hit in res2['hits']['hits']:
    print("%(data)s" % hit["_source"])
#for doc in res2['hits']['hits']:
    #print("ID: %s, %s" % (doc['_id'], doc['_source']['data']))



