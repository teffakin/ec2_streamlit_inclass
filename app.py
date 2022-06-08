
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("This is a title")
st.text('This is some text.')
st.markdown("Streamlit is **_really_ cool** :+1:")
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.header('This is a header')
st.subheader('This is a subheader')

st.success('This is a success message!')
st.info('This is a purely informational message')
st.error('This is an error')

st.help(range)
st.write('Hello, *World!* :sunglasses:')

#image
#img = Image.open("images.jpeg")
#st.image(img,caption="cattie",width=300)
#st.image(img,caption="cattie",use_column_width="auto")
#st.help(st.image)
#my_video = open("ml.mov",'rb')
#st.video(my_video)

st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")


#Checkbox
cbox = st.checkbox("Hide and Seek")
if cbox:
    st.write("Hide")
else:
    st.write("Seek") 


#radio button
st.radio("Select a color",("blue","orange","yellow"))     

status = st.radio("Select a color",("Blue","Red","Yellow"))
st.write(f"Your favourite color is {status}")
#st.write("Your favourite color is {}".format(status))

#button
st.button("Button")
if st.button("Press me"):
    st.success("Analyze Results are:")

#select_box
occupation=st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Doctor"])
st.write("You selected this option:", occupation)

#multi_select
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])


#slider
option1 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=5)
option2 = st.slider("Select a number", min_value=0.2, max_value=30.2, value=5.2, step=0.2)
result=option1*option2
st.write("multiplication of two options is:",result)


#text_input
name = st.text_input("Enter your name", placeholder="Your name here")
if st.button("Submit"):
    st.write("Hello {}".format(name.title()))


#code
st.code("import pandas as pd")

st.code("import pandas as pd\nimport numpy as np")


with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df

#date input
import datetime
today=st.date_input("Today is", datetime.datetime.now())


d= st.date_input("When is your birthday", datetime.date(2022,4,28))
st.write("Your birthday is:", d)

#st.help(st.date_input)

#time input
the_time=st.time_input("The time is", datetime.time(8,45))

#st.help(st.time_input)

#sidebar
st.sidebar.title("Sidebar title")
st.sidebar.header("Sidebar header")
a=st.sidebar.slider("input",0,5,2,1)
x=st.sidebar.slider("input2")
st.write("# sidebar input result")
st.success(a*x)

#dataframe
st.write("# dataframes")
df = pd.read_csv("Advertising.csv", nrows=(100))
st.table(df.head())  
st.write(df.head()) #dynamic, you can sort, swiss knife
st.dataframe(df.head())#dynamic


#Project Example

import pickle
filename = 'my_model'
model = pickle.load(open(filename, 'rb'))
st.table(df.head())


st.write(df.describe())

TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)


my_dict = {
    "TV": TV,
    "radio": radio,
    "newspaper": newspaper,
}

df=pd.DataFrame.from_dict([my_dict])
st.table(df)


if st.button("Predict"): 
    pred = model.predict(df)
    st.write(pred)



html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Single Customer </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)


tenure=st.sidebar.slider("Number of months the customer has stayed with the company (tenure)", 1, 72, step=1) 
MonthlyCharges=st.sidebar.slider("The amount charged to the customer monthly", 0,100, step=5) 
TotalCharges=st.sidebar.slider("The total amount charged to the customer", 0,5000, step=10) 
Contract=st.sidebar.selectbox("The contract term of the customer", ('Month-to-month', 'One year', 'Two year')) 
OnlineSecurity=st.sidebar.selectbox("Whether the customer has online security or not", ('No', 'Yes', 'No internet service')) 
InternetService=st.sidebar.selectbox("Customer’s internet service provider", ('DSL', 'Fiber optic', 'No')) 
TechSupport=st.sidebar.selectbox("Whether the customer has tech support or not", ('No', 'Yes', 'No internet service'))

def single_customer():
    my_dict = {"tenure" :tenure, 
        "OnlineSecurity":OnlineSecurity, 
        "Contract": Contract, 
        "TotalCharges": TotalCharges , 
        "InternetService": InternetService, 
        "TechSupport": TechSupport, 
        "MonthlyCharges":MonthlyCharges}
    df_sample = pd.DataFrame.from_dict([my_dict])
    return df_sample

df = single_customer()

st.table(df)



