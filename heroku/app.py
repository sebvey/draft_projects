import streamlit as st

import numpy as np
import pandas as pd
import requests

st.markdown("# Front App For My Project")

df = pd.DataFrame({
    'first column':list(range(1,11)),
    'sec column':np.arange(10,101,10)
})

line_count = st.slider('Select a line count',1,10,3)
head_df = df.head(line_count)

head_df

url = 'https://api-yufzv3bpca-ew.a.run.app/predict'
params = {'str_date':'2020-12-10'}

response = requests.get(url,params=params)

if response :
    st.markdown('## The API call is successful')
    st.markdown(f"The prediction is {response.json()['prediction']}")
