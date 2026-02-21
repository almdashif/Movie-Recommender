import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
<style>
.card {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    text-align: center;
    height: 150px;
    margin: 0 0 1.5rem 0;
    transition: transform 0.2s ease-in-out;
}
.card:hover {
    transform: scale(1.05);
}
.card-title {
    font-size: 16px;
    font-weight: bold;
    color: white;
}
.card-year {
    font-size: 14px;
    color: #bbbbbb;
}
</style>
""", unsafe_allow_html=True)

st.title("🎬 Movie Recommender System")

@st.cache_resource
def load_data():
    movies = pickle.load(open('models/movies.pkl','rb'))
    similarity = pickle.load(open('models/similarity.pkl','rb'))
    return movies, similarity

movies, similarity = load_data()

def recommend(movie_title):
    index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]  # 10 items

    recommendations = []

    for i in movie_list:
        m_data = movies.iloc[i[0]]
        recommendations.append({
            "title": m_data['title'],
            "year": int(m_data['year']) if pd.notna(m_data['year']) else "N/A"
        })

    return recommendations


# ---------- UI ----------
selected_movie = st.selectbox("Select a movie", movies['title'].values)

# Clear previous recommendations automatically when movie changes
if "last_selected" not in st.session_state:
    st.session_state.last_selected = selected_movie

if selected_movie != st.session_state.last_selected:
    st.session_state.pop("recommendations", None)
    st.session_state.last_selected = selected_movie

if st.button("Show Recommendations"):
    st.session_state.recommendations = recommend(selected_movie)

if "recommendations" in st.session_state:

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for idx, movie in enumerate(st.session_state.recommendations):
        col = cols[idx % 5]
        with col:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">{movie['title']}</div>
                <div class="card-year">Year: {movie['year']}</div>
            </div>
            """, unsafe_allow_html=True)