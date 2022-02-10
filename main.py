from elasticsearch import Elasticsearch
import output
import statistics
import text_processing
import text_autocomplete
elastic_client = Elasticsearch()

while True:
    text = input("عبارت مورد نظر خود را وارد کنید: " + "\n")

    if text[-1:] == "؟":
        final_text = text[:-2]
        print("لطفا منتظر بمانید...")
        break
    else:
        print("لطفا منتظر بمانید...")
        text_autocomplete.auto_complete(text)

final_text = text_processing.correct_spelling(final_text)

# Python dictionary object representing an Elasticsearch JSON query:
search_param = {
    "_source": ["TITLE", "TEXT"],
    "query": {
        "match_phrase": {
            "TEXT": "%s" % final_text
        }
    }
}

response = elastic_client.search(index="hamshahri", body=search_param)
statistics.analyze(response, final_text)
output.show_result(response)
