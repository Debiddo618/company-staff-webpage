import streamlit as st
from send_email import send_email

with st.form(key="form"):
    email = st.text_input("Your Email Address",key="email")
    topic = st.selectbox("What topic do you want to discuss?",options=("Job Inquiries","Project Proposals","Other"),key="select_box")
    text = st.text_area("Text")
    message = """\
Subject: New email from {}

From: {}
Topic: {}
{}
""".format(email,email,topic,text)
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your message was sent successfully")