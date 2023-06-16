from PIL import Image 
import requests
import streamlit as st
from streamlit-lottie import st_lottie

st.set_page_config(page_title="Edwich")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()


#-----LOAD ASSETS-----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_tfb3estd.json")
img_ben = Image.open("images/ben.png")
img_dog = Image.open("images/dog.png")

#-----HEADER SECTION-------
with st.container():
    st.subheader("Hi, I'm Edrich!")
    st.title("A student from The Philippines.")
    st.write("I'm very passionate in finding ways to learn coding and fufill my dreams in the near  future.")
    st.write("[Learn more >](https://edrichcom.wordpress.com/)")

#-------WHAT I DO--------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Well in my life I do the following:
            - Doing house chores 
            - Play video games on vacant time 
            - Reading e-books when bored or just play games 
            - Study programming 
            - Guard our store 
            well that casually it for now."""
        )
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

#-----PROJECTS HAHA------
with st.container():
    st.write("---")
    st.header("My Coding Languages")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
         st.image(img_ben)
         with text_column: 
          st.subheader("HTML & CSS")
          st.write(
            """I have 0 exprience in HTML and CSS, but I'm 
            currently learning online."""
        )
          st.markdown("[LEARN HTML & CSS....](https://www.freecodecamp.org/news/html-css-11-hour-course/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_dog)
        with text_column:
            st.subheader("Python")
            st.write(
                ''''Python my favorite language to learn, I also have 0.1 experience in this 
                particuar languange. I'm eager to learn thsi type of language 
                cause it is one of the esiest to work with and the most popular 
                and well know language.'''
            )
            st.markdown("[LEARN PYTHON....](https://www.freecodecamp.org/news/tag/python/)")
