def counting_words_in_text(text):
    words_counter = 0
    for _ in text:
        words_counter += 1

    print(f"Колличесвто слов в тексте: {words_counter}")


def finding_longest_word(text):
    longest_word = text[0]
    max_length = len(longest_word)

    for word in text[1:]:
        current_length = len(word)
        if current_length > max_length:
            max_length = current_length
            longest_word = word

    print(f"Самое длинное слово в тексте: {longest_word}")


def split_text(text):
    words = text.lower().split()
    return words


def remove_punctuation_from_text(text):
    symbols_for_remove = """.,!?:;/('")[]{}<+-*>@#$%^"""
    for symbol in symbols_for_remove:
        text = text.replace(symbol, " ")

    return text


def counting_vowels_in_text(text):
    vowels_counter = 0
    vowels = "аеёиоуыэюя"
    for letter in text:
        if letter.lower() in vowels:
            vowels_counter += 1

    print(f"Колличество гласных в тексте: {vowels_counter}шт.")


def repeating_words_in_text(text):
    words_count = {}

    for word in text:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    for word, count in words_count.items():
        print(f"Слово {word} повторяется {count} раз/раза")


while True:
    user_text_input = input("Введите текст: ")
    if not user_text_input:
        print("Пустой текст.")
    else:
        clean_text = remove_punctuation_from_text(user_text_input)
        clean_split_text = split_text(clean_text)
        counting_words_in_text(clean_split_text)
        finding_longest_word(clean_split_text)
        counting_vowels_in_text(clean_text)
        repeating_words_in_text(clean_split_text)
        break