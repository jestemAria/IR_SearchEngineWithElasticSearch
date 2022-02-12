from colorama import init
from termcolor import colored

init()


def show_result(json_data):
    """this is a TUI for showing results, it's a function that takes a json_data and separate each part of it and
    parse it to show it in a TUI"""

    took = get_took(json_data)
    timed_out = is_timed_out(json_data)
    no_result = has_not_any_result(json_data)
    numbers_of_documents = get_numbers_of_documents(json_data)

    print("\n" * 5)
    print(colored(" " * 250, "yellow", 'on_white', attrs=['bold']))

    if timed_out:
        print(colored("مدت زمان برای انجام درخواست به پایان رسید", "white", 'on_red', attrs=['bold']))

    else:
        print(colored("مدت زمان بازیابی اطلاعات: {} میلی ثانیه".format(took), "white", 'on_green', attrs=['bold']))
        if no_result:
            print("هیچ نتیجه ای برای این درخواست پیدا نشد :(")
        else:
            print(colored("تعداد سندها: {}".format(numbers_of_documents), "white", 'on_green', attrs=['bold']))
            print(colored(" " * 250, "yellow", 'on_blue', attrs=['bold']))
            print(colored("نتایج جستجو:", "green", attrs=['bold']))
            for hit in json_data['hits']['hits']:
                print('\n')
                show_doc_id(hit['_id'])
                show_score(hit['_score'])
                show_title(hit['_source']['TITLE'])
                show_text(hit['_source']['TEXT'])
                print(colored(" " * 250, "yellow", 'on_blue'))


def get_took(json_data):
    return json_data['took']


def is_timed_out(json_data):
    if json_data['timed_out']:
        return True
    else:
        return False


def has_not_any_result(json_data):
    if json_data['hits']['total']['value'] == 0:
        return True
    else:
        return False


def get_numbers_of_documents(json_data):
    return json_data['hits']['total']['value']


def show_doc_id(doc_id):
    print(colored("شناسه سند: {}".format(doc_id), "white", 'on_green', attrs=['bold']))


def show_score(score):
    print(colored("امتیاز: {}".format(score), "white", 'on_magenta', attrs=['bold']))


def show_title(title):
    print('\n')
    print(colored("عنوان", "white", 'on_cyan', attrs=['bold']))
    print(colored(title, "cyan", attrs=['bold']))


def show_text(text):
    shorted_text = text[:500]
    print('\n')
    print(colored("متن", "white", 'on_cyan', attrs=['bold']))
    print(colored(shorted_text, "cyan"))
