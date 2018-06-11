"""Defines the Movie class that contains the details of a movie."""
import webbrowser

class Movie:
    """Initialises Movie class instance variables."""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, rotten_tomatoes_score, certified_fresh, movie_director, movie_storyline, poster_image, movie_trailer):
        self.title = movie_title
        self.rotten_tomatoes = rotten_tomatoes_score
        self.fresh = certified_fresh
        self.director = movie_director
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.youtube_trailer_url = movie_trailer

    def show_trailer(self):
        """Plays the movie trailer in the web browser."""
        webbrowser.open(self.youtube_trailer_url)