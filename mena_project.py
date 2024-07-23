import streamlit as st
import numpy as np
import pickle

# Load the trained model from the pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the function to get user input
def get_user_input():
    ssc_percentage = st.number_input("SSC Percentage", min_value=0.0, max_value=100.0, step=0.1)
    hsc_percentage = st.number_input("HSC Percentage", min_value=0.0, max_value=100.0, step=0.1)
    degree_percentage = st.number_input("Degree Percentage", min_value=0.0, max_value=100.0, step=0.1)
    etest_percentage = st.number_input("Etest Percentage", min_value=0.0, max_value=100.0, step=0.1)
    mba_percentage = st.number_input("MBA Percentage", min_value=0.0, max_value=100.0, step=0.1)

    hsc_subject = st.selectbox("HSC Subject", ("Arts", "Commerce", "Science"))
    gender = st.selectbox("Gender", ("Female", "Male"))
    hsc_board = st.selectbox("HSC Board", ("Central", "Others"))
    work_experience = st.selectbox("Work Experience", ("No", "Yes"))
    ssc_board = st.selectbox("SSC Board", ("Central", "Others"))
    degree = st.selectbox("Degree", ("Commerce and Management", "Science and Tech"))
    specialisation = st.selectbox("Specialisation", ("Finance", "HR"))

    # Convert categorical data to numerical values
    hsc_subject_dict = {"Arts": 0, "Commerce": 1, "Science": 2}
    gender_dict = {"Female": 0, "Male": 1}
    board_dict = {"Central": 0, "Others": 1}
    work_experience_dict = {"No": 0, "Yes": 1}
    degree_dict = {"Commerce and Management": 0, "Science and Tech": 1}
    specialisation_dict = {"Finance": 0, "HR": 1}

    hsc_subject = hsc_subject_dict[hsc_subject]
    gender = gender_dict[gender]
    hsc_board = board_dict[hsc_board]
    work_experience = work_experience_dict[work_experience]
    ssc_board = board_dict[ssc_board]
    degree = degree_dict[degree]
    specialisation = specialisation_dict[specialisation]

    # Create a numpy array of the input values
    
    user_input = np.array([[gender,ssc_percentage, ssc_board, hsc_percentage, hsc_board,
                            hsc_subject,  degree_percentage, degree, work_experience, etest_percentage,  specialisation, mba_percentage]])

    return user_input

# Streamlit app
st.title("Placement Predictor")

# Get user input
user_input = get_user_input()

# Predict using the model
if st.button("Predict"):
    prediction = model.predict(user_input)
    st.write(f"The predicted placement status is: {'Placed' if prediction == 1 else 'Not Placed'}")
    #st.write(prediction)
