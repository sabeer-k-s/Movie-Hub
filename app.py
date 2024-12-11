from flask import Flask, render_template, request, jsonify
import pickle

# Load pickle files
movies_data = pickle.load(open('Pickle_files/movies_data.pkl', 'rb'))
movies_about = pickle.load(open('Pickle_files/movie_about.pkl', 'rb'))
similarity = pickle.load(open('Pickle_files/similarity.pkl', 'rb'))
posters = pickle.load(open('Pickle_files/posters.pkl', 'rb'))

app = Flask(__name__)

# Helper functions
def fetch_poster(movie_name):
    movie_id = movies_data[movies_data['title'] == movie_name]['id'].iloc[0]
    poster_index = posters[posters['id'] == movie_id].index[0]
    poster_path = posters['poster_path'].iloc[poster_index]
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

def fetch_movie_about(movie_name):
    movie_id = movies_data[movies_data['title'] == movie_name]['id'].iloc[0]
    movies_about_index = movies_about[movies_about['id'] == movie_id].index[0]
    overview = movies_about['overview'].iloc[movies_about_index]
    genre = movies_about['genre_names'].iloc[movies_about_index]
    poster_index = posters[posters['id'] == movie_id].index[0]
    selected_poster_path = posters['backdrop_path'].iloc[poster_index]
    full_path = f"https://image.tmdb.org/t/p/w500/{selected_poster_path}"
    return overview, genre, full_path

def recommend_movie(movie):
    index = movies_data[movies_data['title'] == movie].index[0]
    sorted_similarity = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend = []
    recommend_poster = []
    for i in sorted_similarity[1:6]:
        recommend.append(movies_data.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_data.iloc[i[0]].title))
    return recommend, recommend_poster

# Routes
@app.route('/')
def home():
    return render_template('index.html', movies=list(movies_data['title']))

@app.route('/search', methods=['POST'])
def search():
    movie_name = request.form['movie_name']
    if movie_name in movies_data['title'].values:
        overview, genre, poster = fetch_movie_about(movie_name)
        recommend, recommend_posters = recommend_movie(movie_name)
        return jsonify({
            'overview': overview,
            'genre': genre,
            'poster': poster,
            'recommend': recommend,
            'recommend_posters': recommend_posters
        })
    else:
        return jsonify({'error': 'Movie not found!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
