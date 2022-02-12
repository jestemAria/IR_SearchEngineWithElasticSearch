import wikipedia
from googletrans import Translator

translator = Translator()


def auto_complete(text):
    """for auto completion the program uses wikipedia api and it returns the top 4 results in english
    so google translate api will translate them back to persian"""
    final_suggests = []
    wikipedia_results = wikipedia.search(text, results=4)
    # print(wikipedia_results)

    for result in wikipedia_results:
        final_suggests.append(translator.translate(result, src='en', dest='fa').text)

    print("پیشنهاد برای شما: ")
    for result in final_suggests:
        print(result + "\t")
