import streamlit as st

import PIL
from PIL import Image
from googletrans import Translator

import easyocr
reader = easyocr.Reader(['en']) #IMP 'hi'
translator = Translator()

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

st.title('OCR')

def load_image(image_file):
	img = Image.open(image_file,mode = 'r')
	return img


if image_file is not None:
	im = PIL.Image.open(image_file)
    	bounds = reader.readtext(image_file,add_margin = 0.1,width_ths=0.5, link_threshold=0.4,decoder='beamsearch', blocklist='=-' )
	text_list = reader.readtext(image_file,add_margin = 0.55,width_ths=0.7, link_threshold=0.8,decoder='beamsearch', blocklist='=-',detail = 0 )
	#print(text_list)

    	text_comb =' '.join(text_list) #changed into a single line
	#print(text_comb)
    	text_comb
else:
	pass
