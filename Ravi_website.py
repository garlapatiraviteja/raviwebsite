
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
    with st.expander("Synonyms_antonyms "):
        st.write(''' 
                   - I started by importing the necessary NLTK libraries which are from python and data, such as the wordnet corpus, which contained synsets (sets of synonyms) and antonyms for English words.
                   
                   - I also defined a function that took a word as input and returned a list of its synonyms and antonyms. 

                   - To generate synonyms for a given word, I used the synsets() function from the wordnet corpus, which returned a list of synsets for a given word. From each synset, I extracted the lemmas, which were the different forms of the word in the synset, including synonyms. 
                  
                   - I then extracted the names of the lemmas and removed the original word from the list to avoid duplicates.  This gave me a list of synonyms for the given word.
                  
                   - To generate antonyms, I used a similar approach, but instead of extracting the lemmas' names, I extracted their antonyms using the antonyms() function from the synset. This gave me a list of antonyms for the given word. 
                  
                    - Once the synonyms and antonyms had been generated, I returned them as a dictionary or list, depending on the desired output format. 
                  
                  - I could also add additional features to the function, such as the ability to handle multiple words or handle cases where no synonyms or antonyms were found.
                    
                   
            Overall, this project demonstrated the power and flexibility of NLTK for natural language processing tasks such as generating synonyms and antonyms for English words, and was a great example of how to leverage NLTK's powerful corpus and functionality for real-world applications. When we give any word to by using the word net module which consists of synsets and lemas in the NLTK . it'll generated for synonyms and antonyms and will give us the synonyms and antonyms for a word .

               ''')
        
    with st.expander(" Virtual AI Painter "):
        st.write(''' 
                - To create a virtual painter that can draw anything using our figures, I started by importing the necessary libraries, such as cv2 and cvzone, which is a Python library
        for computer vision applications. 

                -  I then created a function that took an image of a Hand as input and returned the coordinates of the tip of the index finger and the middle finger.

                -   Next, I created a loop that continuously captured frames from the webcam and displayed them on the screen. 

                - Within the loop, I used the previously defined function to track the position of the user's fingers in real-time. 

                - I then created a canvas or a white image where the virtual painter would draw. I defined the thicknessand color of the brush, which was used to draw on the canvas. Using the position of
        the user's fingers, I determined the movement of the brush on the canvas. 

                - For example, if the index finger moved up, the brush moved up on the canvas. If the middle finger was lifted, the brush was lifted off the canvas. I also added functionality
        for changing the color of the brush and clearing the canvas. 

                -   Finally, I added a feature for saving the image that the virtual painter created, allowing users to save their artwork to their computer. Overall, this project demonstrated the power and potential
        of computer vision applications in Python and was a fun and interactive way for users to create art using their own finger ''')

    with st.expander("Mouse Detector  "):
        st.write(''' 
                                    
                    -    To create a virtual mouse that allows users to move the cursor using their hands, I  started by importing the necessary libraries, such as cv2 and mediapipe, which is a
                    Python library for building real-time computer vision applications. 

                    - I then created a  function that took an image of a hand as input and returned the coordinates of the tip  of the index finger. Next, I created a loop that continuously captured frames from the
                    webcam and displayed them on the screen. 

                    - Within the loop, I used the previously   defined function to track the position of the user's index finger in real-time. Using the position of the user's index finger, I determined the movement of the mouse cursor on
                    the screen. 

                    - For example, if the index finger moved up, the cursor moved up on the   screen. If the index finger moved to the right, the cursor moved to the right on the
            screen. I also added functionality for clicking and dragging the mouse cursor, which  allowed users to interact with the computer as if they were using a physical mouse.
                    - Finally, I added a feature for controlling the scrolling of the screen, allowing users to  scroll up and down by moving their finger up and down.
                     
                    
                Overall, this project   demonstrated the power and potential of computer vision applications in Python and  was a fun and interactive way for users to control their computer using their hands
                                ''')
    st.write("---")

    st.subheader("Side projects : ")
    with st.expander("  Autonomous Vehicle technology "):
        st.write(''' 

       -   Developed a prototype of an autonomous vehicle that can navigate on its own to a specific destination, while avoiding obstacles and adhering to traffic laws. This is an impressive feat
           that requires a range of skills and technologies.
            - I used Python as the programming language for the project, which is a popular language for machine learning and artificial intelligence applications. I also used deep neural networks and machine learning algorithms, specifically
            Tensorflow, to process images from Google Maps API, which allowed the vehicle to make decisions about where to go and how to avoid obstacles. 
            - To train the neural network, you first collected a massive amount of data by driving carefully in GTA V, a popular video game that provides a realistic simulation of driving. Once I had collected 2 terabytes of data, you
            sorted and labelled it before training the neural network provided by Nvidia. 

            - In addition to machine learning, I used OpenCV for computer vision, which helped the vehicle to detect objects in its environment. I used embedded systems and robotics technologies to integrate
            hardware components and software systems, allowing the vehicle to operate autonomously.

    - Overall, the project demonstrates how machine learning and artificial intelligence can be applied to create autonomous vehicles that can navigate safely and efficiently on their own.
    Successfully delivered a toy car capable of navigating itself in the real world .
        
         ''')
        
    with st.expander("What's up chat bot "):
        st.write('''

         -  I developed a machine learning project that uses Microsoft RNN to learn English language patterns from Reddit data, and an automation script that allows me to read
and respond to messages on WhatsApp Web using Selenium. 
        - My project is a great  example of the power of machine learning and automation in streamlining tasks and Improving user experience. 
        - By training my project on Reddit data using Microsoft  RNN, I was able to teach it to understand the nuances of English language patterns
and respond accurately to natural language queries. 
      - With the automation script I developed using Python and Selenium, my project can read and respond to messages on WhatsApp Web, making it an efficient and convenient tool for
managing messages and tasks on the messaging platform.
    - The automation script allows my project to navigate the WhatsApp Web interface and process incoming messages, providing accurate responses based on the learned language patterns.

             - Overall, my project demonstrates the potential of machine learning and automation to simplify tasks and improve user experience, and shows the importance of continually exploring and developing new technologies and tools to make our lives easier and more efficient. I'm proud of the work I've done on this project! It's just like a what's up bot which we can interact like humans
                '''

        )
                 
                


    

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
                            Hi there, my name is Raviteja Garlapati. I am a programmer and python developer with a passion for cutting-edge technology. Over the years, I have developed a diverse set of skills,
                including expertise in robotics, python, and autonomous vehicle technology. I believe that technology has the power to change the world for the better, and I am dedicated to using my
                skills to make a positive impact in society. My work in python development has taught me the  importance of creativity, collaboration, and perseverance. As a programmer, I strive to create
                code that is efficient, elegant, and user-friendly. I believe that good programming is not just about writing code, but also about problem solving and communication. My interest in
                robotics and autonomous vehicle technology has led me to explore the cutting edge of automation and machine learning. I am excited about the possibilities of these technologies,
                and I am eager to continue learning and pushing the boundaries of what is possible. Overall, I am a driven and curious individual who is passionate about technology and its potential to
                make the world a better place. I am always seeking new challenges and opportunities to learn and grow, and I look forward to what the future holds.

            '''
        )    


    with st.container():
        st.write("---")
        st.subheader("Work  - Experince  ")
        st.markdown(
            '''
             As a Python developer, could use the modules OpenCV, NLTK, NumPy, and Pandas for machine learning tasks:

            - OpenCV: I could use OpenCV for computer vision tasks such as object recognition or face detection. For example, I could train a machine learning model to recognize different objects or faces using OpenCV's image processing functions and then use that model to make predictions on new images.

            - NLTK: I could use NLTK for natural language processing tasks such as sentiment analysis or text classification. For example, I could use NLTK to preprocess and tokenize text data, then train a machine learning model to classify the text into different categories (e.g., positive/negative sentiment or different topics).

            - NumPy: I could use NumPy for numerical computing and handling large arrays or matrices. For machine learning tasks, I might use NumPy to preprocess data, normalize feature values, or perform linear algebra operations needed for machine learning algorithms.

            - Pandas: I could use Pandas for data manipulation and analysis, particularly for working with tabular data. I could use Pandas to clean and preprocess data, perform feature engineering (e.g., creating new features from existing ones), or analyze data to identify patterns and relationships that might be useful for machine learning models.

            Overall, as a Python developer, I can use these modules in various ways to preprocess data, extract features, and train machine learning models for a wide range of applications.

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


