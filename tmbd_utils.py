import requests

API_KEY = "f4d0925fb0fbdf42dc85cbda759959e0"  # your TMDb API key

def get_movie_details(title, api_key):
    search_url = "https://api.themoviedb.org/3/search/movie"
    search_params = {
        "api_key": api_key,
        "query": title
    }

    try:
        response = requests.get(search_url, params=search_params, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data["results"]:
            movie = data["results"][0]
            plot = movie.get("overview", "Plot not available.")
            poster_path = movie.get("poster_path")

            poster_url = (
                f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "N/A"
            )
            return plot, poster_url
        else:
            return "Movie not found.", "N/A"

    except Exception as e:
        print(f"Error fetching movie details for '{title}': {e}")
        return "Error occurred while fetching details.", "N/A"
