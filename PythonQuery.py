from elasticsearch import Elasticsearch
es = Elasticsearch()

res = es.search(index="test", body={"data": viaf}})
res1 = es.search(index="test", body={"data": mitsos}})
print("Got %d Hits:" % res['hits']['total'])
print("Got %d Hits:" % res1['hits']['total'])


