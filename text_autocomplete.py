import wikipedia
from googletrans import Translator

translator = Translator()


def auto_complete(text):
    final_suggests = []
    wikipedia_results = wikipedia.search(text, results=4)
    # print(wikipedia_results)

    for result in wikipedia_results:
        final_suggests.append(translator.translate(result, src='en', dest='fa').text)

    print("پیشنهاد برای شما: ")
    for result in final_suggests:
        print(result + "\t")

    # TODO: RETURN FALSE IF NO SUGGESTIONS
