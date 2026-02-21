# 🎬 Movie Recommender System

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-red?logo=streamlit)](https://movie-recommender-ashif.streamlit.app/)

A content-based movie recommendation system built using:

- Python
- Pandas
- Scikit-learn
- Streamlit

---

## 🚀 Live App

👉 **Try it here:**  
https://movie-recommender-ashif.streamlit.app/

---

## 📌 Features

- Recommends 5–10 similar movies
- Content-based filtering (overview, cast, genres, keywords)
- Cosine similarity model
- Clean Streamlit UI
- Deployed on Streamlit Cloud

---

## 🧠 How It Works

1. Movie metadata is processed.
2. Important text features are combined.
3. Text is vectorized using `CountVectorizer`.
4. Similarity is calculated using cosine similarity.
5. Top similar movies are recommended.

---

## 🛠️ Installation (Run Locally)

Clone the repository:

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
movie-recommender/
│
├── app.py
├── main.py
├── requirements.txt
├── models/
│   ├── movies.pkl
│   └── similarity.pkl
└── data/
```

---

## 🌍 Deployment

This app is deployed using Streamlit Community Cloud.

---

## 📧 Author

almdashif