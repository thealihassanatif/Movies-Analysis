import pandas as pd

# Change "Netflix Movies.csv" with the file path.
dataset_file = 'Netflix Movies.csv'

def search_movie():
    # Get the name of the movie from the user
    movie_name = input("Enter the name of the movie:\nMake sure to use the exact name \nFor example Thor: Ragnarok or Our Godfather ")

    # Search for the movie in the dataset
    movie_data = df[df['title'].str.lower() == movie_name.lower()]

    # Check if the movie is found
    if movie_data.empty:
        print(f"Movie '{movie_name}' not found in the dataset.")
    else:
        # Display information about the movie
        print("\nMovie Details:")
        print(f"Title: {movie_data['title'].values[0]}")
        print(f"Country: {movie_data['country'].values[0]}")
        print(f"Release Year: {movie_data['release_year'].values[0]}")
        print(f"Added on Netflix: {movie_data['date_added'].values[0]}")
        print(f"Rating: {movie_data['rating'].values[0]}")
        print(f"Director: {movie_data['director'].values[0]}")
        print(f"Cast: {movie_data['cast'].values[0]}")
        print(f"Description: {movie_data['description'].values[0]}")

# Call the function to search for a movie
search_movie()
