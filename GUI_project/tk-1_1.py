# 추천 프로그램 3 - chatGPT
import tkinter as tk
from tkinter import messagebox

# Sample movie data
movies = {
    "Action": ["Die Hard", "Mad Max: Fury Road", "The Dark Knight"],
    "Comedy": ["The Hangover", "Superbad", "Anchorman"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"]
}

def get_recommendation():
    selected_genre = genre_var.get()
    
    if selected_genre:
        recommendations = movies.get(selected_genre, [])
        
        if recommendations:
            recommended_movies.set("\n".join(recommendations))
        else:
            recommended_movies.set("No recommendations available for this genre.")
    else:
        messagebox.showinfo("Error", "Please select a genre.")

# Create the main GUI window
root = tk.Tk()
root.title("Movie Recommendation")

# Create and place widgets
genre_label = tk.Label(root, text="Select a genre:")
genre_label.pack()

genre_var = tk.StringVar()
genre_dropdown = tk.OptionMenu(root, genre_var, *movies.keys())
genre_dropdown.pack()

recommend_button = tk.Button(root, text="Get Recommendation", command=get_recommendation)
recommend_button.pack()

recommended_movies = tk.StringVar()
recommended_movies_label = tk.Label(root, textvariable=recommended_movies)
recommended_movies_label.pack()

root.mainloop()