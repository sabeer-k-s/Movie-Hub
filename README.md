# Streamlit-based IMDb Clone with NLP Movie Recommendation System

This project is a web application developed using Streamlit that serves as an IMDb clone. It provides comprehensive movie information including posters, summaries, and genres, leveraging data fetched from the TMDB API and converted into a DataFrame. The app also features a personalized movie recommendation system implemented using Natural Language Processing (NLP) techniques.

## Features

- **Comprehensive Movie Information:** Users can search for movies and receive detailed information including movie posters, summaries, and genres.
- **Personalized Movie Recommendations:** The app offers five personalized movie suggestions based on user searches and movie descriptions using NLP techniques like CountVectorizer and cosine similarity.
- **User-friendly Interface:** The application provides a seamless and engaging experience for users, integrating movie data and recommendations efficiently.

## Tech Stack

- **Python**
- **Streamlit**
- **TMDB API**
- **Pandas**
- **NLP Techniques:**
  - CountVectorizer
  - Cosine Similarity

## How It Works

1. **Data Fetching:** The application fetches movie data from the TMDB API and converts it into a DataFrame for easy manipulation and display.
2. **Search Functionality:** Users can search for any movie, and the app will display relevant information like the movie's poster, summary, and genres.
3. **Recommendation System:** Based on the user's search and the movie's description, the app provides five personalized movie recommendations. This is achieved using CountVectorizer to convert text data into vectors and cosine similarity to find movies with similar descriptions.

## Screen Recordings

<img src="https://github.com/sabeer-k-s/Movie-Hub/blob/master/Images/Desktop.gif" width='800'>

<p>
<img src="https://github.com/sabeer-k-s/Movie-Hub/blob/master/Images/Mobile.gif" width='250'>
</p>

*Include screen recordings here to demonstrate the app's functionality and user experience.*

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sabeer-k-s/Movie-Hub.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run app.py
   ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.


## Acknowledgments

- [TMDB API](https://www.themoviedb.org/documentation/api) for providing movie data.
- Streamlit for making web application development easy.

---
