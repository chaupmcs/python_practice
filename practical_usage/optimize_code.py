import cProfile, pstats, io
from collections import Counter
from algorithm.leetcode.next_permutation import Solution
def profile(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner


def read_movies(src):
    with open(src) as fd:
        return fd.read().splitlines()


@profile
def find_duplicate_movies(src='../data/input/movies.txt'):
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    movies.sort()
    duplicates = [movie1 for movie1, movie2 in zip(movies[:-1], movies[1:]) if movie1 == movie2]
    return duplicates

@profile
def find_duplicate_movies_2(src='../data/input/movies.txt'):
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    count = Counter(movies)
    duplicates = []
    for k, v in count.items():
        if v > 1:
            duplicates.append(k)

    return duplicates

find_duplicate_movies()
find_duplicate_movies_2()

