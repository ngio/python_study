# 추천 프로그램 - chatGPT
import tkinter as tk
from tkinter import messagebox

# Sample movie data
movies = {
    "Action": ["The Avengers", "Mad Max: Fury Road", "Die Hard"],
    "Comedy": ["Superbad", "The Hangover", "Anchorman"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "Pulp Fiction"]
}

class RecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation App")

        self.label = tk.Label(root, text="Select a genre:")
        self.label.pack()

        self.genre_var = tk.StringVar()
        self.genre_dropdown = tk.OptionMenu(root, self.genre_var, *movies.keys())
        self.genre_dropdown.pack()

        self.recommend_button = tk.Button(root, text="Recommend", command=self.get_recommendation)
        self.recommend_button.pack()

    def get_recommendation(self):
        selected_genre = self.genre_var.get()
        if selected_genre:
            recommended_movies = movies[selected_genre]
            messagebox.showinfo("Recommendation", f"Recommended movies in {selected_genre}:\n\n{', '.join(recommended_movies)}")
        else:
            messagebox.showwarning("Error", "Please select a genre.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecommendationApp(root)
    root.mainloop()
