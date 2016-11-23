import itertools, os, math
from subprocess import Popen, PIPE, STDOUT

from tabulate import tabulate

files_var1 = os.listdir("Bins/var1/")
files_var2 = os.listdir("Bins/var2/")

files_orig = os.listdir("Bins")[:-2]

def full_path(f,dir=''):
    """ f is a stirng"""
    return "Bins/" + dir + f

def NCD(file1, file2):
    p = Popen(['./NCD.sh', full_path(file1), full_path(file2), '>> logging'], stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

    return p.stdout.read().split('\n')[-2]

def CR(file):
    p = Popen(['./CR.sh', full_path(file)], stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

    return p.stdout.read().split('\n')[-2]

def CR_similarity(x, y):
    return math.sqrt( abs( pow(float(x),2) - pow(float(y),2) ) )

crs = []

cr2 = {}
for f in files:
    cr2[f] = CR(f)

for f in files:
    crs.append([f] + [CR_similarity(cr2[f], cr2[x]) for x in files])

#print crs


# THIS IS FOR COMPARING (orig, v1) (orgi, v1) (v1, v2) - MODIFY ACCORDINGLY

ncds = []

for i in range(len(files_orig)):
    ncds.append([files_orig[i], files_var1[i]] + [NCD(files_orig[i], 'var1/' + files_var1[i])])

for i in range(len(files_orig)):
    ncds.append([files_orig[i], files_var2[i]] + [NCD(files_orig[i], 'var2/' + files_var2[i])])

for i in range(len(files_orig)):
    ncds.append([files_var1[i], files_var2[i]] + [NCD('var1/'+files_var1[i], 'var2/' + files_var2[i])])


with open('ncd_compare.csv', 'w') as o:
    o.write( "file1, file2, NCD" + '\n')
    for n in ncds:
        o.write(','.join(n) + '\n')

with open('cr_v3.csv', 'w') as o:
    o.write("filename, " + ','.join(files) + '\n')
    for c in crs:
        o.write(','.join([str(x) for x in c]) + '\n')

