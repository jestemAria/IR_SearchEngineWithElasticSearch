from elasticsearch import Elasticsearch, helpers

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
"""with options bellow we can specify settings and mapping manually for the index"""

options = '''{
"settings": {
    "index": {
            "similarity": {
                "text_similarity": {
                     "type" : "DFR",
                     "basic_model" : "g",
                     "after_effect" : "l",
                     "normalization" : "h2",
                     "normalization.h2.c" : "3.0"
                }
            }
        },
        "analysis": {
            "analyzer": {
                "custom_analyzer": {
                    "tokenizer": "standard",
                      "filter": [
                        "lowercase",
                        "decimal_digit",
                        "arabic_normalization",
                        "persian_normalization",
                        "persian_stop"
                      ]
                }
            },
            "filter": {
                "custom_stop": {
                    "type":       "stop",
                    "stopwords": "stopwords.txt"
                },
                "persian_stop": {
                  "type":       "stop",
                  "stopwords":  "_persian_"
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "DOCID": {
              "type": "text",
              "index": false
            },
            "CAT": {
              "type": "text",
              "analyzer": "persian"
            },
            "TITLE": {
              "type": "text",
              "analyzer": "persian",
              "similarity": "text_similarity"
            },
            "TEXT": {
              "type": "text",
              "analyzer": "persian"
            }
        }
    }
}'''

response = es.indices.create(index="hamshahri", ignore=400, body=options)
print(response)
