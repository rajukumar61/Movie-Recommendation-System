# Movie-Recommendation-System

This project is a movie recommendation system that suggests movies to users based on their preferences. The system utilizes machine learning techniques to analyze movie data and provide personalized recommendations to users.

# File Structure

- **frontend** : a Node.js library file used in building carousels in the frontend of this application
- **app3.py** : a Python file containing frontend design codes and using the database files (.pkl)
- **dataset.csv** : the database file containing 10k movies data
- **Main.ipynb** : Jupyter Notebook file containing machine learning codes for the RS system
- **movies_list.pkl** : the pickle file extracted from Main.ipynb containing a list of movies
- **similarity.pkl** : the pickle file extracted from Main.ipynb containing an array list of cosine similarity of each movie

# Libraries
  - pandas
  - streamlit
  - scikit-learn
  - numpy
  - pickle

# Database
The TMDB Movies Dataset has been used in this project. This dataset contains data for 10k top-rated TMDB movies till 26-July-2022.

   **Content**
   The Dataset contains the following columns:
      - ID
      - Title
      - Genre
      - Overview
      - Popularity
      - Original_language
      - Release_date
      - Vote_average
      - Vote_count

## Data Processing
Collecting useful data
The project selects only the essential columns from the dataset, including 'id', 'title', 'overview', and 'genre'. These columns are considered sufficient for movie recommendation purposes, particularly for content-based filtering methods.

Combining Useful Columns & making a new column
The project concatenates the 'overview' and 'genre' columns into a new column called 'tags', effectively combining information from both columns for recommendation purposes. This new 'tags' column can be used in recommendation systems to capture relevant information from both the movie overview and genre, aiding in the recommendation process based on content similarity.

Output & Result
The output of the recommendation system project is a website interface where users can select a movie from a dropdown menu containing a list of 10,000 movies. After selecting a movie, users can choose the number of movies they want to be recommended (default is 5). Upon clicking the "Show Recommendation" button, the system displays a list of recommended movies along with their respective posters.

These posters are fetched from the TMDB (The Movie Database) website's APIs using the movie IDs that are recommended based on the selected movie. This functionality enhances the user experience by providing visual representations of the recommended movies alongside their titles.

The entire project is coded in Python.

Steps to Run
Clone this repository to your local machine.
Open the cloned folder in Visual Studio Code or any terminal of your choice.
To add the "frontend" folder for the carousel:
Create a folder named "frontend".
Navigate to the "frontend" folder in the terminal.
Run the following commands:
arduino
Copy code
npm i
npm run build
After completing the frontend setup, navigate back to the main folder in the terminal.
Run the following command to start the application:
arduino
Copy code
streamlit run app.py
Hit enter, and the movie recommendation system will be launched in your default web browser.
Note: Ensure that you have all the required libraries installed in your Python environment before running the application.
