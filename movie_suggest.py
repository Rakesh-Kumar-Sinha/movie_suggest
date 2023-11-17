import tkinter as tk
from tkinter import messagebox
import random

# List of movies
movies = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "Fight Club",
    # Add more movies here
]

def suggest_movie():
    suggested_movie = random.choice(movies)
    messagebox.showinfo("Movie Suggestion", f"Your movie suggestion: {suggested_movie}")

# Tkinter setup
root = tk.Tk()
root.title("Movie Suggestion")

label = tk.Label(root, text="Click below to get a movie suggestion!")
label.pack()

suggest_button = tk.Button(root, text="Get Movie Suggestion", command=suggest_movie)
suggest_button.pack()

root.mainloop()
