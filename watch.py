#!/usr/bin/python
import subprocess
from signal import SIGTERM, SIGKILL
import time
import sys
import os

def main(arr, secs_to_wait):
  pipe = subprocess.Popen(arr)
  # time to sleep in seconds.
  time.sleep(secs_to_wait)
  pipe.poll()
  if pipe.returncode == None:
    sys.stderr.write("[%s] stop\n" % pipe.pid)

    # give the monitored program a chance to flush files,
    # wait for 10 seconds.
    os.kill(pipe.pid, SIGTERM)
    time.sleep(10)
    pipe.poll()
    if pipe.returncode == None:
      sys.stderr.write("[%s] kill\n" % pipe.pid)
      os.kill(pipe.pid, SIGKILL)

main(sys.argv[1:], 3*60)

# usage:
#   ./watch.py <program> <arguments>
# time set to 3*60 seconds = 3 minues
