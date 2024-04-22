from flask import Flask, render_template, request
import googleapiclient.discovery
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = Flask(__name__, template_folder="Templates")

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# YouTube API credentials here
API_KEY = ""

def fetch_comments(video_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )
    response = request.execute()

    comments = []

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comment_text = comment['textDisplay']
        sentiment = analyze_sentiment(comment_text)
        comments.append({
            'author': comment['authorDisplayName'],
            'text': comment_text,
            'sentiment': sentiment,
        })

    return comments

def analyze_sentiment(text):
    # Analyze sentiment using the SentimentIntensityAnalyzer
    scores = sid.polarity_scores(text)
    sentiment = 'Neutral'

    if scores['compound'] > 0.05:
        sentiment = 'Positive'
    elif scores['compound'] < -0.05:
        sentiment = 'Negative'

    return sentiment

def analyze_polarity(text):
    return 'Positive'

@app.route("/", methods=["GET", "POST"])
def index():
    comments = []
    sentiment_counts = {'Positive': 0, 'Neutral': 0, 'Negative': 0}

    if request.method == "POST":
        video_url = request.form["video_url"]
        video_id = extract_video_id(video_url)
        comments = fetch_comments(video_id)

        # Count sentiment occurrences
        for comment in comments:
            sentiment_counts[comment['sentiment']] += 1

        # Create a pie chart for sentiment analysis
        labels = list(sentiment_counts.keys())
        values = list(sentiment_counts.values())

        # Update the make_subplots call to have proper row_span and col_span values
        fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'bar'}]],
                            subplot_titles=["Sentiment Distribution", "Sentiment Counts"])

        # Add traces to the subplot
        fig.add_trace(go.Pie(labels=labels, values=values, name="Sentiment Distribution"), row=1, col=1)
        fig.add_trace(go.Bar(x=labels, y=values, name="Sentiment Counts"), row=1, col=2)

        # Update layout to prevent overlapping
        fig.update_layout(title_text="Sentiment Analysis", showlegend=False)

        # Convert the plotly chart to HTML
        chart_div = fig.to_html(full_html=False)
    else:
        chart_div = None

    return render_template("index.html", comments=comments, chart_data=chart_div)


def extract_video_id(url):
    video_id = url.split("v=")[1]
    return video_id

if __name__ == "__main__":
    app.run(debug=True)
