from fastapi import FastAPI, Request    # FastAPi: main class to create API, Request: to handle incoming data
from transformers import pipeline       # pipeline: Hugging Face utility to use pre-trained models for task

app = FastAPI()     # to initialize FastAPI application

# Initialize the sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")     # to load a pre-trained sentiment analysis model. Analyze and return a label like (positive or negaive)

@app.post("/analyze/")      # This decorater sets up a POST endpoint at /analyze/.
async def analyze_sentiment(request: Request):      # fucntion: analyze_sentiment handles incoming request to /analyze/. It extracts the text, analyzes and return JSON response.
    #Get the JSON data from the request
    data = await request.json()
    text = data.get('text', '')

    # Perform the sentiment analysis using the model
    result = sentiment_analyzer(text)

    # Return the label and confidence score as a JSON response
    return {"label": result[0]['label'], "score": result[0]['score']}