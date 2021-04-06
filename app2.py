
import pandas as pd
import numpy as np


import sweetviz

def app():
    train = pd.read_csv("Dataset/hepatitis.csv")

    train.head()


    train.tail()



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

