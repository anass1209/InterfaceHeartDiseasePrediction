import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score
from xgboost import XGBClassifier
import joblib
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv("Data/heart.csv")

# Limitation des valeurs de certaines colonnes
data.trestbps.loc[data.trestbps > 170] = 170
data.chol.loc[data.chol > 360] = 360
limite_inferieur = ( data.thalach.quantile(0.25)) -1.5 * (data.thalach.quantile(0.75)-data.thalach.quantile(0.25))
data.thalach.loc[data.thalach < limite_inferieur] = limite_inferieur

def learn(dataset, algorithme, opt=2):
    X = dataset.drop('target', axis=1)
    y = dataset['target']

    # train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.31, random_state=42)

    # Standardization of numerical features with StandardScaler;
    # Models Not Based on Decision Trees benefit most from this type of standardization.
    scaler = StandardScaler()

    columns_scaler = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

    X_train[columns_scaler] = scaler.fit_transform(X_train[columns_scaler])
    X_test[columns_scaler] = scaler.transform(X_test[columns_scaler])

    if opt == 0:
        ml = algorithme(max_iter=1000)
    elif opt == 1:
        ml = algorithme(n_estimators=1000)
    elif opt == 2:
        ml = algorithme()

    # training
    train_sizes, train_scores, valid_scores = learning_curve(ml, X_train, y_train, train_sizes=np.linspace(0.1, 1.0, 10), cv=5)

    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, np.mean(train_scores, axis=1), label='Training score')
    plt.plot(train_sizes, np.mean(valid_scores, axis=1), label='Cross validation score')
    plt.xlabel('Training examples')
    plt.ylabel('Score')
    plt.title('Learning Curve')
    plt.legend()
    plt.grid()

    plt.show()

    ml.fit(X_train, y_train)
    print('Accuracy:')
    score_train = ml.score(X_train, y_train)
    print('     Train = {:.4}'.format(score_train * 100) + '%')

    score_test = ml.score(X_test, y_test)
    print('     Test = {:.4}'.format(score_test * 100) + '%')

    # predict
    y_predict = ml.predict(X_test)
    print('\nClassification Report:\n', classification_report(y_test, y_predict))
    print('Confusion Matrix:')
    confusion = confusion_matrix(y_test, y_predict)
    sns.heatmap(confusion, annot=True, cmap='Blues')

    # Precision, recall, F1-score
    precision = precision_score(y_test, y_predict)
    recall = recall_score(y_test, y_predict)
    f1 = f1_score(y_test, y_predict)

    print(f'\nPrecision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1-score: {f1}')

    return ml


# Entraîner le modèle
xgb_model = learn(data, XGBClassifier)
joblib.dump(xgb_model, 'heart_Disease_model.pkl')

