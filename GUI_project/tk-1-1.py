# 추천 프로그램 2 - chatGPT
import tkinter as tk
from tkinter import messagebox
import random

# List of movies
movies = [
    "Movie 1",
    "Movie 2",
    "Movie 3",
    "Movie 4",
    "Movie 5",
]

def recommend_movie():
    recommended_movie = random.choice(movies)
    messagebox.showinfo("Recommended Movie", f"Recommended Movie: {recommended_movie}")

# Create the main window
root = tk.Tk()
root.title("Movie Recommendation")

# Create and place widgets
label = tk.Label(root, text="Click the button to get a movie recommendation!")
label.pack(pady=10)

recommend_button = tk.Button(root, text="Recommend Movie", command=recommend_movie)
recommend_button.pack()

# Start the GUI event loop
root.mainloop()