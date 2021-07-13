import streamlit as st





class Multiple_Modules:


    def __init__(self):

        self.apps = []





    def add_Module(self,module_title,function):

        self.apps.append({
            "module_title": module_title,
            "function" : function
        })


    def run(self):
        app = st.sidebar.radio(
            'Go To',
            self.apps,
            format_func=lambda app: app['module_title'])

        app['function']()