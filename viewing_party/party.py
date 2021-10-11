def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            'title':title,
            'genre':genre,
            'rating':rating
        }
        return movie
    else:
        return None

def add_to_watched(user_data, movie):

    user_data = {
        "watched":[]
    }

    movie = {
        'title': 'Title A',
        'genre': 'Horror',
        'rating': 3.5
    }

    user_data["watched"].append(movie)

    return user_data
    