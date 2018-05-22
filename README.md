DATA PREPARATION
1) See data_preparation/queries_to_get_data.txt to get data. Unpack them in data/cancer/ and data/normal/ folders.
2) Run bash script data_preparation/unpack in data/cancer/ and data/normal/ folders folders to unpack all data.
3) Run data_preparation/make_input4R.py to make input file for R (data/input4R.csv).
4) Run data_preparation/rename_files.py to prepare filenames for R analysis.
5) Run data_preparation/make_input4heatmap.py to prepare input for heatmap.

DATA ANALYSIS
1) PCA in data_analysis/PCA
2) To decrease number of features allpy DESeq: data_analysis/DESeq, then manually copy that genes in txt file and with data_preparation/make_input4Py.py script convert it in data/ input csv files for data prediction.
3) Draw heatmap of our data: x - genes, y - observations, color - counts. First 32 observation is normal tissue, the others - cancer.

DATA PREDICTION
1) prediction/predictions.py script divide 32 normal tissue observations by 4 parts (8 obdervations in each). One of these parts and 46 varians of cancer tissue (8 observations each) is for test, other data is for train. For all theese sets of train and test data script calculates auc for these classifiers: 'penalized SVM', 'logistic regression', 'XGBoost', 'LDA', 'random forest'. Then it takes average by all sets for each classifier.
