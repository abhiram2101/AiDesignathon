# app.py - Streamlit UI for the AI-based skill development application


# app.py - Streamlit UI for displaying employee profiles and skill data
#code for skill dashboard
import streamlit as st

# Streamlit UI components
st.title('Employee Skill Management System')

# Mock employee data
employees = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

# Mock skill data
skills = [
    {"employee_id": 1, "technology": "Python", "skill_level": "Intermediate", "years_of_experience": 3},
    {"employee_id": 1, "technology": "SQL", "skill_level": "Advanced", "years_of_experience": 5},
    {"employee_id": 2, "technology": "Java", "skill_level": "Intermediate", "years_of_experience": 4}
]

# Main UI section
selected_employee = st.selectbox('Select Employee:', [f'{emp["id"]} - {emp["name"]}' for emp in employees])

if selected_employee:
    employee_id = int(selected_employee.split('-')[0].strip())
    employee_data = next(emp for emp in employees if emp["id"] == employee_id)
    
    st.subheader('Employee Profile:')
    st.write(f'Name: {employee_data["name"]}')
    st.write(f'Email: {employee_data["email"]}')
    
    st.subheader('Skill Data:')
    skill_data = [skill for skill in skills if skill["employee_id"] == employee_id]
    for skill in skill_data:
        st.write(f'Technology: {skill["technology"]}')
        st.write(f'Skill Level: {skill["skill_level"]}')
        st.write(f'Years of Experience: {skill["years_of_experience"]}')
        st.write('---')






# code for skill submition and validation

import streamlit as st

# Streamlit UI components
st.title('AI Skill Development Application')

# Function to handle skill validation request
def validate_skill():
    technology = st.text_input('Enter Technology:')
    skill_level = st.selectbox('Select Skill Level:', ['Beginner', 'Intermediate', 'Advanced'])
    years_of_experience = st.number_input('Enter Years of Experience:', min_value=0, max_value=50)
    validator_id = st.text_input('Enter Validator ID:')
    
    if st.button('Submit Validation Request'):
        # Placeholder logic for skill validation
        # This function would contain the logic to process the validation request
        # For demonstration purposes, let's print the submitted data
        st.write('Skill Validation Request Submitted:')
        st.write(f'Technology: {technology}')
        st.write(f'Skill Level: {skill_level}')
        st.write(f'Years of Experience: {years_of_experience}')
        st.write(f'Validator ID: {validator_id}')
        st.success('Skill validation request submitted successfully.')

# Main UI section
st.subheader('Skill Validation:')
validate_skill()
