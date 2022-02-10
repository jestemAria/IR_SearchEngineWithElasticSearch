import xmltodict
import json
import os
from xml.parsers.expat import ExpatError
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# options = '''{
#     "settings": {
#         "index": {
#             "similarity": {
#                 "text_similarity": {
#                      "type" : "DFR",
#                      "basic_model" : "g",
#                      "after_effect" : "l",
#                      "normalization" : "h2",
#                      "normalization.h2.c" : "3.0"
#                 }
#             }
#         },
#         "analysis": {
#             "analyzer": {
#                 "custom_analyzer": {
#                     "tokenizer": "standard",
#                       "filter": [
#                         "lowercase",
#                         "decimal_digit",
#                         "arabic_normalization",
#                         "persian_normalization",
#                         "persian_stop"
#                       ]
#                 }
#             },
#             "filter": {
#                 "custom_stop": {
#                     "type":       "stop",
#                     "stopwords": ["و","در","به","از","که","می","این","است","را","با","های","برای","آن","یک","شود","شده","خود","ها","کرد","شد","ای","تا"
#                                   ,"کند","بر","بود","گفت","نیز","وی","هم","کنند","دارد","ما","کرده","یا","اما","باید","دو","اند","هر","خواهد","او","مورد","آنها","باشد","دیگر",
#                                   "مردم","نمی","بین","پیش","پس","اگر","همه","صورت","یکی","هستند","بی","من","دهد","هزار","نیست","استفاده","داد","داشته","راه","داشت","چه","همچنین","کردند","داده",
#                                   "بوده","دارند","همین","میلیون","سوی","شوند","بیشتر","بسیار","روی","گرفته","هایی","تواند","اول","نام","هیچ","چند","جدید","بیش","شدن","کردن","کنیم","نشان","حتی",
#                                   "اینکه","ولی","توسط","چنین","برخی","نه","دیروز","دوم","درباره","بعد","مختلف","گیرد","شما","گفته","آنان","بار","طور","گرفت","دهند","گذاری","بسیاری","طی","بودند","میلیارد",
#                                   "بدون","تمام","کل","تر","براساس","شدند","ترین","امروز","باشند","ندارد","چون","قابل","گوید","دیگری","همان","خواهند","قبل","آمده","اکنون","تحت","طریق","گیری","جای","هنوز","چرا",
#                                   "البته","کنید","سازی","سوم","کنم","بلکه","زیر","توانند","ضمن","فقط","بودن","حق","آید","وقتی","اش","یابد","نخستین","مقابل","خدمات","امسال","تاکنون","مانند","تازه","آورد","فکر","آنچه","نخست","نشده",
#                                   "شاید","چهار","جریان","پنج","ساخته","زیرا","نزدیک","برداری","کسی","ریزی","رفت","گردد","مثل","آمد","ام","بهترین","دانست","کمتر","دادن","تمامی","جلوگیری","بیشتری","ایم","ناشی","چیزی","آنکه","بالا","بنابراین",
#                                   "ایشان","بعضی","دادند","داشتند","برخوردار","نخواهد","هنگام","نباید","غیر","نبود","دیده","وگو","داریم","چگونه","بندی","خواست","فوق","ده","نوعی","هستیم","دیگران","همچنان","سراسر","ندارند","گروهی","سعی","روزهای","آنجا",
#                                   "یکدیگر","کردم","بیست","بروز","سپس","رفته","آورده","نماید","باشیم","گویند","زیاد","خویش","همواره","گذاشته","شش","نداشته","شناسی","خواهیم","آباد","داشتن","نظیر","همچون","باره","نکرده","شان","سابق","هفت","دادند","جایی",
#                                   "بی","جز","زیر","رویِ","سریِ","تویِ","جلویِ","پیشِ","عقبِ","بالایِ","خارجِ","وسطِ","بیرونِ","سویِ","کنارِ","پایینِ","نزدِ","نزدیکِ","دنبالِ","حدودِ","برابر","طبقِ","مانندِ","ضدِّ","هنگامِ","برایِ","مثلِ",
#                                   "اثرِ","تولِ","علتِ","سمتِ","عنوانِ","قصدِ","روب","جدا","کی","که","چیست","هست","کجا","کجاست","چطور","کدام","آیا","مگر","چندین","یک","چیزی","دیگر","کسی","بعری","هیچ","چیز","جا","کس","هرگز",
#                                   "یا","تنها","بلکه","خواه","بله","بلی","آره","آری","مرسی","البتّه","لطفاً","آنکه","وقتیکه","همین","پیش","مدّتی","هنگامی","مان","تان","ی","ور","هممون","وی","کنن","کنند","میکنند","میکنن","نزدیم","نمیموند",
#                                   "دارای","خودی","وگرد","همانند","بشوند","نمیکنند","انها","بازم","پیششون","ابدا","عمدتا","بندی","مند","آخه","آورده","میباشد","ساخته‌ام","میگردد","درباره","میدهم","خویش","دوباره","پراز","هشان","بتوان","مینوشند","داشتند","میخواستند",
#                                   "در","تو","با","که","به","هم","از","نمیگیرند","بین","بینمان","بیاریم","بدهید","نکنند","گذاری","ما","نمیاورم","خواست","رفته ام","هایت","همچنانکه","تان","تنها","میخواهند","دچار","شناسید","خودی","بوجود","همانند",
#                                   "دارای","بریزید","کنیم","کنم","چی","می","بعدا","هاش","گرچه","ازش","باشه","شدید","نشون","رسید","بری","دارم","الی","گه","اینطوری","کلی","ی","توی","هستن","اون","میشه","شو","بشم","برید",
#                                   "باشه","واقعا","رو","اینجا","وارد","اینکه","آیا","یعنی","شرط","بدان","نباش","علیرغم","علارغم","خیلی"]
#                 },
#                 "persian_stop": {
#                   "type":       "stop",
#                   "stopwords":  "_persian_"
#                 }
#             }
#         }
#     },
#     "mappings": {
#         "news": {
#             "properties": {
#                 "DOCID": {
#                     "type": "text",
#                     "index": false
#                 },
#                 "CAT": {
#                     "type": "text",
#                     "analyzer": "parsi"
#                 },
#                 "TITLE": {
#                     "type": "text",
#                     "analyzer": "parsi",
#                     "similarity": "text_similarity"
#                 },
#                 "TEXT": {
#                     "type": "text",
#                     "analyzer": "parsi"
#                 }
#             }
#         }
#     }
# }'''

path = "./"
for index, file in enumerate(os.listdir(path)):
    if file.endswith(".xml"):
        print(index)
        with open(file, "rb") as xml:
            documents = []

            try:
                r = xmltodict.parse(xml)
                results = json.loads(json.dumps(r, ensure_ascii=False))['HAMSHAHRI2']['DOC']

                for result in results:

                    del result["ISSUE"]
                    del result["ORIGINALFILE"]
                    del result["DATE"]
                    del result["DOCNO"]

                    result['CAT'][0] = result["CAT"][0]["#text"]
                    result['CAT'][1] = result["CAT"][1]["#text"]

                    try:
                        if isinstance(result["TEXT"], dict):
                            result['TEXT'] = str(result['TEXT']["#text"])

                    except KeyError:
                        result['TEXT'] = str(result['TEXT'])

                    document = {}
                    document["_source"] = result
                    document["_type"] = "_doc"
                    document["_index"] = "hamshahri"

                    documents.append(document)
                    # print(document)

                helpers.bulk(es, documents)

            except ExpatError:
                print("not well-formed")
