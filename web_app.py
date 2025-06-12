import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))
#creating empty spaces in each column
col0, col1, col2, col3, col4, col5, col6 = st.columns(7)
with col0:
    st.write('')
with col1:
    st.write('')
with col2:
    st.write('')    
#Display the text in a title formatting
with col3:
    st.title("ⴍage") 
with col4:
    st.write('')
with col5:
    st.write('')
with col6:
    st.write('')

col7, col8, col9 = st.columns(3)
with col7:
    st.write('')  
    #displaying the string formatted as markdown  
with col8:
    st.markdown("<h6 style='text-align: center;'>A simple web app to predict annual salary</h6>", unsafe_allow_html=True)
with col9:
    st.write('')
#defines a list of genders
gen_list = ["Female", "Male"]
#defines a list of education levels
edu_list = ["Bachelor's", "Master's", "PhD"]
#defines a list of jobs
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"]
#shows the jobs indexes
job_idx = [0, 1, 10, 11, 20]
#st.radio creates a radio button selector
#This enables the user to selct a gender according to the gen_list
gender = st.radio('Pick your gender', gen_list)
#st.slider creates a slider widget and only accepts numerical data
#enables the user to pick his age from 21 to 55 by sliding 
age = st.slider('Pick your age', 21, 55)
#st.selectbox displays a select widget
#enables the user to select an education level accrding to edu_list
education = st.selectbox('Pick your education level', edu_list)
#the user selects the job title according to job_list
job = st.selectbox('Pick your job title', job_list)
#The user picks the years of experience using the sliding widget
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")
#creating 5 columns for layout space
col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')
with col11:
    st.write('')   
#Creating the predict salary button at the 12th column 
with col12:
    predict_btn = st.button('Predict Salary')
with col13:
    st.write('')
with col14:
    st.write('')
#if the predict salary button is clicked
if(predict_btn):
    #converts the age from the slider to an integer
    inp1 = int(age)
    #converts the experience from the slider to a float
    inp2 = float(experience)
    #searches for the index of a job in the job_list
    inp3 = int(job_idx[job_list.index(job)])
    #finds the index of the education level in edu_list
    inp4 = int(edu_list.index(education))
    #finds the index of the gender in the gen_list
    inp5 = int(gen_list.index(gender))
    X = [inp1, inp2, inp3, inp4, inp5]
    #predict the salary
    salary = model.predict([X])
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('') 
        #this is where the salary will be shown   
    with col16:
        st.text(f"Estimated salary: ${int(salary[0])}")
    with col17:
        st.write('')


