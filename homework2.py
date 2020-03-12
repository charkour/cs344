# Temp file for development
from collections import Counter

THRESHOLD = 1

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
good = count_occurrences(ham_corpus, Counter())
nbad = len(spam_corpus)
ngood = len(ham_corpus)

g_keys = list(good.keys())
b_keys = list(bad.keys())
# https://stackoverflow.com/questions/1319338/combining-two-lists-and-removing-duplicates-without-removing-duplicates-in-orig
combined_keys = b_keys
combined_keys.extend(k for k in g_keys if k not in combined_keys)



def probability_email_containing_word_is_spam(word):
    """Adapted from the article"""
    g = 2*good[word] if word in good else 0
    b = bad[word] if word in bad else 0
    if g + b > THRESHOLD:  # changed to one
        return max(0.01, min(0.99, min(1.0, b / nbad) / (min(1.0, g / ngood) + min(1.0, b / nbad))))
    else:
        return 0

# create a third hash


probs = dict()
for key in combined_keys:
    probs[key] = probability_email_containing_word_is_spam(key)

print(probs)

# TODO: Add the other function!!!

# TODO: What makes it Bayesian?
'''
This is Bayesian because it uses a bayesian combination of probabilities. MORE!!!
'''

"""
Set prod = the product of the elements of probs
Return prod / (prod + (the product of the complement of the elements of probs))
"""
def calculate_spam_prob(email):
    prod = 1
    complement = 1
    for element in email:
        prod *= probs[element.lower()]
        complement *= (1 - probs[element.lower()])
    return prod / (prod + complement)

print(calculate_spam_prob(ham_corpus[0]))
print(calculate_spam_prob(ham_corpus[1]))
print(calculate_spam_prob(spam_corpus[0]))
print(calculate_spam_prob(spam_corpus[1]))


"""
Part 2: Join prob = 2^4 = 16
bayesian: 9
With the Bayesian network structure, we are able to make simplifications due to the assumptions based 
on how the network is structured.

"""



