from nltk.corpus import stopwords
import re

def letters_only(text):
    letters = re.sub("[^a-zA-Z]", " ", text)
    return letters
def lower_only(text):
    return text.lower().split()

def remove_stopwords(text):
    no_stopwords = [word for word in text if word not in stopwords.words("english")]
    print(( " ".join(no_stopwords )))
    return no_stopwords

