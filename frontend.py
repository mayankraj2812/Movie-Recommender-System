import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_ids):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_ids)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movieindex=movies[movies['title']==movie].index[0]
    distances=similarity[movieindex]
    movielist=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommendedmovieposter=[]
    for i in movielist:
        movieid=movies.iloc[i[0]].movie_id
#fetch poster from api
        
        recommended_movies.append(movies.iloc[i[0]].title)
        recommendedmovieposter.append(fetch_poster(movieid))
    return recommended_movies,recommendedmovieposter

moviedict=pickle.load(open('moviedict.pkl','rb'))
movies=pd.DataFrame(moviedict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selectedmoviename = st.selectbox(
    "Please Select a Movie",
    (movies['title'].values),
)

st.write("You selected:", selectedmoviename)

if st.button("Show Recommendation"):
    names,posters=recommend(selectedmoviename)
    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
       st.text(names[0])
       st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
