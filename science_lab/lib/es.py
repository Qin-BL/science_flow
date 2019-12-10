
from settings import ES_CONF
from elasticsearch import Elasticsearch


es = Elasticsearch(ES_CONF)


async def get_es_search(index, body):
    es = Elasticsearch(ES_CONF)
    res = es.search(index=index, doc_type='all', body=body, timeout='2s')
    return res


async def update_es_search(index, id, **kwargs):
    es = Elasticsearch(ES_CONF)
    inline = ";".join(["ctx._source.%s = params.%s" % (i, i) for i in kwargs.keys()])
    updateBody = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"_id": id}}
                ],
            }
        },
        "script": {
            "inline": inline,
            "params": kwargs,
            "lang": "painless"
        }
    }
    res = es.update_by_query(index=index, doc_type='all', body=updateBody, timeout='2s')
    if not res['updated']:
        return False
    return True
