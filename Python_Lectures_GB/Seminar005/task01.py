"""Напишите программу, удаляющую из текста все слова, содержащие ""абв""."""


def delete_abv_words(text):
    words = [i for i in text.split()]
    for word in words:
        if 'абв' in word:
            words.remove(word)
    return ' '.join(words)


sentence = input('Введите текст: ')
print(delete_abv_words(sentence))