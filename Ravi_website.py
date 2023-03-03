
import streamlit as st

 
# https://www.webfx.com/tools/emoji-cheat-sheet/ -- emojis list

st.set_page_config(page_title="Raviteja",page_icon=":smile:")

#Hidding the style

hide_st_style ="""

 <style>
 #MainMenu {visibility:hidden;}
 footer {visibility:hidden;}
 </style>

"""
st.markdown(hide_st_style,unsafe_allow_html=True)

##adding background

st.markdown("""
    <style>
        .stApp {
        background: url("https://pps.whatsapp.net/v/t61.24694-24/319779783_525119986270612_1445455221244685298_n.jpg?ccb=11-4&oh=01_AdQ6ozlqURkzyWp0bPqGLaEqdFRuUKERW4FHuBI8Nv1hxg&oe=64096E68");
        background-size: cover;
        }
    </style>""", unsafe_allow_html=True)



def Projects ():
    st.markdown("# Projects 👨🏻‍💻") # copied emojies from net {https://getemoji.com/}
    with st.expander("Project 1"):
        st.write("Project 1 description")
        
    with st.expander("Project 2"):
        st.write("Project 2 description")

    st.write("---")
    with st.expander("Project 1"):
        st.write("Project 1 description")
        
    with st.expander("Project 2"):
        st.write("Project 2 description")


    

def contact():
    st.markdown("# Contact 📱")
    with st.expander("Phone"):
        st.markdown("- +91 - 8331835351")
        st.markdown("- +91 - 8919453489")

    
    st.write("---")    

    with st.expander("Email"):
        st.markdown("- garlapatiravitejag.grr@outlook.com")
        st.markdown("- garlapatiravitejag.gr1997@outlook.com")    

    
    


def main_page():

    st.header("Hi , I'm Raviteja Garlapati :smiley: :")
    st.title("Python Developer ")
    st.caption("To obtain a challening position as a Python develeoper in a dynamic and innovative company where I can utilize my skills and knowledge to contribte to the company's growth and sucess")
    # st.write("[Learnmore](Profilesummary)") # need to add some thing
        


    ## What I can do ? ......

    with st.container():
        st.write("---")
        st.subheader("Profile summary")
        st.write(
            '''
            - Over 3 years of experience as a Python Developer with a strong foundation in computer science and software engineering principles.
            - Proficient in developing and maintaining complex web applications using Python, and related technologies.
            - Experienced in working with data processing libraries like NumPy, Pandas , Open CV and other related things
            - Having ample of amount of knowledge in machine learning algorithms like open ai , Dalle-E which are basically build using the TF and web scrappy
            - Strong problem-solving skills and ability to work independently as well as in a team environment
            - I'm CEH (Certified for Ethical Hacker) holder also
            - Have knowledge based on cloud related things also like SCCM , Exchange Online
            '''
        )    


    with st.container():
        st.write("---")
        st.subheader("Work Experience")
        st.markdown(
            '''
            - Developed and maintained complex web applications using Python,..
            - Worked with data processing libraries like NumPy, Pandas, and open cv to analyze and manipulate large no of datasets
            - Created some cool stuff which related to web scrapy and NLTK by using python
            - Worked with the database team to optimize database performance and implement data security measures.
            - Tried to analyze the data for excel using the pandas and check the things by using the graphs(matplot lib)
            - Sample example in that we used to generate the automatically synonyms and antonyms by using NLTK module in python . and also 
                knowledge on Scrapy by using we used to grab the info from the net and store in excel by using python.
            - Created a AI based flappy BIRD by using matplotlib and pygame modules

            '''
        )   

       


page_names_to_funcs = {
    "Main": main_page,
    "Projects": Projects,
    "Contact": contact,
}

with st.sidebar: 
    st.image('https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png')
    st.info('Garlapati Raviteja')
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


