import streamlit as st
import pickle

movies_data = pickle.load(open('Pickle_files/movies_data.pkl','rb'))
movies_about = pickle.load(open('Pickle_files/movie_about.pkl','rb'))
similarity = pickle.load(open('Pickle_files/similarity.pkl','rb'))
posters = pickle.load(open('Pickle_files/posters.pkl','rb'))

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .reportview-container {
        background: #1a1a1a;
        color: #f8f8f8;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def fetch_poster(movie_name):
  movie_id = movies_data[movies_data['title'] == movie_name]['id'].iloc[0]
  poster_index = posters[posters['id'] == movie_id].index[0]
  poster_path = posters['poster_path'].iloc[poster_index]
  full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
  return full_path

def fetch_movie_about(movie_name):
  movie_id = movies_data[movies_data['title'] == movie_name]['id'].iloc[0]
  movies_about_index = movies_about[movies_about['id']==movie_id].index[0]
  overview = movies_about['overview'].iloc[movies_about_index]
  genre = movies_about['genre_names'].iloc[movies_about_index]
  poster_index = posters[posters['id'] == movie_id].index[0]
  selected_poster_path = posters['backdrop_path'].iloc[poster_index]
  full_path = "https://image.tmdb.org/t/p/w500/"+selected_poster_path
  return overview,genre,full_path

st.header('Movie Hub')
st.image('background.jpg')

st.subheader("Search Movie Name")
select_value = st.selectbox('', movies_data['title'])


def recommend_movie(movie):
  index = movies_data[movies_data['title']==movie].index[0]
  sorted_similarty = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda similarity_tuple:similarity_tuple[1])
  recommend = []
  recommend_poster = []
  for i in sorted_similarty[1:6]:
    recommend.append(movies_data.iloc[i[0]].title)
    recommend_poster.append(fetch_poster(movies_data.iloc[i[0]].title))
  return recommend,recommend_poster

if st.button("Search"):
  select_movie_overview,select_movie_genre,select_movie_poster = fetch_movie_about(select_value)
  column1,column2 = st.columns(2)
  with column1:
    st.subheader(select_value)
    st.image(select_movie_poster)
  with column2:
    st.subheader("Plot")
    st.write(select_movie_overview)
    st.subheader("genre")
    st.write(select_movie_genre)

  st.header('Recommended Movies')
  movie_name,movie_poster = recommend_movie(select_value)
  col1,col2,col3,col4,col5 = st.columns(5)
  with col1:
    st.image(movie_poster[0])
    st.write(movie_name[0])
  with col2:
    st.image(movie_poster[1])
    st.write(movie_name[1])
  with col3:
    st.image(movie_poster[2])
    st.write(movie_name[2])
  with col4:
    st.image(movie_poster[3])
    st.write(movie_name[3])
  with col5:
    st.image(movie_poster[4])
    st.write(movie_name[4])