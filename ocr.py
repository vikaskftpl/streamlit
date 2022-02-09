#for ocr.py
#streamlit cache clear
#pip install streamlit --upgrade
#pip install googletrans
#pip install googletrans==3.1.0a0
#pip install PIL
#pip install easyocr
#pip uninstall opencv-python-headless==4.5.5.62
#pip install opencv-python-headless==4.5.2.52
#pip install easyocr

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import streamlit as st
import PIL
from PIL import Image
from googletrans import Translator
import easyocr
reader = easyocr.Reader(['en']) #IMP 'hi'
translator = Translator()

#def load_image(image_file_tmp):
	#img = Image.open(image_file_tmp,mode = 'r')
	#return img


image_file_tmp = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
st.title('OCR NEW')

try:
	with open(os.path.join(image_file_tmp),"wb") as input:
		#image_file =Image.open(input,mode = 'r')
		image_file =Image.open(input)
except FileNotFoundError:
	st.error('File not found.')

if image_file is not None:
	#image_file =Image.open(image_file_tmp,mode = 'r')
	text_list = reader.readtext(image_file,add_margin = 0.55,width_ths=0.7, link_threshold=0.8,decoder='beamsearch', blocklist='=-',detail = 0 )
	text_comb =' '.join(text_list)
	st.write('', str(text_comb))#for streamlit
else:
	pass
