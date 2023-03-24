import streamlit as st
import smtplib
import re
from PIL import Image
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# hide_ststyle = """
#             <style>
#             MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
c1,c2,c3=st.columns([1,1,1])
page_bg="""
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://i.imgur.com/T5CRnc9.png");
    background-size: cover;
}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
</style>
"""
# with c2:
st.markdown(page_bg,unsafe_allow_html=True)

with c1:
    st.write("ok")

st.write(
    '''<style>
    .my-div {
        position: relative;
    }
    .my-div::after {
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        width: 1px;
        border-right: 10px solid black;
        margin-left: 50%;
        height: 250px;
    }
</style>
<div class="my-div">
    
</div>
''',unsafe_allow_html=True)



with c3:
    text_input_value = st.text_input('Enter some text')
    if st.button('Click to clear text'):
        # Clear the text_input widget
        
        print(text_input_value)



# st.write('''<h1 style="font-family: Helvetica; font-size: 40px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px;"><span style="color: #FF7A59">Hello World!</span></h1>''',unsafe_allow_html=True)


