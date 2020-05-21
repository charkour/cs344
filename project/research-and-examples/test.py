"""Little script to quickly assess the performance of the DQN agent.
This is not very efficient but it does what it needs to.
The runtime is O(n^3)

NOTE: If you are just wanting to test, comment out
the training line in cechine-example.py. Line 97: dqn.fit()
"""

import subprocess
out = subprocess.check_output(['python3', 'ceshine-example.py'])
decoded = out.decode('utf-8')
print(decoded)
completed = str(decoded.count('reward: 1.'))
total = str(decoded.count('reward: '))
print(completed + "/" + total)
