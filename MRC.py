import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommend_movies =[]
    for i in distances[1:6]:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies
movie_dict =pickle.load(open('movie_dict.pkl','rb'))
movies  = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recomandation System ')

selecte_movie_name = st.selectbox(
'this page will suggest you good movies',
movies['title'].values)

if st.button('recommend'):
    recommendations = recommend(selecte_movie_name)
    for i in recommendations:
        st.write(i)