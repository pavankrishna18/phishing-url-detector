import joblib
import pandas as pd
from utils.feature_extractor import extract_features

# Load model
model = joblib.load("model/phishing_url_model.pkl")

def predict_url(url):
    features = extract_features(url)
    df_feat = pd.DataFrame([features])
    prediction = model.predict(df_feat)[0]
    return "Phishing" if prediction == 1 else "Legitimate"

if __name__ == '__main__':
    test_url = input("Enter a URL to check: ")
    result = predict_url(test_url)
    print("Prediction:", result)
