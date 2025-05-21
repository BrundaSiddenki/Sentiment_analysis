
# 🎨 MoodMosaic – Intelligent Emotion Insight Web App

MoodMosaic is an AI-powered sentiment analysis platform that intelligently understands emotions from **text**, **images**, and **videos**. With a modern, interactive UI and deep learning models behind the scenes, MoodMosaic helps users gain insight into emotional context—be it for personal reflection, product feedback, or multimedia content analysis.

---

## 🚀 Features

- 📝 **Text Sentiment Analysis** using Transformers (`distilbert-base-uncased`)
- 📸 **Image Sentiment Detection** using Facial Emotion Recognition via DeepFace
- 🎥 **Video Sentiment Classification** by extracting and analyzing keyframes with OpenCV
- 🔁 **Dual Input Comparison** to evaluate and contrast two texts
- 🖥️ **Responsive Bootstrap UI** for a classy and professional experience
- 📂 Simple **file upload system** for quick testing of images and video

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Flask** – Web Framework
- **Transformers** – NLP models from HuggingFace
- **DeepFace** – Emotion recognition from facial expressions
- **OpenCV** – Video frame capture and processing
- **Bootstrap 5** – Elegant UI layout and responsiveness

---

## 📦 Installation Instructions

> ⚠️ Make sure Python 3.10 or higher is installed.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/moodmosaic.git
cd moodmosaic
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

> If you face `tf-keras` issues:
```bash
pip install tf-keras
```

### 4. Run the Web App
```bash
python app.py
```

### 5. View the Website
Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🗂 Folder Structure

```
moodmosaic/
├── app.py
├── templates/
│   ├── splash.html
│   ├── classify.html
├── static/
│   └── style.css
├── utils/
│   └── sentiment_utils.py
├── uploads/
│   └── (temporary file storage)
├── requirements.txt
└── README.md
```

---

## 📸 UI Preview

> Screenshots coming soon!  
Sample:  
- 👋 Welcome Splash Screen (splash.html)  
- 📊 Analyze & Compare Page (classify.html)

---

## 🧠 How It Works

| Input Type | Technique Used | Output |
|------------|----------------|--------|
| Text       | BERT transformer pipeline | Positive / Negative / Neutral |
| Image      | DeepFace emotion recognition | Happy / Sad / Angry / etc. |
| Video      | Frame capture + DeepFace | Aggregated emotion result |

---

## ⚙️ Sample Usage

### Text Sentiment
> Input 1: "Today is a wonderful day!"  
> Output: **Positive**

### Image Sentiment
> Upload a selfie – system detects emotion as **Happy**.

### Video Sentiment
> Upload a short video – system detects the most common emotion as **Neutral**.

---

## 🧾 License

MIT License – free to use, modify, and distribute.

---

## ✨ Author

**Brunda Siddenki**  
For academic, competition, or career-building projects.  
Feel free to reach out for enhancements, deployments, or debugging support.

---

## 💡 Future Enhancements

- 🌐 Multilingual Support
- 📊 Emotion Statistics Dashboard
- 🔔 Real-Time Feedback System
- ☁️ Cloud Deployment (Streamlit / Render / HuggingFace Spaces)
