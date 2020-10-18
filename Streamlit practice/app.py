#in the command line, have to say pip install streamlit 
#(streamlit) C:\Users\Nasik\Desktop>streamlit run app.py

import streamlit as st

#text/Tiyle 
st.title("Streamlit Tutorial")

st.header("This is a header")


st.subheader("This is a sub-header")

#text
st.text("Hello streamlit")

#markdown
st.markdown('###this is a markdown')
#text

#Error/colorful text
st.success("Successful")

st.info("Information")

st.warning("Warning")

st.error("This is an error")

st.exception("Name Error('name 2 not defined ')")

#get help info about any python 
st.help(range)

#writing a text

st.write("Text with write")
st.write("Text with write")
st.write(range(10))
st.warning("Warning")

#for the images and videos, you have to keep the media in the same working directory for this example

#images 
from PIL import Image
img= Image.open("2.jpg")
st.image(img,width=300, caption="Nature")

vid_file=open("1.mkv","rb").read()
st.video(vid_file)

#audio
#audio_file= open("1.mp3","rb").read()
#st.audio(audio_file, format='audio/mp3')

#widget
#checkbox
if st.checkbox("Show/Hide"):
	st.text("Showing or hiding widget")

#radio
status =st.radio("What is your status",("Active","Incative"))

if status == 'Active':
	st.success("You are Active")

else:
	st.warning("You are Inactive")

#select box
Occupation= st.selectbox("Your Occupation", ['Programmer','Doctor', 'Lawyear'])
st.write("You have selected this option", Occupation)
#multi select 
location=st.multiselect("Where do you live?",("Bangladesh","Malaysia", "Canada", "Ireland"))

st.write("You have selected",len(location),'locations')

#slider
age=st.slider("What's your age?", 1,80)

st.write("You are",(age),'years old')

st.button("Click Me")
if st.button("About"):
	st.text("Streamlit is amazing")

#TEXT INPUT
firstname=st.text_input("Enter your first name","Type here...")
if st.button("Submit"):
	result=firstname.title()
	st.success(result)

#Text Area
message=st.text_area("Enter your message here","Type here...")
if st.button("Click to see"):
	result=message.title()
	st.success(result)

#Date Input 
import datetime
today=st.date_input("Today is ", datetime.datetime.now())

#Time 
The_time= st.time_input("The times is ", datetime.time())

#Displaying JSON
st.text("Display JSON")
st.json({'name':'Nasik', 'gender': 'Male'})


#Display RAW CODE
st.text("Display Raw code")
st.code("import numpy as np")

#Display RAW CODE
with st.echo():
	#this will also show as a comment 
	import pandas as pd
	df=pd.DataFrame()


#Progress Bar
import time 
my_bar= st.progress(0)
for p in range(50):
	my_bar.progress(p+1)

#Spinner
with st.spinner ("waiting.."):
	time.sleep(2)
st.success("Finished!!")

#Ballon
#st.balloons()

#sidebars

st.sidebar.header("About")
st.sidebar.text("This is a Tutorial")
#functions
#cache will take less time
@st.cache
def run_fxn():
	return range(50)
st.write(run_fxn())
"""
#other important features
#plot
st.pyplot()

#dataframes
st.dataframe(df)

#tables
st.table(df)

"""



