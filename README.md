### YouTube Comment Sentiment Analysis

Welcome to the YouTube Comment Sentiment Analysis repository! This project aims to analyze the sentiment of YouTube comments using Natural Language Processing (NLP) and the `SentimentIntensityAnalyzer` from the `nltk` library. The project includes both backend code for sentiment analysis and a simple frontend interface using HTML and CSS.

## Table of Contents

1. Project Overview
2. Technologies Used
3. Usage
4. Project Structure

## Project Overview

The primary goal of this project is to analyze YouTube comments and determine their sentiment (positive, negative, or neutral). The project uses Python with the `nltk` library for sentiment analysis and a simple HTML/CSS frontend for user interaction. Users can input comments manually or read comments from a file, and the sentiment analysis is displayed on the frontend.

Technologies Used

- Backend:
  - Python
  - `nltk` (Sentiment Analysis)
- Frontend:
  - HTML
  - CSS
  - JavaScript


1. Install Dependencies:
   Ensure Python is installed on your system. Install the required Python packages:
   
   pip install nltk
   

2. Download NLTK Data:
   The `SentimentIntensityAnalyzer` requires specific NLTK data. Download it using Python:
  
   python -c "import nltk; nltk.download('vader_lexicon')"


## Usage

To run the sentiment analysis, follow these steps:

1. **Run the Backend**:
   Start the backend script that analyzes the sentiment of the input comments.

   python sentiment_analysis.py


2. **Open the Frontend**:
   Open the `index.html` file in a web browser to interact with the frontend. You can input comments and view the sentiment analysis results.

## Project Structure

- **Backend**:
  - `sentiment_analysis.py`: Python script for sentiment analysis.
- **Frontend**:
  - `index.html`: Main HTML file for the frontend.
  - `style.css`: CSS for styling the frontend.
  - `script.js`: JavaScript for handling frontend interactions.

