#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#! pip install sentence-splitter
#! pip install transformers
#! pip install SentencePiece

#import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True, suppress_st_warning=True)

def download_model():
    model_name = 'tuner007/pegasus_paraphrase'
    #torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    #model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
    model = PegasusForConditionalGeneration.from_pretrained(model_name)
    return model, tokenizer
    
st.title('AI Reviews')
tgt_text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)
model, tokenizer = download_model()

if st.button('Click to get AI Reviews'):
    if tgt_text == '':    
        st.write('Please enter text to get AI Reviews')
    else:
        
        #batch = tokenizer.prepare_seq2seq_batch(tgt_text,truncation=True,padding='longest',max_length=60, return_tensors="pt").to(torch_device)
        batch = tokenizer.prepare_seq2seq_batch(tgt_text,truncation=True,padding='longest',max_length=60, return_tensors="pt")
        translated = model.generate(**batch,max_length=60,num_beams=10, num_return_sequences=10, temperature=1.5)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        st.write('', str(tgt_text))#for streamlit
        
        contentDF = tgt_text
        dataframeFinal = pd.DataFrame(contentDF)
        csv = dataframeFinal.to_csv(index=True)

        st.download_button(label="Download CSV", data=csv,mime="text/csv",file_name="AIReviews.csv")
        
    if st.button('Clear output'):
        st.text_area.empty()
#else: pass
        
else: pass
   
num_return_sequences = 10
num_beams = 10
