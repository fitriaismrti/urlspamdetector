import streamlit as st
from predict_function import *

import pickle
import validators

model = pickle.load(open("final_model.pkl", "rb"))

st.title("URL Spam Checker")
st.write("We made this application to help you find out if a link is spam or not, you can check a link before click it to keep your device safe. Randomly clicking links or going to unknown websites on your computer, phone, or even smart TV can put you at risk of covertly downloaded software intended to damage or disable your computer or other devices. We made this application using the Naive Bayes and Simplification method. Then, we tested using a dataset collection of spam and non-spam urls that we got from kaggle. We hope that with this application people can be vigilant in accessing a link whose source is not clear.")

link = st.text_input(label = "Input URL", placeholder = "Insert your url here")

if st.button("Check"):
    if link == '':
        st.write("Please input the link")
    else:
        result = predict_result(link)
        if result == -1:
            st.write("Please input a valid link")
        elif result == 0:
            st.write("Your link is not a spam")
        elif result == 1:
            st.write("Yous link is a spam")