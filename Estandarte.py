import streamlit as st

def show_home():
    st.title("You have arrived")
    
    st.image("img/pic1.jpg", use_column_width=True)
    
    st.write("""
    Foolishness, Dante. Foolishness. Might control everything. And without power you can not protect anything. Let alone yourself. 
    Also, the autbiography and portfolio is in the navbar, top left.
    """)
    
def show_about():
    st.title("Greetings human!")
    
    with st.container():
        col1, col2 = st.columns([1, 2])  
        with col1:
            st.image('img/profile.jpg')  
        with col2:
            st.title("I'm Ellan Jude Estandarte")
            st.subheader("4th Year BSIT Student")
            st.write('At Cebu Institute of Technology - University.')

    st.write('---')

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Education")
            st.write("""
            - Cebu Institute of Technology - University
                - Bachelor of Science in Information Technology (Currently)
            - Siaton Science High School
                - Senior High - Science, Technology, Engineering and Mathematics (2020)
            - Siaton National High School
                - Junior High (2018)
            - Felipe Tayko Memorial School
                - Elementary (2012)       
            """)

def show_portfolio():
    st.title("Portfolio")
    
    with st.container():
        st.header("My Projects")
        col1, col2 = st.columns((1, 2))
        col3, col4 = st.columns((1, 2))
        with col1:
            st.image('img/front.jpg')
        with col2:
            st.subheader('CIMP-Frontend')
            st.write('The frontend for our Capstone. It uses React and MUI. The project is about managing assets from our school property.')
            st.markdown('[Github Repo](https://github.com/rosnuker/CIMP-Frontend)')
        with col3:
            st.image('img/back.jpg')
        with col4:
            st.subheader('CIMP-Backend')
            st.write('The backend for our Capstone. It uses Springboot.')
            st.markdown('[Github Repo](https://github.com/reeyyyxd/CIMP_Backend)')
            
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ("Home", "About Me", "Portfolio"))

if page == "Home":
    show_home()
elif page == "About Me":
    show_about()
elif page == "Portfolio":
    show_portfolio()
