"""Little script to quickly assess the performance of the DQN agent.
This is not very efficient but it does what it needs to.
The runtime is O(n^3)
"""

import subprocess
out = subprocess.check_output(['python3', 'ceshine-example.py'])
decoded = out.decode('utf-8')
print(decoded)
completed = str(decoded.count('reward: 1.'))
total = str(decoded.count('reward: '))
print(completed + "/" + total)
