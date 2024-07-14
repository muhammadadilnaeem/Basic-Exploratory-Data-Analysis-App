# In this file we will create Basic EDA App with Streamlit

# Importing necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components
from PIL import Image
import base64

# Setting the page configuration
st.set_page_config(
    page_title="Exploratory Data Analysis (EDA) App",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Adding some CSS for a better UI
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .report-container {
            max-width: 100%;
        }
        .css-18e3th9 {
            padding-top: 1rem;
        }
        .css-1d391kg {
            padding-top: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

# Title of the web app
st.markdown("""
# **Exploratory Data Analysis (EDA) App**

- This app is developed by **Adil Naeem** called **EDA app**. 
- This app helps you to perform EDA on your dataset. Let's get started!
            
""")

# Add image file to the app with a size of 800x800
image = Image.open(r'C:\Users\user\Desktop\Streamlit_dashboards\Exploratory Data Analysis App\data.jpg')
image_width = 800 # image_width = st.slider("Image Width", min_value=700, max_value=800, value=700, step=5)
st.image(image, width=image_width)

# Sidebar for user interactions
st.sidebar.header("Instructions")
st.sidebar.markdown("""
1. **Upload your CSV file**: Use the file uploader below to upload your CSV dataset.
2. **View the DataFrame**: The uploaded dataset will be displayed in the main page.
3. **Generate EDA Report**: An interactive profiling report will be generated and displayed.
4. **Explore the Report**: Scroll through the report for insights and visualizations.
""")

st.sidebar.header("Upload your CSV file")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Function to load data
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# Function to generate profile report
@st.cache_data
def generate_profile_report(dataframe):
    return ProfileReport(dataframe, explorative=True)

# If file is uploaded, load data and display profiling report
if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.header('**Input DataFrame**')
    st.write(df)

    st.header('**Profiling Report**')
    profile_report = generate_profile_report(df)
    profile_html = profile_report.to_html()
    components.html(profile_html, height=1000, scrolling=True)

# If no file is uploaded, display info and offer example dataset
else:
    st.sidebar.info('Awaiting for CSV file to be uploaded...')
    if st.sidebar.button('Press to use Example Dataset'):
        @st.cache_data
        def load_example_data():
            return pd.DataFrame(np.random.rand(100, 5), columns=['a', 'b', 'c', 'd', 'e'])

        df = load_example_data()
        st.header('**Example DataFrame**')
        st.write(df)

        st.header('**Profiling Report**')
        profile_report = generate_profile_report(df)
        profile_html = profile_report.to_html()
        components.html(profile_html, height=1000, scrolling=True)
