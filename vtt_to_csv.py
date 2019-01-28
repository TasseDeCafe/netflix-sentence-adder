import os
import re
from nltk import tokenize
import csv


def tokenize_text():
    vtt_files = [x for x in os.listdir("./") if x.endswith(".vtt")]
    text = ''
    for x in vtt_files:
        with open("{}".format(x), 'r') as subtitles:
            lines = subtitles.readlines()
            for line in lines:
                if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}',
                                                                     line) is None and re.search('^$', line) is None:
                    text += ' ' + line.rstrip('\n')
                text = text.lstrip()
    return tokenize.sent_tokenize(text)


def find_matching_sentences():
    csv_files = [x for x in os.listdir("./") if x.endswith(".csv")]
    sentences = tokenize_text()
    matching_sentences = []
    for x in csv_files:
        with open("{}".format(x), 'r') as list_words:
            reader = csv.reader(list_words)
            for word in reader:
                matching_sentence = [sentence for sentence in sentences if word[0] in sentence]
                matching_sentences.append(matching_sentence)
    return matching_sentences


def create_list_words():
    csv_files = [x for x in os.listdir("./") if x.endswith(".csv")]
    words = []
    for x in csv_files:
        if x != 'words_with_sentences.csv':
            with open("{}".format(x), 'r') as list_words:
                reader = csv.reader(list_words)
                for word in reader:
                    words.append(word[0])
    return words


def create_csv(matching_sentences, words):
    with open("words_with_sentences.csv", "w") as words_with_sentences:
        writer = csv.writer(words_with_sentences)
        i = 0
        while i < len(words):
            if len(matching_sentences[i]) >= 1:
                writer.writerow([words[i], matching_sentences[i][0]])
            else:
                writer.writerow([words[i], ""])
            i += 1


if __name__ == '__main__':

    create_csv(find_matching_sentences(), create_list_words())

# Let's add a comment.