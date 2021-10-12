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

    user_data["watched"].append(movie)

    return user_data
    
def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for d in user_data['watchlist']:
        if d['title'] == title:
            user_data["watchlist"].remove(d)
            user_data["watched"].append(d)
    return user_data





