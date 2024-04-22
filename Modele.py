import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tpot import TPOTClassifier

# Chargement du jeu de données
data = pd.read_csv("Data/heart.csv")

# Séparation des features et de la cible
X = data.drop(columns=['target'])
y = data['target']

# Fonction pour extraire des méta-features
def extract_meta_features(X):
    meta_features = pd.DataFrame(index=X.index)  # Initialiser un DataFrame vide avec les mêmes index que X

    # Méta-features statistiques pour les colonnes numériques
    num_cols = X.select_dtypes(include=['number']).columns
    for col in num_cols:
        meta_features[f'{col}_mean'] = X[col].mean()
        meta_features[f'{col}_std'] = X[col].std()
        meta_features[f'{col}_min'] = X[col].min()
        meta_features[f'{col}_max'] = X[col].max()

    # Méta-features pour les colonnes catégorielles
    cat_cols = X.select_dtypes(include=['category', 'object']).columns
    for col in cat_cols:
        meta_features[f'{col}_nunique'] = X[col].nunique()
        # Ajouter d'autres méta-features pour les colonnes catégorielles si nécessaire

    # Ajouter des méta-features globales
    meta_features['num_rows'] = len(X)
    meta_features['num_cols'] = len(X.columns)
    # ... ajouter d'autres méta-features globales ...

    return meta_features

# Split des données en ensembles de meta-apprentissage et de test
X_meta_train, X_meta_test, y_meta_train, y_meta_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Extraction des méta-features pour l'ensemble de meta-apprentissage
meta_features_train = extract_meta_features(X_meta_train)

# Entrainement d'un modèle de meta-learning (exemple avec TPOT)
tpot = TPOTClassifier(generations=10, population_size=50, verbosity=2, random_state=42)
tpot.fit(meta_features_train, y_meta_train)

# Utiliser le meilleur pipeline de TPOT
final_model = tpot.fitted_pipeline_

# Extraction des méta-features pour l'ensemble de meta-test
meta_features_test = extract_meta_features(X_meta_test)

# Evaluation sur l'ensemble de test
y_pred = final_model.predict(meta_features_test)
accuracy = accuracy_score(y_meta_test, y_pred)
print("Accuracy:", accuracy)
