class Movie:
    """Base class for a movie record."""
    def __init__(self, name, rating, ticket_price):
        self.name = name
        self.rating = rating          # e.g. out of 10
        self.ticket_price = ticket_price
        self.category = self.categorize()

    def categorize(self):
        """Hit / Average / Flop based on rating."""
        if self.rating >= 7:
            return "Hit"
        elif self.rating >= 4:
            return "Average"
        else:
            return "Flop"

    def display(self):
        print(f"Movie: {self.name} | Rating: {self.rating} "
              f"| Ticket Price: ₹{self.ticket_price} | Category: {self.category}")


class Cinema:
    """Manages a collection of Movie objects."""
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"Added: {movie.name}")

    def display_all_movies(self):
        if not self.movies:
            print("No movies in the collection yet.")
            return
        print("\n--- Movie Collection ---")
        for movie in self.movies:
            movie.display()
        print("-------------------------\n")


def main():
    cinema = Cinema()

    movie_data = [
        ("Interstellar", 8.6, 250),
        ("Jawan", 6.0, 300),
        ("Random Flop Movie", 3.2, 180),
    ]

    for name, rating, price in movie_data:
        movie = Movie(name, rating, price)
        cinema.add_movie(movie)

    cinema.display_all_movies()


if __name__ == "__main__":
    main()