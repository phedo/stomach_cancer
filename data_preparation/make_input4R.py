import os

rootdir_normal = '../data/normal/'
rootdir_cancer = '../data/cancer/'
res = open('../data/input4R.csv', 'w')

res.write('Class')

# write header in res file
file_to_take_headers = open('../data/cancer/0a4893c6-92fc-49d1-9747-e99b7f5326a3.htseq.counts', 'r')
while True:
    line = file_to_take_headers.readline()
    if not line:
        break
    res.write(',' + str(line.split('\t')[0]))
res.write('\n')

# write data in res file
# first, write normal tissue data, class = 1
print(rootdir_normal)
for subdir, dirs, files in os.walk(rootdir_normal):
    counter = 1
    for fl in files:
        print(str(counter) + ') ' + fl)
        f = open(rootdir_normal + fl, 'r')
        res.write('1')
        while True:
            line = f.readline()[:-1].split('\t')
            if len(line) < 2:
                break
            res.write(',' + line[1])
        counter += 1
        res.write('\n')

print(rootdir_cancer)
# second, write cancer tissue data, class = 0
for subdir, dirs, files in os.walk(rootdir_cancer):
    counter = 1
    for fl in files:
        print(str(counter) + ') ' + fl)
        f = open(rootdir_cancer + fl, 'r')
        res.write('0')
        while True:
            line = f.readline()[:-1].split('\t')
            if len(line) < 2:
                break
            res.write(',' + line[1])
        counter += 1
        res.write('\n')
