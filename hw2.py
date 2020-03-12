'''
This module implements the Bayesian network shown in the text, Figure 14.12a.

'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.12a - rain/wet grass example
cloudy = BayesNet([
    ('Cloudy', '', 0.50),
    ('Sprinkler', 'Cloudy', {T: 0.10, F: 0.50}),
    ('Rain', 'Cloudy', {T: 0.80, F: 0.20}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.90, (F, T): 0.90, (F, F): 0.00}),
])

# # Compute P(Burglary | John and Mary both call).
# print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# # elimination_ask() is a dynamic programming version of enumeration_ask().
# print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# # gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
# print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# # See the explanation of the algorithms in AIMA Section 14.4.

# P(Cloudy)
print(enumeration_ask('Cloudy', dict(), cloudy).show_approx())

# P(Sprinkler | cloudy)
print(enumeration_ask('Sprinkler', dict(Cloudy=T), cloudy).show_approx())

# P(Cloudy| the sprinkler is running and it’s not raining)
print(enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), cloudy).show_approx())

# P(WetGrass | it’s cloudy, the sprinkler is running and it’s raining)
print(enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), cloudy).show_approx())

# P(Cloudy | the grass is not wet)
print(enumeration_ask('Cloudy', dict(WetGrass=F), cloudy).show_approx())


