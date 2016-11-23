import itertools, os, math
from subprocess import Popen, PIPE, STDOUT

p = Popen(['./entCalculator', '-d', 'test/'], stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

outp = p.stdout.read().split('\n')[1:-2]

outp = [o.strip().replace(';', ',') for o in outp]

print outp

files = os.listdir("../Bins")

with open('SE_v1.csv', 'w') as o:
    o.write("filename, " + ','.join(files) + '\n')
    for i in range(len(files)):
        o.write(files[i] + ',' + outp[i] + '\n')
