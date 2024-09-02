import streamlit as st

# Title of the app
st.title("Basic Streamlit App")

# Input text box for user's name
name = st.text_input("Enter your name:")

# Input number box for user's age
age = st.number_input("Enter your age:", min_value=0, max_value=120)

# Button to trigger the action
if st.button("Submit"):
    if name and age:
        st.write(f"Hello, {name}! You are {age} years old.")
    else:
        st.write("Please enter both your name and age.")

# Footer
st.write("Thank you for using the app!")