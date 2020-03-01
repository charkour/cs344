'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013

@author: Charles Kornoelje cek26
@version Mar 1, 2020 for CS 344, Lab04, at Cal Uni
    Updated for Lab04 answers extra credit.
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])
T, F = True, False
P[T, T, T, T] = 0.054; P[T, T, F, T] = 0.006
P[F, T, T, T] = 0.036; P[F, T, F, T] = 0.004
P[T, F, T, T] = 0.008; P[T, F, F, T] = 0.032
P[F, F, T, T] = 0.072; P[F, F, F, T] = 0.288
P[T, T, T, F] = 0.054; P[T, T, F, F] = 0.006
P[F, T, T, F] = 0.036; P[F, T, F, F] = 0.004
P[T, F, T, F] = 0.008; P[T, F, F, F] = 0.032
P[F, F, T, F] = 0.072; P[F, F, F, F] = 0.288

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())

# i) 16
# ii) Yes, probabilities in a Join Distrubution table must add to one. An "axiom of probability".
#   There must be some probability for each combination of T/F values.
# iii) I do not think you can have something other than T/F values. If there is an "inbetween" state with an unclear
#   T/F answer, it can be broken down into a T/F answer with a RV for each "inbetween" state. The table will become quite large.
# iv) Yes, it is 50-50 if there will be rain.

# b) P(toothache|rain) = P(toothache^rain) / P(rain)
#       = (0.054 + 0.006 + 0.008 + 0.032) / (0.054 + 0.006 + 0.008 + 0.032 + 0.036 + 0.072 + 0.004 + 0.288)
#       = 0.1 / 0.5
#       = 0.2
# P(~toothache|rain) = 1 - 0.2 = 0.8
# *P*(Toothache|rain) = <0.2, 0.8>

# Compute P(Toothache|Rain=T)
PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(PC.show_approx())