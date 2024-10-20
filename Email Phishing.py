# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import re
import string


data = {
    'email_text': [
        "Congratulations, you've won a lottery! Click here to claim your prize.",
        "Your order has been shipped. Track your delivery using this link.",
        "Please verify your account by clicking this link.",
        "Dear customer, you are entitled to receive a refund of $1000. Act now!",
        "You have received a secure message from your bank.",
        "Urgent: Update your account information to prevent service suspension.",
        "Your Amazon order is confirmed. Check your order status here.",
        "Alert: Unusual login attempt detected. Verify your identity.",
        "Your invoice for the purchased items is attached.",
        "Phishing scam detected, report it immediately.",
    ],
    'label': [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)



def clean_text(text):
    text = text.lower()  
    text = re.sub(r'\[.*?\]', '', text)  
    text = re.sub(r'\w*\d\w*', '', text)  
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  
    text = re.sub(r'<.*?>+', '', text)  
    text = text.translate(str.maketrans('', '', string.punctuation))  
    return text

df['email_text'] = df['email_text'].apply(lambda x: clean_text(x))


tfidf_vectorizer = TfidfVectorizer(max_features=3000)  
X = tfidf_vectorizer.fit_transform(df['email_text']).toarray()  
y = df['label']  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

conf_matrix = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix:\n{conf_matrix}")


class_report = classification_report(y_test, y_pred)
print(f"Classification Report:\n{class_report}")

new_email = ["You have won a free iPhone! Click here to claim your prize."]
cleaned_email = [clean_text(email) for email in new_email]  # Clean the email


email_tfidf = tfidf_vectorizer.transform(cleaned_email).toarray()

prediction = model.predict(email_tfidf)

if prediction[0] == 1:
    print("Phishing Email Detected!")
else:
    print("Legitimate Email")

