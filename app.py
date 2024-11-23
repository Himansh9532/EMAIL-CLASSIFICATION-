import streamlit as st
from joblib import load

# Load the saved model and vectorizer
model = load("bernoulli_model.joblib")
vectorizer = load("vectorizer.joblib")  # Save and load your vectorizer

# Title of the app
st.title("Spam Message Classifier")

# Subtitle
st.subheader("Enter a message to classify it as Spam or Ham")

# Input text box
user_input = st.text_area("Enter your message here:")

# Button for prediction
if st.button("Classify"):
    if user_input.strip():
        # Transform the input text and predict
        transformed_text = vectorizer.transform([user_input])
        prediction = model.predict(transformed_text)
        
        # Display the result
        result = "Spam" if prediction[0] == 1 else "Ham"
        st.success(f"The message is classified as: **{result}**")
    else:
        st.error("Please enter a valid message!")
