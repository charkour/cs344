'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013

@author: Charles Kornoelje cek26
@version Mar 1, 2020 for CS 344, Lab04, at Cal Uni
    Updated for Lab04 answers.
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())

# Exercise 4.1.b
# i)
# P(cavity|catch) = P(Cavity ^ catch) / P(catch)
#       = (.108 + 0.072) / (.108 + 0.072 + 0.016 + 0.144)
#       = 0.18 / 0.34
#       = 0.529
# P(~cavity|catch) = 1 - 0.529 = 0.471
# *P*(Cavity|catch) = <0.529, 0.471>
# ii) Compute *P*(Cavity|Catch=T)
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

# NOTE: Heads = T, Tails = F
P = JointProbDist(['Coin1', 'Coin2'])
T, F = True, False
P[T, T] = P[F, T] = P[T, F] = P[F, F] = 0.5 * 0.5

# 4.1.c
# Compute P(Coin2|Coin1=T)
PC = enumerate_joint_ask('Coin2', {'Coin1': T}, P)
print(PC.show_approx())

# 4.c Yes, it confirms my answer. The probability of flipping a second coin is independent of the first coin flip.
# It is a 50% chance for heads or tails showing on the second coin.

# Using full joint will be hard to use when there are a large number of variables. Some numbers would be
# difficult to get in the real world and the table would become very large and too large to use.

