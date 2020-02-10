"""

This module implements the happy, (not) hungry, healthy problem using PAIP GPS.

@author: kvlinden
@version 25jan2013

@author: Charles Kornoelje
@version 9feb2020
"""
from gps import gps
import logging

'''
This is the introvert runner problem.
The goal is to be at home as an introvert (happy)
  and to get in a run (healthy)
  and to get food (not hungry).
When running to the store, the runner gets healthy but also hungry and not happy.
At the store, eating food makes the runner not hungry.
And after the walk back home, the runner becomes happy.
'''

'''
The GPS is unable to solve the problem when the goals are ordered 'happy', 'not hungry', 'healthy'
but it is able to solve the problem when the goals are ordered 'healthy', 'happy', 'not hungry'.
'''

# Happy, (Not) Hungry, Healthy actions
actions = [
    {
        'action': 'run to store',
        'preconds': [
            'not hungry',
            'happy',
        ],
        'add': [
            'healthy',
            'hungry',
            'not happy'
        ],
        'delete': [
            'not healthy',
            'not hungry',
            'happy'
        ]
    },
    {
        'action': 'eat a snack',
        'preconds': [
            'hungry',
        ],
        'add': [
            'not hungry'
        ],
        'delete': [
            'hungry',
        ]
    },
    {
        'action': 'walk home',
        'preconds': [
            'not happy'
        ],
        'add': [
            'happy',
        ],
        'delete': [
            'not happy'
        ]
    },
]

# Formulate the problem states and actions.
problemA = {

    'initial': ['happy', 'not hungry', 'not healthy'],
    'goal': ['happy', 'not hungry', 'healthy'],
    # 'goal': ['healthy', 'happy', 'not hungry', ],
    'actions': actions
}


def printSequnce():
    """
    Print the solution, if there is one.
    """
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')


if __name__ == '__main__':
    # This turns on detailed logging for the GPS "thought" process.
    logging.basicConfig(level=logging.DEBUG)

    # Use GPS to solve the problem formulated above.
    actionSequence = gps(
        problemA['initial'],
        problemA['goal'],
        problemA['actions']
    )

    printSequnce()
