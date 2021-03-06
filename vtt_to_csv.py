import os
import re
from nltk import tokenize
import csv


def remove_tags(fileContents):
    """Removes <c> tags"""
    replacement = re.sub(r'<c[.\w\d]*>', '', fileContents)
    replacement = re.sub(r'</c[.\w\d]*>', '', replacement)
    replacement = re.sub(r'</c>', '', replacement)

    return replacement

def tokenize_text():
    """Extracts all the text from the vtt file, removes all the newlines and tokenizes the sentences into a list."""
    vtt_files = [x for x in os.listdir("./") if x.endswith(".vtt")]
    text = ''
    for x in vtt_files:
        print(f"Found {len(vtt_files)} .vtt file(s).")
        with open("{}".format(x), 'r') as subtitles:
            lines = subtitles.readlines()
            for line in lines:
                if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}',
                                                                     line) is None and re.search('^$', line) is None:
                    text += ' ' + line.rstrip('\n')
                text = text.lstrip()
    text = remove_tags(text)
    return tokenize.sent_tokenize(text)


def find_matching_sentences():
    """Checks the csv file provided by the user which contains the word list and finds a match in the sentences
    extracted with tokenize_text."""
    csv_files = [x for x in os.listdir("./") if x.endswith(".csv")]
    sentences = tokenize_text()
    matching_sentences = []
    for x in csv_files:
        if x != 'words_with_sentences.csv':
            with open("{}".format(x), 'r') as list_words:
                reader = csv.reader(list_words)
                for word in reader:
                    if word:
                        matching_sentence = [sentence for sentence in sentences if word[0].lower() in sentence.lower()]
                        matching_sentences.append(matching_sentence)
    return matching_sentences


def create_list_words():
    """Creates a list with the words from the csv file provided by the user."""
    csv_files = [x for x in os.listdir("./") if x.endswith(".csv")]
    words = []
    for x in csv_files:
        if x != 'words_with_sentences.csv':
            with open("{}".format(x), 'r') as list_words:
                reader = csv.reader(list_words)
                for word in reader:
                    if word:
                        words.append(word[0])
    return words


def create_csv(matching_sentences, words):
    """Creates the csv file. The first column is the list of words, and the second column is the matching sentences.
    If there is no matching sentence, the entry is left blank."""
    with open("words_with_sentences.csv", "w") as words_with_sentences:
        writer = csv.writer(words_with_sentences)
        i = 0
        while i < len(words):
            # This line checks if there is a matching sentence.
            if matching_sentences[i]:
                writer.writerow([words[i], *matching_sentences[i]])
            else:
                writer.writerow([words[i], ""])
            i += 1


if __name__ == '__main__':

    create_csv(find_matching_sentences(), create_list_words())
    print("The file(s) have been processed. A file called 'words_with_sentences.csv' has been created.")
