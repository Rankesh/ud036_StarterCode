import media
import fresh_tomatoes

"""Movie Database"""

#Movie 1 - Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")
#Movie 2 - Avatar
avatar = media.Movie("Avatar",
                        "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved.",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#Movie 3 - The Lego Movie
the_lego_movie = media.Movie("The Lego Movie",
                        "An ordinary Lego minifigure who finds himself being the only one to help a resistance stop a tyrannical businessman from gluing everything in the Lego worlds into his vision of perfection.",
                        "https://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg",
                        "https://www.youtube.com/watch?v=IMvJEqQQ2pc")

# Movies Instances
movies = [toy_story, avatar, the_lego_movie]

#Generating HTML
fresh_tomatoes.open_movies_page(movies)
