
ip = 'http://localhost:9200/topbeat-*/_search?pretty/'


import urllib2
import json
import time
import sort








def main():
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    
    for i in range(10):
        res=urllib2.urlopen(ip)
        result=res.read()
        d=json.loads(result)
        mem= d['hits']['hits'][0]['_source']['mem']       
        cpu= d['hits']['hits'][0]['_source']['cpu']
        fs= d['hits']['hits'][0]['_source']['swap']
        
        k=sort.sortjson()
        k.walk(d['hits'])
       
        time.sleep(5)



if __name__=="__main__":main()
