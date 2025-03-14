from elasticsearch import Elasticsearch

def create_elastic_client(host="http://localhost:9200"):
    return Elasticsearch(hosts=[host])
