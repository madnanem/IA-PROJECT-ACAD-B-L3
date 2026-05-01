from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
def apply_stemming(tokens):
    stemmed = [] 
    for word in tokens:
    
        lemmed_word = lemmatizer.lemmatize(word, pos='v') 
        stemmed.append(lemmed_word)
    return stemmed