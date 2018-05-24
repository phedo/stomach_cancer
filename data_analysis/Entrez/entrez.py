from Bio import Entrez
import re

def summary(term):
    Entrez.email = "nukkduko@gmail.com"
    handle = Entrez.esearch(db='gene', term=term)
    record = Entrez.read(handle)
    if len(record['IdList'])>0:
        uid = record['IdList'][0]
        handle = Entrez.esummary(db="gene", id=uid)
        record = Entrez.read(handle)
        summary = record['DocumentSummarySet']['DocumentSummary'][0]['Summary']
        return summary
    else:
        return False


input = open('../../data/4summary_threshold_1.5.xls', 'r')
output_tumor = '../../data/genes_summary_tumor_threshold_1.5.txt'
output_no_tumor = '../../data/genes_summary_no_tumor_threshold_1.5.txt'

counter_not_found_genes = 0
c = 1
with open(output_tumor, 'w') as tumor, open(output_no_tumor, 'w') as no_tumor:
    while True:
        line = input.readline().split(',')
        if not line:
            break
        gene_name = line[0]
        lfc = line[2]
        baseMean = line[1]
        lfcSE = line[3]
        gene_name_short = re.findall(r'[\w]*\.', gene_name)[0][:-1]
        print(gene_name_short)
        sry = summary(gene_name_short)
        if sry:
            key_word = re.search(r'cancer|tumor', sry)
            print(key_word)
            if key_word == None:
                print(str(c) + ')')
                no_tumor.write(str(lfc) + '\t' + str(baseMean) + '\t' + str(lfcSE) + '\t' + gene_name + '\t' + sry + '\n')
            else:
                print(c)
                tumor.write(str(lfc) + '\t' + str(baseMean)+ '\t' + str(lfcSE)  + '\t' + gene_name + '\t' + sry + '\n')
            c+=1
        else:
            counter_not_found_genes += 1
print('Genes not found:' + str(counter_not_found_genes))

