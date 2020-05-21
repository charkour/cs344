# A Dive into Reinforcement Learning: Artificial Intelligence Project Proposal

By Charles Kornoelje
for CS 344 at Calvin University

Updated: 05/21/20

## Overview and Vision
The goal of my CS 344 honors final project is to take a deep dive into [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning), with the hope of training an artificial intelligence agent to play a video game. The first agent I was able to implement was with a [deep Q-learning network](https://en.wikipedia.org/wiki/Q-learning#Deep_Q-learning) (DQN) designed to play the Atari 2600 game, _[Breakout](https://w.wiki/RQQ)_, the classic brick-breaking game. However, I quickly learned that training a somewhat intelligent agent would take lots of computational time and energy, which I did not have, so I began training an agent and moved on to find a game that took less power, which led me to the text-based video game, _[FrozenLake](https://gym.openai.com/envs/FrozenLake-v0/)_. I was able to train a smart agent to play the game after following a guide and tweaking some code.

The purpose of this project is to learn how to use reinforcement learning to train agents. Reinforcement learning is a domain of machine learning where an agent takes actions based on observations in their environment to maximize their reward. The project falls under the active reinforcement learning realm in which a [Q-learning](https://en.wikipedia.org/wiki/Q-learning) agent is trained with an action-utility function (Q-function) to learn a control policy that tells an agent which actions to take at a current state. Learning the control policy will assist the agent in decision making in order to take proper actions to maximize their score in video games. If an agent is able to be trained to play a game well, the same training can be applied to real life activities and techniques.



## Code Modules
* report.ipynb: Here is the writeup for the for the project, with a 
detailed explanation of the work. There are code cells that help you run the code but
I suggest you run the code from the files
* updates.ipynb: These are all of the changes I have made since the meeting on 05/15/20
* proposal.ipynpb: The old proposal. This is outdated.
* research-and-examples: This directory has code for the project and code I found and built off of during 
my project.
    * boyuan-dqn-example.py: I extended this code to be a DNQ (with less memory) to play _Breakout_
    * ceshine-example.py: I extended this code to be a DQN and DDQN agent to play the 8x8 version of _FrozenLake_
    * test.py: A small script that helped me assess the accuracy of the _FrozenLake_ agent.
    * Note: All additional files are either images used in the report, other files I used for reserach
    or training weights from research.

## How to run the code
In order to run the code, you need to install the packages:

*   [gym](https://gym.openai.com/) 0.17.2
*   [numpy](https://numpy.org/) 1.18.1
*   [tensorflow](https://www.tensorflow.org/) 1.14.0
*   [keras](https://keras.io/) 2.3.1
*   [keras-rl](https://github.com/matthiasplappert/keras-rl) 0.4.2
*   [atari-py](https://github.com/openai/atari-py) 0.2.6
*   [skimage](https://scikit-image.org/) 0.16.2
*   [Collections](https://docs.python.org/3.6/library/collections.html#collections.deque) from Python 3.6

I suggest using a Python Virtual Environment to install the pages. 
From there, I used the Python IDE PyCharm to run my code.
I would suggest not to use PyCharm because it crashes often and does not play
well with Jupyter Notebooks or markdown on MacOS or Linux.
