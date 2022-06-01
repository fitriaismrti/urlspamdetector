import streamlit as st
from predict_function import *

import pickle
import validators

model = pickle.load(open("final_model.pkl", "rb"))

st.title("URL Spam Detector")
st.write("updated deskripsi")

link = st.text_input(label = "Input URL", placeholder = "insert your url here")

if st.button("check"):
    if link == '':
        st.write("please input the link")
    else:
        result = predict_result(link)
        if result == -1:
            st.write("please input a valid link")
        elif result == 0:
            st.write("not spam")
        elif result == 1:
            st.write("spam")