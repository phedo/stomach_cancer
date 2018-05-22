import os

rootdir = '../data/all_data/'
res_cancer = open('../data/input4heatmap_right_cancer.csv', 'w')
res_normal = open('../data/input4heatmap_right_normal.csv', 'w')


# write header in res file
file_to_take_headers = open('../data/cancer/0a4893c6-92fc-49d1-9747-e99b7f5326a3.htseq.counts', 'r')
counter = 0
k=0
#while k<23000:
while True:
    line = file_to_take_headers.readline()
    if not line:
        break
    res_normal.write(',' + str(counter))
    counter+=1
    k+=1
res_normal.write('\n')

# write data in res file
# first, write normal tissue data, class = 1
print(rootdir)
for subdir, dirs, files in os.walk(rootdir):
    counter_cancer = 33
    counter_normal = 1
    for fl in files:
        f = open(rootdir + fl, 'r')
        if fl[:6] == 'cancer':
            res_cancer.write(str(counter_cancer))
            counter_cancer += 1
            k=0
            #while k<23000:
            while True:
                line = f.readline()[:-1].split('\t')
                if len(line) < 2:
                    break
                res_cancer.write(',' + line[1])
                k+=1
            counter += 1
            res_cancer.write('\n')
        else:
            res_normal.write(str(counter_normal))
            counter_normal += 1
            k=0
            #while k<23000:
            while True:
                line = f.readline()[:-1].split('\t')
                if len(line) < 2:
                    break
                res_normal.write(',' + line[1])
                k+=1
            counter += 1
            res_normal.write('\n')
