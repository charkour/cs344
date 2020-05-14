"""
@author: CeShine
@author: Charkour
Updated to work for 8x8 frozen ice.
Ability to load weights.
Fix small bugs for new versions.
Reuseability features.

Using keras-rl (https://github.com/matthiasplappert/keras-rl) to provide basic framework,
and embedding layer to make it essentially a Q-table lookup algorithm.
"""

import tempfile
import gym
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten, Dropout, Reshape
from keras.layers.embeddings import Embedding
from keras.optimizers import Adam
from keras.layers.normalization import BatchNormalization
from rl.agents.dqn import DQNAgent
from rl.policy import Policy, BoltzmannQPolicy
from rl.memory import SequentialMemory


class DecayEpsGreedyQPolicy(Policy):

    def __init__(self, max_eps=.1, min_eps=.05, lamb=0.001):
        super(DecayEpsGreedyQPolicy, self).__init__()
        self.max_eps = max_eps
        self.lambd = lamb
        self._steps = 0
        self.min_eps = min_eps

    def select_action(self, q_values):
        assert q_values.ndim == 1
        nb_actions = q_values.shape[0]
        eps = self.min_eps + (self.max_eps - self.min_eps) * \
            np.exp(-self.lambd * self._steps)
        self._steps += 1
        if self._steps % 1e3 == 0:
            print("Current eps:", eps)
        if np.random.uniform() < eps:
            action = np.random.random_integers(0, nb_actions - 1)
        else:
            action = np.argmax(q_values)
        return action


ENV_NAME = 'FrozenLake8x8-v0'

np.set_printoptions(threshold=np.inf)
np.set_printoptions(precision=4)

# Get the environment and extract the number of actions.
env = gym.make(ENV_NAME)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n

def get_keras_model(action_space_shape):
    model = Sequential()
    model.add(Embedding(64, 4, input_length=1))
    model.add(Reshape((4,)))
    print(model.summary())
    return model

model = get_keras_model(nb_actions)

memory = SequentialMemory(window_length=1, limit=10000)
policy = DecayEpsGreedyQPolicy(max_eps=0.9, min_eps=0, lamb=1 / (1e4))
dqn = DQNAgent(model=model, nb_actions=nb_actions,
               memory=memory, nb_steps_warmup=500,
               target_model_update=1e-2, policy=policy,
               enable_double_dqn=False, batch_size=512
               )
dqn.compile(Adam())


try:
    dqn.load_weights('dqn_{}_weights.h5f'.format(ENV_NAME))
except Exception as e:
    print(e)
    pass

temp_folder = tempfile.mkdtemp()
env = env.unwrapped
# env = gym.wrappers.Monitor(env, directory=temp_folder, force=True, write_upon_reset=True)
# env.monitor.start(temp_folder)

# dqn.fit(env, nb_steps=1e5, visualize=False, verbose=1, log_interval=10000)
# # dqn.fit(env, nb_steps=100, visualize=False, verbose=1, log_interval=100)
#
# # After training is done, we save the final weights.
# dqn.save_weights('dqn_{}_weights1.h5f'.format(ENV_NAME), overwrite=True)

dqn.load_weights("./dqn_FrozenLake8x8-v0_weights1.h5f")

# Finally, evaluate our algorithm for 5 episodes.
dqn.test(env, nb_episodes=20, visualize=True)
# env.monitor.close()



