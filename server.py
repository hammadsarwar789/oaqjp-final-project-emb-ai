from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """
    Serve the main page of the NLP Emotion Detection app.
    
    Returns:
        Rendered HTML template for the home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_endpoint():
    """
    Endpoint to process emotion detection requests.
    
    Extracts the text to analyze from query parameters,
    calls the emotion_detector function, and formats the response.
    
    Returns:
        str: Formatted string with emotion scores and dominant emotion,
             or error message for invalid input.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    results = emotion_detector(text_to_analyze)

    if results["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {results['anger']}, 'disgust': {results['disgust']}, "
        f"'fear': {results['fear']}, 'joy': {results['joy']} and "
        f"'sadness': {results['sadness']}. The dominant emotion is "
        f"{results['dominant_emotion']}."
    )
    return response


if __name__ == "__main__":
    app.run(debug=True)
