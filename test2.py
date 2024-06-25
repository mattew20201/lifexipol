import os 
import subprocess

cmd = 'ls'
result = subprocess.run(cmd,capture_output=True,text=True)
print(result.stdout)