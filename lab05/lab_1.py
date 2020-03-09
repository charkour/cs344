'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
@author: Charles Kornoelje
@version Mar 8, 2020

Updated for exercises 5.1 and 5.4
'''

from probability import BayesNet, enumeration_ask, gibbs_ask, rejection_sampling, likelihood_weighting

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
])

# 5.1.a
# i) *P*(Alarm | burglary ∧ ¬earthquake)
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# ii) *P*(John | burglary ∧ ¬earthquake)
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# iii) *P*(Burglary | alarm)
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
# iv) *P*(Burglary | john ∧ mary)
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

# These numbers make sense based on the network.

# 5.4
# None of the approximation algorithms match the exact inference algorithms.
# Enum ask (exact inference) is always <0.284, 0.716> but the other algorithms vary in result when you run them.
# The reason why the approximate algorithms change on each run is due to their random nature.
print("Enumeration Ask: ", enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

# Rejection sampling is different from exact inference because it generates random samples from the distribution and
#   then rejects samples that don't match the evidence. It ends up rejecting many samples, especially when the
#   amount of evidence variables are large.
print("Rejection Sampling: ", rejection_sampling('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary, 10000).show_approx())

# Likelihood weighting fixes evidence variables and only varies nonevidence variables in the samples. This makes it
#   similar to rejection sampling but it will only produce samples that are consistent with the evidence. It varies from
#   exact inference because it is estimating samples when exact does not estimate.
print("Likelihood Weighting: ", likelihood_weighting('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary, 10000).show_approx())

# Gibbs ask does not match with exact inference because it generates random samples. Gibbs ask is a type of MCMC
#   that starts at a random state, and then flips a random variable while keeping the evidence variables fixed.
print("Gibbs Ask: ", gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())



