import pandas as pd
from sklearn.metrics import roc_curve, auc
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
import numpy as np

def auc_value(y_test, y_predict):
    fpr, tpr, _ = roc_curve(y_test, y_predict)
    return auc(fpr, tpr)

def predictions(X_train, y_train, X_test, y_test):
    predictions = list()
    #columns = ['penalized SVM', 'logistic regression', 'XGBoost', 'LDA', 'random forest']
    # penalized_svm
    penalized_svm = SVC(kernel='linear', class_weight='balanced', probability=True)
    penalized_svm.fit(X_train, y_train)
    y_scores = penalized_svm.decision_function(X_test)
    predictions.append(auc_value(y_test, y_scores))
    #print(y_scores)
    #print('penalized SVM: ' + str(auc_value(y_test, y_scores)))

    # logistic regression
    log_regr = LogisticRegression(penalty='l1', solver='liblinear')
    log_regr.fit(X_train, y_train)
    y_predict = log_regr.predict(X_test)
    predictions.append(auc_value(y_test, y_predict))
    # print('logistic regression: ' + str(auc_value(y_test, y_predict)))
    #print(log.predict(X_test))

    # XGBoost
    xgboost = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.05)
    xgboost.fit(X_train, y_train)
    y_scores = xgboost.predict(X_test)
    predictions.append(auc_value(y_test, y_scores))

    # LDA
    lda = LinearDiscriminantAnalysis()
    lda.fit(X_train, y_train)
    LinearDiscriminantAnalysis(n_components=None, priors=None, shrinkage=None,
                               solver='svd', store_covariance=False, tol=0.0001)
    y_predict = lda.predict(X_test)
    predictions.append(auc_value(y_test, y_predict))

    # random forest
    rf = RandomForestClassifier(bootstrap=False, class_weight=None, criterion='gini',
                                 max_depth=70, max_features='sqrt', max_leaf_nodes=None,
                                 min_impurity_decrease=0.0, min_impurity_split=None,
                                 min_samples_leaf=10, min_samples_split=20,
                                 min_weight_fraction_leaf=0.0, n_estimators=800, n_jobs=1,
                                 oob_score=False, random_state=5, verbose=0, warm_start=False)
    rf.fit(X_train, y_train)
    y_predict = rf.predict_proba(X_test)
    predictions.append(auc_value(y_test, y_predict[:, 1]))

    return predictions

df_normal = pd.read_csv('../../data/input_genes4P_normal_padj_less_0.01_threshold_4.csv')
df_cancer = pd.read_csv('../../data/input_genes4P_cancer_padj_less_0.01_threshold_4.csv')

df_normal = df_normal.sample(frac=1).reset_index(drop=True)
df_cancer = df_cancer.sample(frac=1).reset_index(drop=True)
#print(df_normal['ENSG00000029559.6'])
data = list()
for i in range(4):
    print(str(i)+')')
    df_test_normal = df_normal[8*i:8*i+8]
    #print(df_test_normal['ENSG00000029559.6'])
    df_train_normal = df_normal
    for k in range(8*i,8*i+8):
        df_train_normal = df_train_normal.drop(k)
    #print(df_train_normal['ENSG00000029559.6'])

    for j in range(46):
        df_test_cancer = df_cancer[8*i:8*i+8]
        df_train_cancer = df_cancer
        for w in range(8*i,8*i+8):
            df_train_cancer = df_train_cancer.drop(w)
        df_train = df_train_normal.append(df_train_cancer)
        df_test = df_test_normal.append(df_test_cancer)

        y_train = df_train.Class
        X_train = df_train.drop('Class', axis=1)
        y_test = df_test.Class
        X_test = df_test.drop('Class', axis=1)
        data.append(predictions(X_train, y_train, X_test, y_test))
columns = ['penalized SVM', 'logistic regression', 'XGBoost', 'LDA', 'random forest']
df = pd.DataFrame(data, columns = columns)
print(df.mean())
#print(predictions(X_train, y_train, X_test, y_test))


# clf = RandomForestClassifier(max_depth=2, random_state=5)
#
# # Number of trees in random forest
# n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
# # Number of features to consider at every split
# max_features = ['auto', 'sqrt']
# # Maximum number of levels in tree
# max_depth = [int(x) for x in np.linspace(10, 100, num=10)]
# max_depth.append(None)
# # Minimum number of samples required to split a node
# min_samples_split = [20, 50, 100]
# # Minimum number of samples required at each leaf node
# min_samples_leaf = [10, 20, 40]
# # Method of selecting samples for training each tree
# bootstrap = [True, False]
#
# random_grid = {'n_estimators': n_estimators,
#                'max_features': max_features,
#                'max_depth': max_depth,
#                'min_samples_split': min_samples_split,
#                'min_samples_leaf': min_samples_leaf,
#                'bootstrap': bootstrap}
#
# rs = RandomizedSearchCV(estimator=clf, param_distributions=random_grid, n_iter=100, verbose=2, random_state=5, n_jobs=2)
# rs.fit(X_train, y_train)
# best_model = rs.best_estimator_
# print('Best model:')
# print(best_model)