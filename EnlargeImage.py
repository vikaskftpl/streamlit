#https://idealo.github.io/image-super-resolution/
#streamlit cache clear
#pip install streamlit --upgrade

import numpy as np
# git clone https://github.com/idealo/image-super-resolution
# cd image-super-resolution
# python setup.py install
pip install ISR
pip install 'h5py==2.10.0' --force-reinstall

from ISR.models import RDN
import numpy as np
from PIL import Image
#pip install tensorflow
#pip install ISR
from googletrans import Translator
import easyocr
reader = easyocr.Reader(['en']) #IMP 'hi'
translator = Translator()
import pandas as pd



import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import streamlit as st
import PIL
from PIL import Image
import pandas as pd
st.title('Enlarge an Image file')
try:
	image_file_tmp = st.file_uploader(' ')
except FileNotFoundError:
	st.error('Upload an image file (only) of less than 200 MB')

if image_file_tmp is not None:
	image_file =Image.open(image_file_tmp,mode = 'r')
	lr_img = np.array(image_file)
	rdn = RDN(weights='psnr-small')
	sr_img = rdn.predict(lr_img)
	Image.fromarray(sr_img)
	st.image(sr_img, caption='Enlarged Image',width=None)
	#text_list = reader.readtext(image_file,add_margin = 0.55,width_ths=0.7, link_threshold=0.8,decoder='beamsearch', blocklist='=-',detail = 0 )
	#text_comb =' '.join(text_list)
	#st.write('', str(text_comb))#for streamlit
	#st.download_button('Download Text', text_comb)
	#st.download_button('Download Image',data = sr_img,file_name='Enlarged Image')#,mime="image/png"
	
else:
	pass
