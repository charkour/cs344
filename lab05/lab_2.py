'''
This module implements the Bayesian network based on exercise 5.2

@author: kvlinden
@version Jan 2, 2013
@author: Charles Kornoelje
@version Mar 8, 2020
'''

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2}),
])

# 5.2
# a) *P*(Cancer | positive results on both tests)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# b) *P*(Cancer | a positive result on test 1, but a negative result on test 2)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

# These results make sense after thinking it through, but I was initially surprised how small the probability of having
#   cancer is if both test are true. I noticed that having one failed test, dramatically decreases the probability of
#   having cancer. The probability of having cancer when one test fails is near zero.
# a)
"""
*P*(Cancer | positive results on both tests) = 
    = *P*(C | t1 ^ t2)
    = a<P(c)P(t1|c)P(t2|c), P(~c)P(t1|~c)P(t2|~c)>
    = a<(0.01)(0.9)(0.9), (0.99)(0.2)(0.2)>
    = a<0.0081, 0.0396>
    = 20.96<0.0081, 0.0396>
    = <0.17, 0.83>
"""
# b)
"""
*P*(Cancer | a positive result on test 1, but a negative result on test 2) = 
    = *P*(C | t1 ^ ~t2)
    = a<P(c)P(t1|c)P(~t2|c), P(~c)P(t1|~c)P(~t2|~c)>
    = a<(0.01)(0.9)(0.1), (0.99)(0.2)(0.8)>
    = a<0.0009, 0.1584>
    = 6.277<0.0009, 0.1584>
    = <0.006, 0.994>
"""

