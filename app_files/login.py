import base64

import streamlit as st
import pandas as pd
from PIL.ImagePath import Path
from PIL import Image
import numpy as np
import time
#@st.cache
#st.set_page_config(
 #   page_title="Insurance Fraud Analysis", layout="wide", page_icon="images/car-keys.png",
#)

st.header("Login Section")
#st.help(pd.DataFrame)
#with st.spinner('Wait for it...'):
    #time.sleep(5)
#st.success('Done!')
#st.balloons()
#import time
#my_bar = st.progress(0)
#for percent_complete in range(100):
    #time.sleep(0.1)
    #my_bar.progress(percent_complete + 1)
#color = st.color_picker('Pick A Color', '#00f900')
#st.write('The current color is', color)
#uploaded_file = st.file_uploader("Choose a file")
#if uploaded_file is not None:
     # To read file as bytes:
 #   bytes_data = uploaded_file.getvalue()
 #   st.write(bytes_data)
 #   # To convert to a string based IO:
 #   stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
 #   st.write(stringio)
     # To read file as string:
 #   string_data = stringio.read()
 #   st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
 #   dataframe = pd.read_csv(uploaded_file)
 #   st.write(dataframe)
#st.text_area('Text to analyze', '''
 # It was the best of times, it was the worst of times, it was
 # the age of wisdom, it was the age of foolishness, it was
 # the epoch of belief, it was the epoch of incredulity, it
 #  was the season of Light, it was the season of Darkness, it
 # was the spring of hope, it was the winter of despair, (...)''')
#title = st.text_input('Movie title', 'Life of Brian')
#st.write('The current movie title is', title)
def app():
    st.header('Login Section')
    username = st.text_input('User Name')
    password = st.text_input("Password",type='password')
    login_cols = st.beta_container()
    logeed = st.checkbox("Keep me Logged In")
    login_cols= st.button("Login")

    st.markdown("""
        ----                           
       """)
    create_account = st.button("Create New Account")

#while not logeed:
     # st.balloons()
     # time.sleep(4)
#else:
home = st.sidebar.button('Home')
if home:
    st.title("**Insurance Fraud analysis**")
    st.markdown("""
        ----                           
       """)
#st.title("my first app")
#st.write("Here's our first attempt at using data to create a table:")
#st.write(pd.DataFrame({
#'first column': [1, 2, 3, 4],
#'second column': [10, 20, 30, 40]
#}))

#df = pd.DataFrame({
#'first column': [1, 2, 3, 4],
#'second column': [10, 20, 30, 40]
#})
#df

   #chart_data = pd.DataFrame(
   #np.random.randn(20, 3),
   #columns=['a', 'b', 'c'])
   #st.line_chart(chart_data)

  # map_data = pd.DataFrame(
   #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   #columns=['lat', 'lon'])
   #st.map(map_data)

#if st.checkbox('Show dataframe'):
   #chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
   #chart_data

#option = st.selectbox('Which number do you like best?', df['first column'])
#'You selected: ', option

#option = st.selectbox('Which number do you like best?',df['first column'])
#'You selected:', option
#'fjwwihtebvveirehjrorhlwjgngbltght4ekdnwjkbrguei'


#left_column, right_column = st.beta_columns(2)
#pressed = left_column.button('Press me?')
#if pressed:
 #  right_column.write("Woohoo!")
#expander = st.beta_expander("FAQ")
#expander.write("Here you could put in some really, really long explanations...")

#latest_iteration = st.empty()
##bar = st.progress(0)
#for i in range(100):
 #  # Update the progress bar with each iteration.
 #  latest_iteration.text(f'Iteration {i+1}')
 #  bar.progress(i + 1)
 #  time.sleep(0.1)



#add_selectbox = st.sidebar.slider('how are you')
#selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
    image = Image.open('images/car-keys.png')
