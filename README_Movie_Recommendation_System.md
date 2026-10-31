# Movie Recommendation System

A content-based movie recommendation application built with Python and Streamlit. Select a movie from the dropdown, and the application recommends five movies with the highest content-similarity scores.

The recommendation workflow is developed in a Jupyter Notebook and presented through a simple Streamlit web app.

## Tech Stack

- Python — core programming language
- Pandas — loading, merging, and processing movie data
- NLTK — text preprocessing with stemming
- Scikit-learn — text vectorization and cosine similarity
- Joblib — loading the saved similarity matrix
- Pickle — loading the processed movie data
- Streamlit — interactive web application
- Jupyter Notebook — data preparation and recommendation workflow

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
```

**Windows:**
```bash
venv\\Scripts\\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install streamlit pandas nltk scikit-learn joblib jupyter
```

### 4. Prepare the recommendation files

The Streamlit application expects these two files in its working directory:

- `movies.pickle` — processed movie data containing the movie titles
- `similarity.joblib` — precomputed movie-to-movie similarity scores

The notebook uses the following input datasets:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

Run `movies.ipynb` from top to bottom to perform the data preparation and content-based recommendation workflow. Ensure the notebook's saved artifacts are named `movies.pickle` and `similarity.joblib` and are placed beside `app.py`.

> The uploaded application code loads these two saved artifacts; it does not create them when the Streamlit app starts.

### 5. Run the Streamlit application

Make sure `app.py`, `movies.pickle`, and `similarity.joblib` are in the same folder, then run:

```bash
python -m streamlit run app.py
```

### 6. Open the application

Streamlit will display a local URL in the terminal, usually:

```text
http://localhost:8501
```

## How It Works

1. **Load the datasets** — the notebook reads the TMDB movies and credits CSV files.
2. **Combine movie information** — movie details and credits are merged using the `title` column.
3. **Select useful information** — fields such as overview, genres, keywords, cast, and crew are prepared for recommendation.
4. **Clean and transform text** — structured genre, keyword, cast, and crew values are extracted; text is normalized and processed.
5. **Build movie tags** — relevant text information is combined into a single tag representation for each movie.
6. **Stem words** — NLTK's Porter Stemmer reduces related word forms to their stems.
7. **Convert text into vectors** — Scikit-learn's `CountVectorizer` converts movie tags into numerical word-count vectors.
8. **Measure similarity** — cosine similarity calculates how similar the movie vectors are to one another.
9. **Recommend movies** — the Streamlit app finds the selected movie's similarity row, sorts the scores, skips the selected movie itself, and displays the top five matches.

## Application Features

- Choose a movie from a dropdown list.
- Generate recommendations by clicking the **Recommend** button.
- Display five movies ranked by their similarity to the selected movie.
- Use precomputed similarity scores so the app does not need to calculate the full similarity matrix on every interaction.

## Recommendation Logic

The application uses a content-based filtering approach.

It compares movies using information represented in their processed tags. When a user selects a movie:

- The app finds that movie's row in the processed movie dataset.
- It retrieves the corresponding row from the similarity matrix.
- It sorts the movie indexes by similarity score in descending order.
- It skips the first result (the selected movie itself).
- It displays the next five movie titles.

## Project Structure

```text
movie-recommendation-system/
│
├── movies.ipynb                 # Data preparation and recommendation workflow
├── app.py                       # Streamlit application
├── tmdb_5000_movies.csv         # Movie metadata input dataset
├── tmdb_5000_credits.csv        # Cast and crew input dataset
├── movies.pickle                # Saved processed movie data
├── similarity.joblib            # Saved similarity matrix
└── README.md                    # Project documentation
```

The two CSV files are notebook inputs. The two saved artifact files are required by the Streamlit application. Include them in the repository if their size and dataset licensing allow it, or provide clear instructions for obtaining or generating them.

## Concepts Covered

| Area | Concepts |
|---|---|
| Data handling | CSV loading, Pandas DataFrames, merging, column selection |
| Data cleaning | Handling missing values and duplicate checks |
| Text preprocessing | Extracting text from structured values, lowercasing, removing spaces |
| NLP | Tokenization and Porter Stemming |
| Feature extraction | CountVectorizer and stop-word removal |
| Similarity | Cosine similarity and ranking |
| Recommendation systems | Content-based filtering |
| App development | Streamlit title, dropdown selection, button, and result display |
| Model/data persistence | Pickle and Joblib |

## Notes

- The application requires both `movies.pickle` and `similarity.joblib`; it will not start successfully if either file is missing or the paths are incorrect.
- Keep the row order of `movies.pickle` aligned with the row and column order used to create `similarity.joblib`. The app uses the selected movie's DataFrame index to access the corresponding similarity row.
- The notebook expects the two TMDB CSV files to be available at the paths used in the notebook.
- The current interface displays movie titles only; it does not display posters, descriptions, ratings, or similarity percentages.
- The application returns five recommendations, excluding the selected movie itself.
- Confirm dataset terms and licensing before publishing the raw datasets or generated files to a public repository.

## Author

Built as a Python, NLP, and machine-learning project to explore content-based movie recommendations.
