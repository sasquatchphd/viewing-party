from collections import Counter

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


def get_watched_avg_rating(user_data):
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    average = sum(ratings) / (len(ratings)) if ratings else 0
    return(average)

def get_most_watched_genre(user_data):
    genres = Counter(g['genre'] for g in user_data['watched'])
    pop_genre = genres.most_common()
    return(pop_genre[0][0]) if pop_genre else None
    
def get_unique_watched(user_data):
    