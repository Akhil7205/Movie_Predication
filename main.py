import json
import streamlit as st
from recommend import df, recommend_movies
from tmbd_utils import get_movie_details  # or tmdb_utils if you switched

# Load API key from config
with open("config.json", "r") as f:
    config = json.load(f)

TMDB_API_KEY = config ["TMDB_API_KEY"]

# Set Streamlit page config
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommender")

# Get movie list for dropdown
movie_list = sorted(df['title'].dropna().unique())
selected_movie = st.selectbox("🎬 Select a movie:", movie_list)

# Button to recommend
if st.button("🚀 Recommend Similar Movies"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend_movies(selected_movie)

        if recommendations is None or recommendations.empty:
            st.warning("❌ Sorry, no recommendations found.")
        else:
            st.success("✅ Top similar movies:")
            for _, row in recommendations.iterrows():
                movie_title = row['title']
                plot, poster = get_movie_details(movie_title, TMDB_API_KEY)

                with st.container():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if poster and poster != "N/A":
                            st.image(poster, width=100)
                        else:
                            st.write("🖼️ No Poster Found")
                    with col2:
                        st.markdown(f"### {movie_title}")
                        st.markdown(f"_{plot}_" if plot and plot != "N/A" else "_Plot not available_")
