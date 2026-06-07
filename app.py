import streamlit as st
import pickle
import pandas as pd
import requests
import gzip
import os

# ── API keys via st.secrets (add to .streamlit/secrets.toml) or env vars ──────
TMDB_API_KEY = st.secrets.get("TMDB_API_KEY", os.environ.get("TMDB_API_KEY", ""))

if not TMDB_API_KEY:
    st.error("TMDB API key not found. Add TMDB_API_KEY to .streamlit/secrets.toml or your environment.")
    st.stop()

# ── TMDB helpers ──────────────────
def fetch_posters(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}',
        params={'api_key': TMDB_API_KEY, 'language': 'en-US'}
    )
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"

def fetch_trailer(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={'api_key': TMDB_API_KEY, 'language': 'en-US'}
    )
    data = response.json()
    if data['results']:
        trailer_key = data['results'][0]['key']
        return f"https://www.youtube.com/watch?v={trailer_key}"
    return None

def fetch_top_rated_movies():
    response = requests.get(
        'https://api.themoviedb.org/3/movie/top_rated',
        params={'api_key': TMDB_API_KEY, 'language': 'en-US', 'page': 1}
    )
    return response.json()['results']

def fetch_trending_movies():
    response = requests.get(
        'https://api.themoviedb.org/3/trending/movie/week',
        params={'api_key': TMDB_API_KEY}
    )
    return response.json()['results']

# ── Load data ──────────────────────────────────────────────────────────────────
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# ── Sidebar filters ────────────────────────────────────────────────────────────
st.sidebar.header("Customize Your Recommendations")
selected_genre = st.sidebar.selectbox('Genre Preference', ['All', 'Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi'])
year_range = st.sidebar.slider('Release Year', min_value=1980, max_value=2023, value=(2000, 2023))

# ── UI ─────────────────────────────────────────────────────────────────────────
st.title('🎬 Movie Recommender')
st.markdown("<h3 style='font-size:24px;'>Find movies you'll love based on your favorite selections!</h3>", unsafe_allow_html=True)

selected_movie_name = st.selectbox('Search and select a movie:', options=[''] + list(movies['title'].values))

# ── Recommendation logic ───────────────────────────────────────────────────────
def recommend(movie, genre_filter='All', year_filter=(1980, 2023)):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]

        ranked = sorted(
            list(enumerate(distances)),
            key=lambda x: x[1],
            reverse=True
        )[1:50]  

        
        def passes_filter(idx):
            row = movies.iloc[idx]
            if genre_filter != 'All' and 'genres' in movies.columns:
                genres_val = str(row.get('genres', ''))
                if genre_filter.lower() not in genres_val.lower():
                    return False
            if 'release_date' in movies.columns:
                try:
                    year = int(str(row['release_date'])[:4])
                    if not (year_filter[0] <= year <= year_filter[1]):
                        return False
                except (ValueError, TypeError):
                    pass
            return True

        filtered = [(idx, score) for idx, score in ranked if passes_filter(idx)]

        # 3 most similar + 3 discovery picks
        top_similar = filtered[:3]
        discovery = filtered[5:8] if len(filtered) > 8 else filtered[3:6]
        selected = top_similar + discovery

        recommended_movies = []
        recommended_movies_posters = []

        for idx, _ in selected:
            movie_id = movies.iloc[idx].movie_id
            recommended_movies.append(movies.iloc[idx].title)
            recommended_movies_posters.append(fetch_posters(movie_id))

        return recommended_movies, recommended_movies_posters

    except IndexError:
        return [], []

if st.button('Recommend'):
    if selected_movie_name in movies['title'].values:
        names, posters = recommend(selected_movie_name, selected_genre, year_range)
        if names:
            cols = st.columns(6)
            for i, col in enumerate(cols):
                if i < len(names):
                    with col:
                        st.image(posters[i], caption=names[i], use_container_width=True)
        else:
            st.warning("No recommendations found for these filters. Try broadening your genre or year range.")
    else:
        st.error("Movie not found! Please check your input or select another movie.")

# ── Browse sections 
def display_movies(movie_list):
    cols = st.columns(5)
    for i, movie in enumerate(movie_list):
        if i % 5 == 0 and i > 0:
            cols = st.columns(5)
        with cols[i % 5]:
            poster_url = fetch_posters(movie['id'])
            trailer_link = fetch_trailer(movie['id'])
            st.image(poster_url, use_container_width=True)
            st.write(f"**{movie['title']}**")
            if trailer_link:
                st.markdown(f"[Watch Trailer]({trailer_link})")

st.subheader("🌟 Explore the Top-Rated Movies")
st.markdown("Discover critically acclaimed movies that are loved by audiences worldwide.")
top_rated_movies = fetch_top_rated_movies()
display_movies(top_rated_movies)          

st.subheader("🔥 Trending Movies This Week")
st.markdown("Catch up with the movies everyone is talking about!")
trending_movies = fetch_trending_movies()
display_movies(trending_movies)          

st.markdown(
    """
    <hr>
    <p style="text-align:center; color:grey;">
        Built using Streamlit by Charu Rajput | <a href="https://github.com/charuu2" target="_blank">GitHub</a>
    </p>
    """,
    unsafe_allow_html=True
)
