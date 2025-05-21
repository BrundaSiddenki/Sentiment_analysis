from flask import Flask, render_template, request, send_file
from textblob import TextBlob
import tempfile

app = Flask(__name__)

# Analyze text sentiment
def analyze_text_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        emoji = "😊"
        state = "Positive mental state"
        advice = "Keep up the positive mindset. Practice gratitude daily!"
    elif polarity < -0.3:
        emoji = "😞"
        state = "Negative mental state"
        advice = "Try relaxation techniques and talk to someone you trust."
    else:
        emoji = "😐"
        state = "Neutral mental state"
        advice = "Maintain balance, and monitor your feelings regularly."
    return polarity, emoji, state, advice

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/classify')
def classify():
    return render_template('classify.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text_input')
    if not text or text.strip() == '':
        return "No text input provided", 400

    polarity, emoji, state, advice = analyze_text_sentiment(text)
    result = {
        'input': text,
        'polarity': f"{polarity:.2f}",
        'emoji': emoji,
        'state': state,
        'advice': advice
    }

    report_text = f"""\
Input Text: {text}
Polarity Score: {result['polarity']}
Detected Emotion: {result['emoji']} - {result['state']}
Advice: {result['advice']}"""

    tmp = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix='.txt')
    tmp.write(report_text)
    tmp.close()

    return render_template('classify.html', result=result, report_file=tmp.name)

@app.route('/download_report')
def download_report():
    path = request.args.get('path')
    if not path:
        return "No report file specified", 400
    return send_file(path, as_attachment=True, download_name='sentiment_report.txt')

if __name__ == '__main__':
    app.run(debug=True)
