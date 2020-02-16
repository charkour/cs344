"""
This module implements local search on a simple sine function variant.
Uses random restarts.
Extended from abs.py by kvlinden, 6feb2013.

@author: Charles Kornoelje
@version 16feb2020
CS 344, Lab02, Calvin University

"""
import math
import time
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange


class AbsVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


def average_list(l):
    """Return average value of numeric list"""
    return sum(l) / len(l)


if __name__ == '__main__':
    MAXIMUM = 30
    hc_solutions = []
    hc_values = []
    sa_solutions = []
    sa_values = []
    for i in range(1, MAXIMUM + 1):

        # Formulate a problem with a 2D hill function and a single maximum value.
        initial = i
        time1 = time.time()
        p = AbsVariant(initial, MAXIMUM, delta=1.0)
        time2 = time.time()
        print('Initial                      x: ' + str(p.initial)
              + '\t\tvalue: ' + str(p.value(initial))
              + "\t\ttime: %0.3f seconds" % (time2 - time1)
              )

        # Solve the problem using hill-climbing.
        time1 = time.time()
        hill_solution = hill_climbing(p)
        hc_solutions.append(hill_solution)
        hill_value = p.value(hill_solution)
        hc_values.append(hill_value)
        time2 = time.time()
        print('Hill-climbing solution       x: ' + str(hill_solution)
              + '\tvalue: ' + str(hill_value)
              + "\t\ttime: %0.3f seconds" % (time2 - time1)
              )

        # Solve the problem using simulated annealing.
        time1 = time.time()
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        sa_solutions.append(annealing_solution)
        sa_value = p.value(annealing_solution)
        sa_values.append(sa_value)
        time2 = time.time()
        print('Simulated annealing solution x: ' + str(annealing_solution)
              + '\tvalue: ' + str(sa_value)
              + "\t\ttime: %0.3f seconds" % (time2 - time1)
              )
        print("="*12)

    print("Hill-climbing average       x: %0.3f" % (average_list(hc_solutions))
          + '\t\tvalue: ' + str(average_list(hc_values)))
    print("Simulated annealing average x: %0.3f" % (average_list(sa_solutions))
          + '\t\tvalue: ' + str(average_list(sa_values)))



