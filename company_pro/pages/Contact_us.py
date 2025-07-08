import streamlit as st
import sys
import os

# Add parent directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from send_email import send_mail

import pandas

df = pandas.read_csv("C:/Users/Arun JH/Desktop/vaibhavi-proj/company_pro/pages/topics.csv")


st.header("Contact us ")
#creating a form page to send a message through the email
with st.form(key="my_form"):
    user_email=st.text_input("Your Email Address")
    option = st.selectbox(
        'What topic do you want to discuss?',
         df["topics"])


    raw_message =st.text_area("Your Message")
    message = f"""\
Subject: New Email from {user_email}
From : {user_email} 
Topic: {option}
{raw_message}
"""
    message = message + "\n" + user_email
    button = st.form_submit_button("SUBMIT")

    if button:
        send_mail(message)
        st.info("Your email was sent")
