import subprocess
proc = subprocess.Popen(['python3', 'ceshine-example.py'], stdout=subprocess.PIPE)
out = proc.communicate()[0]
print(out)
