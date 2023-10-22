def movie_organizer(*args):
    movies = {}
    result = []
    for info in args:
        movie_name, type_movie = info[0], info[1]
        if type_movie not in movies:
            movies[type_movie] = []

        movies[type_movie].append(movie_name)

    sorted_movies = dict(sorted(movies.items(), key=lambda x: (-len(x[1]), x[0])))

    for type_movie, movie_names in sorted_movies.items():
        result.append(f"{type_movie} - {len(movie_names)}")
        [result.append(f"* {movie}") for movie in sorted(movie_names)]

    return '\n'.join(result)


print(movie_organizer(

("The Godfather", "Drama"),

("The Hangover", "Comedy"),

("The Shawshank Redemption",


"Drama"),

("The Pursuit of Happiness",

"Drama"),

("The Hangover Part II", "Comedy")))