DATA PREPARATION
1) See data_preparation/queries_to_get_data.txt to get data. Unpack them in data/cancer/ and data/normal/ folders.
2) Run bash script data_preparation/unpack in data/cancer/ and data/normal/ folders folders to unpack all data.
3) Run data_preparation/make_input4R.py to make input file for R (data/input4R.csv).
4) Run data_preparation/rename_files.py to prepare filenames for R analysis.

DATA ANALYSIS
1) PCA in data_analysis/PCA
2) To decrease number of features allpy DESeq: data_analysis/DESeq
