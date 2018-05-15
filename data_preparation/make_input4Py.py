
import os

rootdir_normal = '../data/normal/'
rootdir_cancer = '../data/cancer/'
res_normal = open('../data/input_genes4P_normal_padj_less_0.01_threshold_4.csv', 'w')
res_cancer = open('../data/input_genes4P_cancer_padj_less_0.01_threshold_4.csv', 'w')

res_normal.write('Class')
res_cancer.write('Class')

genes = []
file_with_genes = open('../data/sorted_genes/all_genes_with_padj_less_0.01_threshold_4.txt', 'r')
j=0
while True:
    gene_name = file_with_genes.readline()
    j+=1
    if not gene_name:
        break
    print(str(j)+") "+gene_name[:-1])
    if gene_name[:-1] != '':
        genes.append(gene_name[:-1])
file_with_genes.close()

# write header in res file
file_to_take_headers = open('../data/cancer/0a4893c6-92fc-49d1-9747-e99b7f5326a3.htseq.counts', 'r')
while True:
    line = file_to_take_headers.readline()
    if not line:
        break
    g_name = str(line.split('\t')[0])
    if g_name in genes:
        res_normal.write(',' + g_name)
        res_cancer.write(',' + g_name)
res_normal.write('\n')
res_cancer.write('\n')
file_to_take_headers.close()

# write data in res file
# first, write normal tissue data, class = 1
print(rootdir_normal)
for subdir, dirs, files in os.walk(rootdir_normal):
    file_counter = 1
    for fl in files:
        print(str(file_counter) + ') ' + fl)
        f = open(rootdir_normal + fl, 'r')
        res_normal.write('1')
        while True:
            line = f.readline()[:-1].split('\t')
            if len(line) < 2:
                break
            g_name = line[0]
            if g_name in genes:
                res_normal.write(',' + line[1])
        file_counter += 1
        res_normal.write('\n')
res_normal.close()

print(rootdir_cancer)
# second, write cancer tissue data, class = 0
for subdir, dirs, files in os.walk(rootdir_cancer):
    file_counter = 1
    for fl in files:
        print(str(file_counter) + ') ' + fl)
        f = open(rootdir_cancer + fl, 'r')
        res_cancer.write('0')
        while True:
            line = f.readline()[:-1].split('\t')
            if len(line) < 2:
                break
            g_name = line[0]
            if g_name in genes:
                res_cancer.write(',' + line[1])
        file_counter += 1
        res_cancer.write('\n')
res_cancer.close()
