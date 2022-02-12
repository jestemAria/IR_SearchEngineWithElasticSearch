from parsivar import SpellCheck


def correct_spelling(text):
    """this function is used to correct spelling errors in a given text"""
    spell_checker = SpellCheck()
    corrected_text = spell_checker.spell_corrector(text)
    if corrected_text != text:
        print("آیا منظور شما این بود؟ ")
        print(corrected_text)
        return clean_stop_words_in_query(corrected_text)
    else:
        return clean_stop_words_in_query(text)


def clean_stop_words_in_query(text):
    """this function is used to clean stop words in a given text"""
    stopword_list = []

    with open("stop_words.txt", encoding="utf-8") as stop_file:
        stopword_lines = stop_file.readlines()
        for words in stopword_lines:
            for word in words.split(","):
                word = word[:-1]
                word = word[1:]
                stopword_list.append(word)
                # print(word)
            # print(stopword_list)

        text = text.split()
        # print(text)
        for word in text:
            if word in stopword_list:
                text.remove(word)
        cleaned_text = " ".join(text)

        cleaned_text = substitute_persian_with_arabic(cleaned_text)
        print("LOG ->", "پاکسازی نهایی:", cleaned_text)
        return cleaned_text


def substitute_persian_with_arabic(cleaned_text):
    """this function is used to substitute persian with arabic in a given text"""
    for letter in cleaned_text:
        if letter == "ک":
            cleaned_text = cleaned_text.replace(letter, "ك")
        if letter == "ی":
            cleaned_text = cleaned_text.replace(letter, "ي")
    return cleaned_text

"""for test you can test this text"""
# correct_spelling("علی از  خاانه در تاریکی با ۲۲ کیلومتر صرعت بیرون می آید")
