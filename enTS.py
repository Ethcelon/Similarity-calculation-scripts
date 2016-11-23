import itertools, os, math

files_u = os.listdir("segs_universe/recon")
files_0 = os.listdir("segsv1/recon")
files_1 = os.listdir("segsv1/recon")
files_2 = os.listdir("segsv2/recon")

def doEnTS(files, dir):

    def full_path(f):
        return dir + '/recon/' + f

    values = [map(lambda x: float(x) , open(full_path(f)).read().split(';')) for f in files]

    ents = []

    def calculate(x, y):
        return math.sqrt(sum(map(lambda x: pow(x[0] - x[1], 2), zip(x, y))))

    for i in range(len(files)):
        ents += [[files[i]] + [calculate(values[i], y) for y in values]]

    def write_csv(ents):
        with open('EnTS_' + dir + '.csv', 'w') as o:
            o.write('FILENAME,')
            map(lambda x: o.write(x + ','), files)
            o.write('\n')

            for e in ents:
                map(lambda x: o.write(str(x) + ','), e[0:])
                o.write('\n')
    write_csv(ents)

doEnTS(files_u, 'segs_universe')
doEnTS(files_0, 'segsv0')
doEnTS(files_1, 'segsv1')
doEnTS(files_2, 'segsv2')

