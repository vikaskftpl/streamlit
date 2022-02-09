# -*- coding: utf-8 -*-

#streamlit cache clear
#pip install streamlit --upgrade
#pip install googletrans
#pip install googletrans==3.1.0a0
#pip install PIL
#pip install easyocr
#pip uninstall opencv-python-headless==4.5.5.62
#pip install opencv-python-headless==4.5.2.52
#pip install easyocr
import easyocr
import PIL
from googletrans import Translator

from PIL import ImageDraw
from googletrans import Translator

reader = easyocr.Reader(['en']) #IMP 'hi'
translator = Translator()

import streamlit as st
#@st.cache(allow_output_mutation=True, suppress_st_warning=True)
st.title('OCR_Image_to_Text')

import os
def load_image(image_file):
	img = Image.open(image_file,mode = 'r')
	return img

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])


if image_file is not None:
	# To See details
	file_details = {"filename":image_file.name, "filetype":image_file.type,
                              "filesize":image_file.size}
	st.write(file_details)
    	# To View Uploaded Image
	#st.image(load_image(image_file),width=250)


bounds = reader.readtext(image_file,add_margin = 0.1,width_ths=0.5, link_threshold=0.4,decoder='beamsearch', blocklist='=-' )

def draw_boxes(image,bounds,color= 'yellow',width =2):
	draw = ImageDraw.Draw(image)
	for bound in bounds:
		p0,p1,p2,p3=bound[0]
        	draw.line([*p0,*p1,*p2,*p3,*p0], fill = color, width = width)
    	return image

#draw_boxes(im, bounds)
text_list = reader.readtext(image_file,add_margin = 0.55,width_ths=0.7, link_threshold=0.8,decoder='beamsearch', blocklist='=-',detail = 0 )
text_comb =' '.join(text_list) #changed into a single line
text_comb

else: pass