#st.image(image, caption='Sunrise by the mountains',)
#st.image(image)
#st.text('hello')
#st.beta_set_page_config(layout="wide")

    title_container = st.beta_container()
    col1, col2 = st.beta_columns([1,2])

    with title_container:
         with col1:
            #col1.success('first')
            st.image(image,width=500)
         with col2:
              #col2.success('second')
              #st.text('Car Insurance')
              st.markdown('<h1 style="color: purple;">Car Insurance</h1>',unsafe_allow_html=True)
              lines="A comprehensive car insurance policy, also known as motor package insurance, saves you" \
                  "money when your car is damaged in an accident or natural calamity. It also covers your" \
                  "vehicle against theft and burglary. At times, you may end up hurting others or damaging" \
                  "property in an accident. A car insurance policy covers such third party liabilities as" \
                  "well. If you own a car in India, having third party insurance is a must for you. That’s" \
                  "why it’s crucial to buy and renew your policy on time to stay on the right side of the"  \
                  "law and be covered against car damages. At an affordable premium, our reliable car insurance" \
                  "policy protects you against all these risks so that you can drive worry-free." \
                  "Apart from comprehensive car insurance, third-party only and own-damage only car insurance policies" \
                  "are also available. You can choose the policy type as per your needs."
              st.markdown(f"## *{lines}*")
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.header("""
                                                 **What are the different types of car insurance policies?**

              """)
    image1 = Image.open('images/private_car_package_policy.png')
    image2 = Image.open('images/standalone_vehicle.png')
    image3 = Image.open('images/third_party_car.png')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    title1_container = st.beta_container()
    type1, type2,type3 = st.beta_columns([1,1,1])
    #st.markdown('<h1 style="color: majenta;">Car Insurance</h1>',unsafe_allow_html=True)
    with title_container:
         with type1:
                st.image(image1)
                type1.header('\nPrivate car package policy\n')
                type1.write("A comprehensive car insurance policy offers complete protection to you. It covers not only the" \
                            "costs incurred on damages to a third party but also the damages to your car. This policy type" \
                            "also covers car theft and damages caused by fire, burglary and natural disasters.")

         with type2:
                 st.image(image2)
                 type2.header('\nStand-alone own-damage car insurance\n')
                 type2.write("With our stand-alone own-damage car insurance, you are covered for any accidental damages to your car. \
                     These could be due to natural disasters like earthquake, flood, cyclone, and landslide,\
                     or due to manmade disasters like theft, burglary, riot or strike. To buy this insurance,"
                     "you should have an active third party insurance policy of the vehicle.")
         with type3:
                 st.image(image3)
                 type3.header('\nThird party car insurance\n')
                 type3.write("In this type of insurance policy, you are covered against legal liabilities arising out of an accident.\
                         If your car causes injuries to a third party or damages surrounding property, then we will take care of the expenses.")
    st.markdown("""

                    ----
    """)
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')

    title_container = st.beta_container()
    col3, col4 = st.beta_columns([1,2])

    image4 = Image.open('images/ui-tw-insurance-policy.png')

    with title_container:
             with col3:
               #col1.success('first')
                st.image(image4)
             with col4:
             #col2.success('second')
             #st.text('Car Insurance')
                st.markdown('<h1 style="color: purple;">Two Wheeler Insurance</h1>',unsafe_allow_html=True)
                lines1="A two wheeler insurance policy protects your bike or scooter against any damages caused due to" \
               " road accidents, natural disaster, and theft or loss." \
               " A bike insurance policy covers damages to your two wheeler and " \
               "legal liability towards third party. With us, you can secure your bike at affordable rates."
                st.markdown(f"## *{lines1}*")

#def img_to_bytes(img_path):
#img_bytes = Path(img_path).read_bytes()
#encoded = base64.b64encode(img_bytes).decode()
#return encoded

#header_html = "<img src='images/png;base64,{}' class='img-fluid'>".format(
    #img_to_bytes("header.png")
#)
#st.markdown(
 #   header_html, unsafe_allow_html=True,
#)
  # line="In this type of insurance policy, you are covered against legal liabilities arising out of an accident " \
     # ".If your car causes injuries to a third party or damages surrounding property, then we will take care of the expenses"
   #st.markdown(f"## *{line}* ")







