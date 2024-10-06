import streamlit as st      # streamlit: Python library to create simple web applications
import requests     # to make HTTP request; send a request to your FastAPI backend to get the sentiment analysis results

st.title("Sentiment Analysis on User  Reviews")

# User input text
text_input = st.text_area("Enter a review to analyze its sentiment:")       # Create a multi-line text input text box where user can type in their review to analyze

# If the 'Analze' button is clicked
if st.button("Analyze"):        # Execute when button is clicked
    # Send a POST request to your FastAPI endpoint
    response = requests.post(
        "http://127.0.0.1:8000/analyze/",
        json={"text":text_input}
    )

    # Extract the snetiment label and score from the response
    result = response.json()        # Converts the response  from the FastAPI endpoint(JSON format) into a Python dictionary
    sentiment_label = result.get("label")       # Extract the "label" field from the response JSON (Positive or Negative)
    sentiment_score = round(result.get("score") * 100,2)        # Extract the "score" field from the response JSON, which is Confidence Score between 0 and 1

    # Display the results on the Streamlit app
    st.write(f"**Sentiment:** {sentiment_label}")
    st.write(f"**Confidence Score:** {sentiment_score}%")

