#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from transformers import MBartForConditionalGeneration, MBart50Tokenizer
import streamlit as st #for streamlit

#@st.cache(allow_output_mutation=True, suppress_st_warning=True)#for streamlit
def download_model():
    model_name = "facebook/mbart-large-50-many-to-many-mmt"
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBart50Tokenizer.from_pretrained(model_name)
    return model, tokenizer

st.title('Translate to Hindi or Marathi')#for streamlit
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)
model, tokenizer = download_model()#for streamlit

if st.button('Translate to Hindi'):#for streamlit
    if text == '':#for streamlit
        st.write('Please enter English text for translation') #for streamlit
    else: 
        model_name = "facebook/mbart-large-50-many-to-many-mmt"
        tokenizer.src_lang = "en_XX"
        encoded_hindi_text = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**encoded_hindi_text, forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"])
        out = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        st.write('', str(out).strip('][\''))#for streamlit
        ###
#st.title('2. English to Marathi Translation')#for streamlit
#text = st.text_area("Enter English Text:", value='', height=None, max_chars=None, key=None)
#model, tokenizer = download_model()#for streamlit

if st.button('Translate to Marathi'):#for streamlit
    if text == '':#for streamlit
        st.write('Please enter English text for translation') #for streamlit
    else: 
        model_name = "facebook/mbart-large-50-many-to-many-mmt"
        tokenizer.src_lang = "en_XX"
        encoded_hindi_text_1 = tokenizer(text, return_tensors="pt")
        generated_tokens_1 = model.generate(**encoded_hindi_text_1, forced_bos_token_id=tokenizer.lang_code_to_id["mr_IN"])
        out = tokenizer.batch_decode(generated_tokens_1, skip_special_tokens=True)
        st.write('', str(out).strip('][\''))#for streamlit
        
else: pass
st.download_button(label="Download Text", data=text,mime="text",file_name="Translation.txt")
if st.button('Clear output'):
    st.text_area.empty()
