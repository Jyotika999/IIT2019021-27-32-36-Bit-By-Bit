# # EDA.py
# import streamlit as st
# def app():
#     st.title('APP2')
#     st.write('Welcome to app2')

#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


import sweetviz

def app():
    train = pd.read_csv("hepatitis.csv")

    train.head()

    # In[5]:

    train.tail()

    # In[ ]:

    # analysis of alk_phosphate

    # In[14]:

    analysisofphosphate = sweetviz.analyze([train, "Train"], target_feat='alk_phosphate')

    # In[21]:

    analysisofphosphate.show_html('ReportEDAofalk_phosphate.html')

    # In[17]:

    # analysis of age
    analysisofage = sweetviz.analyze([train, "Train"], target_feat='age')

    # In[18]:

    analysisofage.show_html('ReportEDAofage.html')

    # In[ ]:

    # In[ ]:

