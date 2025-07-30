 link to the website : https://moivere.streamlit.app/

# 🎬 Movie Recommender System

A content-based movie recommender system built with Python and Streamlit. Select a movie you like, and the system will suggest 5 similar movies based on their plot, genre, and other features.

## 🌟 Features

- **Interactive UI:** A simple and clean user interface built with Streamlit.
- **Content-Based Filtering:** Recommends movies by analyzing and comparing their textual content (like plot summaries, genres, and keywords).
- **Dynamic Poster Fetching:** Fetches movie posters in real-time from The Movie Database (TMDb) API.
- **Large Movie Dataset:** Utilizes a dataset of thousands of movies.

## 📸 Screenshot

<img width="1909" height="926" alt="image" src="https://github.com/user-attachments/assets/02c9bf96-7ec9-4ba4-ac58-24fd25a415dd" />


## 🛠️ How It Works

The recommendation engine is based on **content-based filtering**.

1.  **Data Preprocessing:** Key features (overview, genres, keywords, cast, crew) for each movie are combined into a single text string or "tag".
2.  **Vectorization:** The text tags for all movies are converted into numerical vectors using the **TF-IDF (Term Frequency-Inverse Document Frequency)** technique. This process creates a vector space where each movie is represented by a point.
3.  **Similarity Calculation:** The **Cosine Similarity** is calculated between the vector of the user's chosen movie and all other movies in the dataset. A higher cosine similarity score means the movies are more alike in content.
4.  **Recommendation:** The system sorts the movies by their similarity score and returns the top 5 most similar movies.

## 🚀 Tech Stack

- **Python:** Core programming language.
- **Pandas:** For data manipulation and handling.
- **Scikit-learn:** For calculating cosine similarity and using TF-IDF.
- **Streamlit:** To create the interactive web application UI.
- **Requests:** For making API calls to TMDb.
- **Git LFS:** For handling the large `similarity.pkl` model file.

## ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/cyberdragon55k/movie_recommender_system.git](https://github.com/cyberdragon55k/movie_recommender_system.git)
    cd movie_recommender_system
    ```

2.  **Install Git LFS:**
    This project uses Git LFS for large file storage. You need to install it to pull the `similarity.pkl` file correctly.
    ```bash
    git lfs install
    git lfs pull
    ```

3.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4.  **Install Dependencies:**
    All required libraries are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Streamlit App:**
    ```bash
    streamlit run app.py
    ```
    The application will open in your web browser.

## 📂 File Structure



.
├── app.py                  # The main Streamlit application script
├── movie_dict.pkl          # Serialized pandas DataFrame with movie data
├── similarity.pkl          # Serialized cosine similarity matrix (handled by Git LFS)
├── requirements.txt        # List of Python dependencies
└── README.md               # You are here!


## 📊 Data Source

This project uses the [TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). Movie posters are fetched from the [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api).

---
*Created by Aditya *
