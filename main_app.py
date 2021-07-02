import streamlit as st
st.set_page_config(
 page_title="Insurance Fraud Analysis", layout="wide", page_icon="images/car-keys.png")
from MULTIAPP import Multiple_Modules
from app_files import EDA,home,user_analysis,prediction

app= Multiple_Modules()

import pandas as pd
from PIL.ImagePath import Path
from PIL import Image
import numpy as np
import time
#@st.cache





app.add_Module("home",home.app)
#app.add_Module("login",login.app)
app.add_Module("eda",EDA.app)
app.add_Module("user_specific_analysis",user_analysis.app)
app.add_Module("Prediction",prediction.app)

app.run()





