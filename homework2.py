# Temp file for development
from collections import Counter

spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]


def count_occurrences(corpus, count):
    """ Referenced: https://www.geeksforgeeks.org/python-combine-two-dictionary-adding-values-for-common-keys/
    https://stackoverflow.com/questions/764235/dictionary-to-lowercase-in-python"""
    for email in corpus:
        count += Counter(email)
    thing = dict((k.lower(), v) for k, v in count.items())
    return thing


bad = count_occurrences(spam_corpus, Counter())
print(bad)
good = count_occurrences(ham_corpus, Counter())
print(good)
nbad = len(spam_corpus)
ngood = len(ham_corpus)
print(nbad)
print(ngood)


# Set g = 2 * the word's good value (or 0 if there is no value)
# Set b = the word's bad value (or 0)
# If g + b > 5
# return max(0.01, min(0.99, min(1.0, b / nbad) / (min(1.0, g / ngood) + min(1.0, b / nbad))))
# Else
# return 0

def probability_email_containing_word_is_spam(word):
    g = 2*good[word]
    b = bad[word]
    if g + b > 1:  # changed to one
        return max(0.01, min(0.99, min(1.0, b / nbad) / (min(1.0, g / ngood) + min(1.0, b / nbad))))
    else:
        return 0


