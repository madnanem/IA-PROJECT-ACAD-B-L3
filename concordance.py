from nltk.text import Text
def get_concordance(tokens, word):
    text_obj = Text(tokens)
    return text_obj.concordance_list(word, width=50, lines=10)