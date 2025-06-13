'''
    Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_that_emotion():
    '''
        This is the handler function of the input form
        This calls the emotion detector and display output in html.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        output = "<strong>Invalid text! Please try again!<strong>"
    else:
        scores = f"""
            'anger': {result['anger']}, 
            'disgust': {result['disgust']}, 
            'fear': {result['fear']}, 
            'joy': {result['joy']}, 
            'sadness': {result['sadness']}
        """
        output = f"""
            For the given statement, the system response is {scores}<br>
            The dominant emotion is <strong>{result['dominant_emotion']}</strong>
        """
    return output

@app.route("/")
def render_index_page():
    '''
        This displays the default index.html in the browser
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
