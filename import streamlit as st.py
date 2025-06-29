import streamlit as st 

st.title("welcome to Fazara Fragrance")
st.header("BEST PERFUME FOR MEN")

import pandas as pd
name=st.text-input("Enter your name:")
Addrees=st.text-input("Enter your Addrees:")
Order=st.selectbox("Enter your oder:",(1,2,3,4,5,6,7,8,9,10))
adr=st.text_area("Enter your text:")
Button=st.button("Done")
if button:
    st.markbown(F"""
                name:{name}
                address:{adr}
                oder:{oder}""")
                
                