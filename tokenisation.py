from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
def tokenize(text):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens]
    stop_words = set(stopwords.words('english'))
    return [w for w in tokens if w.isalpha() and w not in stop_words]