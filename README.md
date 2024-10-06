# Sentiment Analysis on User Reviews

## Overview - 
This project implements a simple Sentiment Analysis tool using Streamlit, FastAPI, and Hugging Face Transformers. The application takes user reviews as input and analyzes their sentiment to classify them as Positive, Negative, or Neutral based on a pre-trained NLP model.

## Project Structure - 
The project consists of two main components:
1) FastAPI Backend: Serves as the backend API that uses a pre-trained model from the Hugging Face library to analyze sentiment.
2) Streamlit Frontend: Provides a user-friendly interface where users can input their reviews and see the results of the sentiment analysis in real-time.

## Tools & Technologies -
- Python
- FastAPI: To build the backend API that handles the sentiment analysis.
- Streamlit: To create a simple and interactive user interface.
- Hugging Face Transformers: To load the pre-trained model for sentiment analysis.
- Uvicorn: To run the FastAPI server.
- Requests: For sending HTTP requests from the Streamlit app to the FastAPI server.

  
## Installation & Setup - 

### Prerequisites
- Make sure you have Python 3.x installed on your system.

### Clone the Repository
```
git clone https://github.com/yourusername/sentiment-analysis-project.git
cd sentiment-analysis-project
```
### Create a Virtual Environment
Create and activate a virtual environment to manage your dependencies.
```
python -m venv venv
```
### Activate the virtual environment:
- Windows
```
venv\Scripts\activate
```
- MacOS/Linux:
```
source venv/bin/activate
```
### Install Dependencies
Install all necessary libraries using pip:
```
pip install -r requirements.txt
```

### Run the FastAPI Backend
Start the FastAPI server by running:
```
uvicorn api:app --reload --port 8000
```
This will run the API server on http://localhost:8000.

### Run the Streamlit Frontend
In a new terminal window (while keeping the FastAPI server running), start the Streamlit app:
```
streamlit run app.py
```
This will open a new browser window at http://localhost:8501 where you can interact with the app.

## Project Structure - 

```
sentiment-analysis-project/
    ├── api.py               # FastAPI backend code
    ├── app.py               # Streamlit frontend code
    ├── venv/                # Virtual environment
    ├── requirements.txt     # Project dependencies
    └── README.md            # Project documentation
```

## Usage - 
1) Open the Streamlit app in your browser.
2) Enter any review or text in the provided text area.
3) Click the Analyze button.
4) The sentiment (e.g., "POSITIVE", "NEGATIVE") and confidence score will be displayed based on the analysis performed by the pre-trained model.


## Example Reviews & Output - 

FastAPI - Swagger UI

![image](https://github.com/user-attachments/assets/166776cf-9834-4d2f-859b-ed8c2f1ffca2)

1. Home Screen

![image](https://github.com/user-attachments/assets/01879cc7-f3fd-43d1-8c3f-5c33fdb529de)

2. Analyzing a Positive Review

![image](https://github.com/user-attachments/assets/8b3cecce-8128-436b-bd09-d2b6ddb278ae)\

3. Analyzing a Megative Review

![image](https://github.com/user-attachments/assets/137279b7-47f7-41cf-8f88-bcf326a32e3a)

## Improvements - 
- Adding more detailed visualizations to the Streamlit interface.
- Extending the model to handle more nuanced sentiment classifications (e.g., "Very Positive", "Neutral", "Mixed", "Somewhat Negative").

## Acknowledgements - 
- Hugging Face for providing the pre-trained NLP model.
- Streamlit and FastAPI for their easy-to-use frameworks.







  
