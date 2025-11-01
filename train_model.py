import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
from utils.feature_extractor import extract_features

# Load raw URL dataset
df = pd.read_csv("data/phishing_url_dataset.csv")

# Extract features from URLs
feature_rows = []
for url in df['url']:
    feature_rows.append(extract_features(url))
X = pd.DataFrame(feature_rows)

# Encode labels: phishing → 1, legitimate → 0
y = df['label'].apply(lambda x: 1 if x.lower() == 'phishing' else 0)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/phishing_url_model.pkl")
print("Model saved to model/phishing_url_model.pkl")