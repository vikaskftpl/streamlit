#!pip install playsound  
#!pip install pyttsx3  
#!pip install gTTS
import gtts  

import streamlit as st
from playsound import playsound 

st.title('Listen the ENTIRE text')


#from google.colab import drive
#drive.mount('/content/drive')
#%cd "/content/drive/My Drive/Colab Notebooks/Projects/NLP_ALLTextProcessing/"
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)

st.write("This Web App is to help listening the text")
if st.button('Text to SPEECH'):#for streamlit
    if text == '':
        #for streamlit
        st.write('Please enter Hindi text for translation') #for streamlit
    else:
        
        #with open('text', 'r') as file:
        data = text.replace('\n', '')
        
        fhand = data.replace("\ufeff", "")
        fhand[0:100]
        t1 = gtts.gTTS(fhand,lang = 'hi')
        # save the audio file
        #t1.save("welcome.mp3") 
        #from IPython.display import Audio
        #Audio('welcome.mp3')
        
        
        from gtts import gTTS
        from tempfile import TemporaryFile
        #tts = gTTS(text='Hello', lang='en')
        f = TemporaryFile()
        t1.write_to_fp(f)
        #Play f
        #f.close()


        
        audio_file = open(f)
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format=‘audio/ogg’)       
        f.close()
      
else: pass
