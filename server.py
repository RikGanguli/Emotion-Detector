from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    out = ", ".join([f"'{key}': {value}" for key, value in response.items() if key != 'dominant_emotion'])
    return f"For the given statement, the system response is {out}. The dominant emotion is '{response['dominant_emotion']}'."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000'''
    app.run(host="0.0.0.0", port=5000)