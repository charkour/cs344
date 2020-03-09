'''
This module implements the Bayesian network based on exercise 5.3

@author: kvlinden
@version Jan 2, 2013
@author: Charles Kornoelje
@version Mar 8, 2020
'''


from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1}),
])

# 5.3.a
# i) *P*(Raise | sunny)
print(enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())
"""
*P*(R | s)
    = *P*(R)    # Raise and Sunny do not have a casual relationship
    = a<P(s), P(~s)>
    = <0.01, 0.99>
    
Initially, I was confused on how to calculate the probability, but realized
there is not a casual relationship between Raise and Sunny. It makes sense
that whatever value Sunny is, it will not effect P(raise)'s outcome.
"""

# ii) *P*(Raise | happy ∧ sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happiness).show_approx())
"""
*P*(R | h ∧ s)
    = a*P*(R, h, s)
    = a*P*(R)P(h|r^s)P(s|r^h)
    = a<P(r)P(h|r^s)P(s|r^h), P(~r)P(h|~r^s)P(s|~r^h)>
    = a<(0.01)(1)(0.7), (0.99)(0.7)(0.7)>
    = a<0.007, 0.4851>
    = 2.03<0.007, 0.4851>
    = <0.0142, 0.9858>
    
This makes sense that if it is sunny out, the probability of a raise causing happiness is lowered
because there is a chance that the person is happy because of the sun and not a raise.
"""

# 5.3.b
# i) *P*(Raise | happy)
print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())
# This makes sense to me that your happiness is probably due to a raise, but there is a chance
#   you are happy due to the sun and not a raise. Happiness does not always mean a raise.

# ii) *P*(Raise | happy ∧ ¬sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())
# This one took a little to understand. If it is not sunny, and a person is happy, it seems that there should be raise.
#   However, it makes sense that one can be happy when there is a no raise and no sun (a 0.1 probability).
