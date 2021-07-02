import streamlit as st
import pandas as pd
import numpy as np
import io
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns
import matplotlib
import joypy
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
matplotlib.use("Agg")




def app():
    #EDA = st.sidebar.button('Exploratory Data Analysis')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    #if EDA:
    st.header("DATASET")
    df = pd.read_csv('insuranceFraud.csv')
    st.dataframe(df,width=2000)

    if st.checkbox("Show Shape"):
        df = pd.read_csv('insuranceFraud.csv')
        st.write(df.shape)
        data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
        df = pd.read_csv('insuranceFraud.csv')
        cols_to_drop = ['policy_number', 'policy_bind_date', 'policy_state', 'insured_zip', 'incident_location',
                        'incident_date', 'incident_state', 'incident_city',
                        'insured_hobbies', 'auto_make', 'auto_model', 'auto_year']
        df.drop(columns=cols_to_drop, inplace=True)
        # st.dataframe(df.head())

    if  st.checkbox("check missing values"):
            df = pd.read_csv('insuranceFraud.csv')
            df = df.replace('?', np.nan)
            #st.dataframe(df.head())
            #null_values = pd.DataFrame(df.isna().sum())
            #null_values = df.isna()
            st.write(df.isna().sum())
    #if st.checkbox ("ckeck for numerical and categorical columns"):
            #pass
            df1 = pd.read_csv('insuranceFraud.csv')
            #buffer = io.StringIO()
            #df.info(buf=buffer)
            pr = ProfileReport(df, explorative=True)
            pr.to_file(output_file='output.html')
            #st_profile_report(pr)cn

            #s = buffer.getvalue()
            #df1 = pd.DataFrame(buffer.getvalue())
            #print(st.write(df1.info(verbose=True)))
            #st.write(s)

            #st.dataframe(df1.info(verbose=True))
    #st.info("As the columns which have missing values, they are only categorical, we'll use the categorical imputer")
    prediction = st.sidebar.button("Prediction")
    st.info("we can see that for almost all categories of the gender of the insured the data is uniformly distributed")
    df['insured_sex'] = df['insured_sex'].map({'FEMALE' : 0, 'MALE' : 1})
    fig = sns.distplot(df['insured_sex'])
    st.pyplot()
    #fig = sns.distplot(df['insured_sex'])
    #ax.scatter([1, 2, 3], [1, 2, 3])
    #st.pyplot(fig)
    #
    st.info("we  can see that for almost all categories of the education level of the person insured the data is uniformly distributed")
    df['insured_education_level'] = df['insured_education_level'].map(
        {'JD': 1, 'High School': 2, 'College': 3, 'Masters': 4, 'Associate': 5, 'MD': 6, 'PhD': 7})
    fig =sns.distplot(df['insured_education_level'])
    st.pyplot()

    st.info(" We can see that there are least claims for trivial incidents,"
            "most claims for minor incidents,and for major and Total loss incidents the claims are almost equal.")
    df['incident_severity'] = df['incident_severity'].map(
        {'Trivial Damage': 1, 'Minor Damage': 2, 'Major Damage': 3, 'Total Loss': 4})
    fig =sns.distplot(df['incident_severity'])
    st.pyplot()
    """
    We can see that there are least claims for trivial incidents,
    most claims for minor incidents,
    and for major and Total loss incidents the claims are almost equal.
    """

    st.info("from the graph it can be concluded that most of the fraud cases are done by the customers new to the company and that too comparatively younger ones.")

    """
    from the graph it can be concluded that most of the fraud cases are done by the customers new 
    to the company and that too comparatively younger ones. 
    """
    fig = sns.scatterplot(df['months_as_customer'], df['age'], hue=df['fraud_reported'])

    st.pyplot()

    st.info("From the plot below, we can see that there is high correlation between Age and the number of months. we'll drop the age column."
            "Also, there is high correlation between total claim amount, injury claim,vehicle claim, and property claim as total claim "
            "is the sum of all others. So, we'll drop the total claim column.")
    df['policy_csl'] = df['policy_csl'].map({'100/300': 1, '250/500': 2.5, '500/1000': 5})
    df['property_damage'] = df['property_damage'].map({'NO': 0, 'YES': 1})
    df['police_report_available'] = df['police_report_available'].map({'NO': 0, 'YES': 1})
    df['fraud_reported'] = df['fraud_reported'].map({'N': 0, 'Y': 1})

    num_df= df.select_dtypes(include=['int64']).copy()
    plt.figure(figsize=(23, 16))
    fig = sns.heatmap(num_df.corr(), annot=True)
    st.pyplot()
    #st.write(sns.distplot(df['insured_sex']))
#def dataframe_info():


    #with open("df_info.txt","w",encoding="utf-8") as f:

    st.info("plots to analyze relationship between different features")
    fig = px.scatter(df, x= "months_as_customer", y = 'age', color = "fraud_reported", marginal_x = "rug", marginal_y = 'histogram')
    fig.update_traces(marker_size= 15, selector = dict(type='scatter'))
    st.plotly_chart(fig,use_container_width=True)

    fig = px.scatter(df, x= 'months_as_customer', y = 'policy_annual_premium', color = 'fraud_reported', marginal_x = 'rug', marginal_y = 'histogram')
    st.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(df, x= 'months_as_customer', y = 'total_claim_amount', color = 'fraud_reported', marginal_x = 'rug', marginal_y = 'histogram')
    st.plotly_chart(fig, use_container_width=True)

    st.info("Let’s see how Total Claim, Injury Claim, Property Claim, and Vehicle Claim are related to fraud_reported.")
    fig = px.scatter_matrix(df, dimensions=['total_claim_amount', 'injury_claim', 'property_claim', 'vehicle_claim'], color = 'fraud_reported')
    st.plotly_chart(fig)

    fig, axes = joypy.joyplot(df,column=['incident_hour_of_the_day', 'number_of_vehicles_involved', 'witnesses'], by='incident_city', ylim = 'own',
    figsize = (20, 10),
    alpha = 0.5,
    legend = True)
    plt.title('Incident hour, No.of vehicles, witnesses vs Incident City', fontsize = 20)
    st.pyplot(fig)

    #x1 = df['insured_sex']
    #train = df[['insured_sex', 'fraud_reported']].groupby(['insured_sex']).count().sort_values(by='fraud_reported', ascending = False)
    #fig1 = sns.countplot(x= x1, hue ="fraud_reported", data =df)
    #st.pyplot(fig = fig1)
