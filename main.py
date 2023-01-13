import streamlit as st
import pandas as pd

st.title("Hi! Welcome to Malaysian Food Recognition")
st.header("About")
about = "This web application offers Malaysian food recognition for advancing AI in food and healthcare, particularly for Malaysian local food. The food image recognition technology is powered by the state-of-the-art deep learning techniques."
st.write(about)

file = st.file_uploader('Upload an Image')

import streamlit as st
import pandas as pd

malaysian_food_df = pd.DataFrame(food_info.malaysian_food)

# Get Nasi Lemak from the dataframe
nasi_lemak_df = malaysian_food_df[food_info.malaysian_food_df['name'] == 'Nasi Lemak']

# Display the content in a table using streamlit
st.table(nasi_lemak_df)