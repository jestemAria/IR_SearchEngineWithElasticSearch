from elasticsearch import Elasticsearch
from math import log

elastic_client = Elasticsearch()


def analyze(response, text):
    """this function separate the search query into words and then will calculate the TF-IDF for each word"""
    doc_frequency = 0
    term_frequency = 0

    list_of_ids = []
    for hit in response['hits']['hits']:
        # print(hit["_id"])
        list_of_ids.append(hit["_id"])

    # print(text)
    split_text = text.split()

    for index in range(len(list_of_ids)):
        term_vectors = elastic_client.termvectors(index="hamshahri", id=list_of_ids[index],
                                                  body={"fields": ["TEXT"],
                                                        "term_statistics": True,
                                                        "field_statistics": True,
                                                        })
        # print(term_vectors)

        doc_count = term_vectors['term_vectors']['TEXT']['field_statistics']['doc_count']

        print("=" * 100)
        for word in range(len(split_text)):
            print("=" * 50)
            for field in term_vectors['term_vectors']['TEXT']['terms']:
                if field == split_text[word]:
                    doc_frequency = term_vectors['term_vectors']['TEXT']['terms'][split_text[word]]['doc_freq']
                    term_frequency = term_vectors['term_vectors']['TEXT']['terms'][split_text[word]]['term_freq']

            print("in doc id :", list_of_ids[index])
            print("document frequency for " + split_text[word] + " is " + str(doc_frequency))
            print("term frequency for " + split_text[word] + " is " + str(term_frequency))
            print("document count is " + str(doc_count))

            idf = log(doc_count / doc_frequency)
            tf_idf = term_frequency * idf

            print("tf-idf for " + split_text[word] + " is " + str(tf_idf))
