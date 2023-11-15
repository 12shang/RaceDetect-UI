import streamlit as st
import pandas as pd

st.set_page_config(page_title="RACEDetect", page_icon=":radio_button:")

# Define the title with emojis using Markdown
title_text = "LFCM: LEVERAGING COMMENT FEATURES IN MULTIMODAL RACIST POST DETECTION"
emojis = "📑📲"

# Combine the title and emojis using Markdown syntax
st.markdown(f"# {title_text} {emojis}")
st.text("🚀 Welcome to RACEDetect web application, a tool for detecting racist posts using ")
st.text("the LFCM model. Leverage comment features and early deep fusion to enhance")
st.text("detection accuracy and create a safer and more inclusive online community.")
st.markdown("---")

# Create a combo list in the menu bar for model selection
selected_model = st.sidebar.selectbox("Select a Model", ["FCM Model", "LFCM Model"])

# Create an input to upload a CSV file
st.sidebar.title("Upload Data")
uploaded_file = st.sidebar.file_uploader("📂 Upload Data", type=["csv"])

# Add some space above the file uploader
st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Define a dictionary to store results for both models
model_results = {
    "FCM Model": None,
    "LFCM Model": None,
}

# Define a function to process and display the data for the FCM Model
def process_data_fcm(uploaded_file):
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        # Assuming that the CSV file has columns named "Tweet Text," "Image," and "Comments"
        if "Tweet Text" in data.columns and "Image" in data.columns and "Comments" in data.columns:
            tweet_sheet = data["Tweet Text"]
            image_url = data["Image"].iloc[0]  # Assuming the image URL is in the first row of the "Image" column
            comment_sheet = data["Comments"]

            model_results["FCM Model"] = {
                "tweet_sheet": tweet_sheet,
                "image_url": image_url,
                "comment_sheet": comment_sheet,
            }

# Define a function to process and display the data for the LFCM Model
def process_data_lfcm(uploaded_file):
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        # Assuming that the CSV file has columns named "Tweet Text," "Image," and "Comments"
        if "Tweet Text" in data.columns and "Image" in data.columns and "Comments" in data.columns:
            tweet_sheet = data["Tweet Text"]
            image_url = data["Image"].iloc[0]  # Assuming the image URL is in the first row of the "Image" column
            comment_sheet = data["Comments"]

            model_results["LFCM Model"] = {
                "tweet_sheet": tweet_sheet,
                "image_url": image_url,
                "comment_sheet": comment_sheet,
            }

# Create a button to start processing for the selected model
if st.sidebar.button("Start Processing") and uploaded_file:
    if selected_model == "FCM Model":
        process_data_fcm(uploaded_file)
    elif selected_model == "LFCM Model":
        process_data_lfcm(uploaded_file)

# Depending on the selected model, display different content on the main page
if selected_model == "FCM Model":
    #st.header("FCM Model Page")
    fcm_results = model_results["FCM Model"]
    if fcm_results:
        tweet_sheet = fcm_results["tweet_sheet"]
        image_url = fcm_results["image_url"]
        comment_sheet = fcm_results["comment_sheet"]
        
        st.subheader("Tweet Text (FCM Model):")
        for tweet_text in tweet_sheet:
            if pd.notna(tweet_text):  # Check for non-missing values
                st.write(tweet_text)

        st.subheader("Image (FCM Model):")
        st.image(image_url)

        st.subheader("Comments (FCM Model):")
        st.table(comment_sheet)
    else:
        st.warning("No FCM Model results available. Please upload data and click 'Start Processing'.")

elif selected_model == "LFCM Model":
    #st.header("LFCM Model Page")
    lfcm_results = model_results["LFCM Model"]
    if lfcm_results:
        tweet_sheet = lfcm_results["tweet_sheet"]
        image_url = lfcm_results["image_url"]
        comment_sheet = lfcm_results["comment_sheet"]
        
        st.subheader("Tweet Text (LFCM Model):")
        for tweet_text in tweet_sheet:
            if pd.notna(tweet_text):  # Check for non-missing values
                st.write(tweet_text)

        st.subheader("Image (LFCM Model):")
        st.image(image_url)

        st.subheader("Comments (LFCM Model):")
        st.table(comment_sheet)
    else:
        st.warning("No LFCM Model results available. Please upload data and click 'Start Processing'.")
