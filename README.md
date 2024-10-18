# Email-Phishing
This project demonstrates a phishing email detection model using Logistic Regression. Below is a guide on creating both dummy datasets for testing and using an actual dataset for real-world applications.
.
1. Dummy Dataset (For Testing and Experimentation)
dummy dataset is a small, artificial dataset with known characteristics to quickly test the model.

Code to Create Dummy Data:
```python
import pandas as pd

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
        "Phishing scam detected, report it immediately."
    ],
    'label': [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]  # 1 = Phishing, 0 = Legitimate
}
df = pd.DataFrame(data)

For real-world data, you will need a more extensive dataset containing various phishing and legitimate emails. This dataset can be obtained from sources like:
Kaggle: Public datasets on phishing emails.
