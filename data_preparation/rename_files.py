import os
import shutil

input_rootdir_normal = '../data/normal/'
input_rootdir_cancer = '../data/cancer/'
output_rootdir = '../data/all_data/'

if not os.path.exists(output_rootdir):
    os.makedirs(output_rootdir)

for subdir, dirs, files in os.walk(input_rootdir_normal):
    for filename in files:
        new_filename = filename
        new_filename.replace('-', '_')
        shutil.copy(input_rootdir_normal + filename, output_rootdir + 'normal_' + new_filename)

for subdir, dirs, files in os.walk(input_rootdir_cancer):
    for filename in files:
        new_filename = filename
        new_filename.replace('-', '_')
        shutil.copy(input_rootdir_cancer + filename, output_rootdir + 'cancer_' + new_filename)

# to remove some non-gene lines from files
for subrirs, dirs, files in os.walk(output_rootdir):
    for file in files:
        f = open(output_rootdir + file, 'r')
        lines = f.readlines()
        f.close()

        w = open(output_rootdir + file, 'w')
        w.writelines([item for item in lines[:-5]])
        w.close()
