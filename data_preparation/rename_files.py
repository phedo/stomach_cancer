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
