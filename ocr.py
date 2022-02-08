# -*- coding: utf-8 -*-

#streamlit cache clear
# !pip uninstall googletrans
#pip install googletrans
# !pip install googletrans==3.1.0a0

import streamlit as st
#@st.cache(allow_output_mutation=True, suppress_st_warning=True)

st.title('OCR_Image_to_Text')

#import PIL
#pip install PIL
from PIL import ImageDraw
from googletrans import Translator

#import easyocr
#pip install easyocr
reader = easyocr.Reader(['en']) #IMP 'hi'
translator = Translator()
    
uploaded_file  = st.file_uploader("Choose a file")
if uploaded_file is not None:
    
    bytes_data = uploaded_file.getvalue()
    open(bytes_data,mode ='r')
    #st.write(bytes_data)

    # To convert to a string based IO:
    #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #stringio = StringIO(uploaded_file.getvalue(),mode = 'r')
    
    #st.write(stringio)

    #import PIL
    #from PIL import ImageDraw
    im = PIL.Image.open(bytes_data)
    im

    # !pip uninstall opencv-python-headless==4.5.5.62

    # !pip install opencv-python-headless==4.5.2.52

    # !pip install easyocr
    #change run type to GPU
    # !pip install googletrans
    #from googletrans import Translator

#     import easyocr
#     reader = easyocr.Reader(['en']) #IMP 'hi'
#     translator = Translator()
    bounds = reader.readtext(bytes_data,add_margin = 0.1,width_ths=0.5, link_threshold=0.4,decoder='beamsearch', blocklist='=-' )
    bounds

    def draw_boxes(image,bounds,color= 'yellow',width =2):
        
        draw = ImageDraw.Draw(image)
        for bound in bounds:
            p0,p1,p2,p3=bound[0]
            draw.line([*p0,*p1,*p2,*p3,*p0], fill = color, width = width)
        return image

    # draw_boxes(im, bounds)
    text_list = reader.readtext(bytes_data,add_margin = 0.55,width_ths=0.7, link_threshold=0.8,decoder='beamsearch', blocklist='=-',detail = 0 )

    text_comb =' '.join(text_list) #changed into a single line
    text_comb

else: pass
