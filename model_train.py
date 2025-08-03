import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Load dataset
df = pd.read_csv("WineQT.csv")

# Drop the ID column
df.drop(columns=['Id'], inplace=True)

# Convert quality to binary: Good (1) if quality ≥ 7
df['quality'] = df['quality'].apply(lambda q: 1 if q >= 7 else 0)

# Split into features and labels
X = df.drop('quality', axis=1)
y = df['quality']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train KNN model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Save model and meta info
joblib.dump(model, 'model.pkl')
joblib.dump(['Bad Quality', 'Good Quality'], 'target_names.pkl')
joblib.dump(list(X.columns), 'feature_columns.pkl')
