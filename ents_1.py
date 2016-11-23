import itertools, os, math
from subprocess import Popen, PIPE, STDOUT


files = os.listdir("../Bins")

def full_path(f):
    """ f is a stirng"""
    return "..Bins/" + f

def ENT(file):
    p = Popen(['./entCalculator', '-i', full_path(file)], stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

for file in files:
    print file
    ENT(file)


