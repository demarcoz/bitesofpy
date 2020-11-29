import collections
import os
import urllib.request

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    return data.splitlines()


def cleanup_text(raw_text):
    raw_text = raw_text.lower()
    return "".join([_ for _ in raw_text if _.isalpha() or _ == " "])


def remove_stopwords(text, stopwords):
    cleaned_text = " ".join([_ for _ in text.split() if _ not in stopwords])
    return cleaned_text


def get_harry_most_common_word():
    stopwords = get_words(stopwords_file)
    raw_text = get_words(harry_text)
    raw_text = " ".join(raw_text)
    text = cleanup_text(raw_text)
    cleaned_text = remove_stopwords(text, stopwords)
    return collections.Counter(cleaned_text.split()).most_common(1)[0]
