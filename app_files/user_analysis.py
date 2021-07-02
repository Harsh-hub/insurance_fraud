import streamlit as st
import pandas as pd
import numpy as np
import io
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")
import os,base64
#from database import create_table
def file_download():
    #readfile = open(os.path.join(filename)).read()
    #b64 = base64.b64decode(readfile.encode()).decode()
    #href = f'<a href="https://drive.google.com/file/d/1XnwlsoTUSu5mOEbNfMzpKaDQCeVIdrnA/view?usp=sharing"</a>'
    href ='< a href = "https://drive.google.com/file/d/1XnwlsoTUSu5mOEbNfMzpKaDQCeVIdrnA/view?usp=sharing"download > Click here < / a >'
    return href




def app():
    st.title("User Specific Analysis")
    st.sidebar.write("----")
    st.sidebar.info("In this module the user can do different plotting on his/her dataset")
    data = st.file_uploader("Upload a Dataset", type=["csv"])
    #if st.button('Download File'):
    #st.write(file_download())
    st.info('Please download the format for the data and update the file and upload it , Do not change the order of the attributes.')
    title_container = st.beta_container()
    col1, col2,col3 = st.beta_columns([3,3,1])
    with title_container:
        with col1:
             st.write("[Click to Download Format](https://drive.google.com/file/d/1XnwlsoTUSu5mOEbNfMzpKaDQCeVIdrnA/view?usp=sharing)")
        with col2:
              pass
              #st.button('See Data Description')
        with col3:
              st.button('See Data Description')




        #starting of uploaded file


    st.write("----")
    if data:
        df = pd.read_csv(data)
        #df_int = pd.read_csv(data)
        df_int = df.select_dtypes(include='int64')
        #df_float_type = pd.read_csv(data)
        df_float = df.select_dtypes(include='float64')
        #df_object = pd.read_csv(data)
        df_object = df.select_dtypes(include='object')
        #df_bool = pd.read_csv(data)
        df_bool = df.select_dtypes(include='bool')


        with st.sidebar.beta_expander('See Data Types'):
             if st.checkbox("float64"):
                 st.table(df_float.columns)
             if st.checkbox('int64'):
                 st.write(df_int.columns)
             #if st.checkbox('object'):
                 #st.write(df_object.columns)
             #if st.checkbox('bool'):
                 #st.write(df_bool.columns)
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        if st.checkbox("Show uploaded dataset"):
              st.write("Uploaded Dataset")
              #df = pd.read_csv(data)
              st.write(df)
              #st.write(df_bool)
              #st.write(df_object)
              #st.write(df_float)
              #st.write(df_int)
              #st.write("----")
              #st.write('\n')
        if st.sidebar.checkbox("Show Shape Of Dataset"):
              st.sidebar.write(df.shape)
              st.write('\n')
        if  st.sidebar.checkbox("Describe The Dataset"):
              st.subheader("Summary")
              st.write(df.describe())
              st.write("----")

        selected_plot = st.selectbox('Select the appropriate plot',('None','line plot','histogram','bar chart','pie chart','scatter plots', 'heatmap' , 'distplot'))
        if selected_plot == 'line plot':
            options_list=list(df_int.columns)
            #options_list.append('None')
            st.write(options_list)
            option_dataframe = pd.DataFrame(columns=options_list)
            options1 = st.selectbox('Select The  x coordinate',options_list)
            #options2 = st.selectbox('Select The   coordinate',options_list)
            #if st.button('Plot'):
            df1 = ['']
            st.write(df[options1])
            rows = df[options1]
            option_dataframe = pd.DataFrame(rows,columns=[options1])
            plot = st.button('Plot')
            if plot:
               st.line_chart(option_dataframe)

               #st.altair_chart(options)
               # fig = plt.plot(options)
               #st.pyplot()
               #st.write(df.plot.line(options))
               #st.write(plt.plot(options))
               #plt.show()
            #lines = df.plot.line(x='pig', y='horse')
            #streamlit.multiselect(label, options, default=None, format_func= <class 'str'>, key=None, help=None)

        if selected_plot == 'histogram':
            options_list_for_hist = list(df_int.columns)
            option_for_histogram = st.selectbox('select the variable',options_list_for_hist)
            st.write(df[option_for_histogram])

            plot = st.button('Plot')
            if plot:
                fig, ax = plt.subplots()
                ax.hist(df[option_for_histogram], bins=20)
                st.pyplot(fig)



        if selected_plot == 'bar chart':
            pass



