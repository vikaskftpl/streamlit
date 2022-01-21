#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import streamlit as st #for streamlit

#@st.cache(allow_output_mutation=True, suppress_st_warning=True)#for streamlit
# def download_model():
#     model_name = "facebook/mbart-large-50-many-to-many-mmt"
#     model = MBartForConditionalGeneration.from_pretrained(model_name)
#     tokenizer = MBart50Tokenizer.from_pretrained(model_name)
#     return model, tokenizer


from nltk.tokenize import word_tokenize
import nltk
#nltk.download('punkt')

from nltk.corpus import stopwords
stopwordlist = list(stopwords.words('english'))

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

import en_core_web_sm
nlp = en_core_web_sm.load()
# nltk.download('stopwords')

stopwords = list(STOP_WORDS)
stopwords = stopwordlist.extend (['(',')','-',':',',',"'s",'!',':',"'","''",'--','.',':','?',';''[',']','``','o','’','“','”','”','[',';'])

nlp = spacy.load('en_core_web_sm')

from heapq import nlargest

st.title('Text Summary')#for streamlit
text1 = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)
text = text1.replace("\ufeff", "")

#model, tokenizer = download_model()#for streamlit

if st.button('Get Summary'):#for streamlit
    if text == '':#for streamlit
        st.write('Please enter passage for summary') #for streamlit
    else: 
#         model_name = "facebook/mbart-large-50-many-to-many-mmt"
#         tokenizer.src_lang = "hi_IN"
#         encoded_hindi_text = tokenizer(text, return_tensors="pt")
#         generated_tokens = model.generate(**encoded_hindi_text, forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"])
#         out = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
#         from nltk.tokenize import word_tokenize
#         import nltk
#         nltk.download('punkt')
          words = word_tokenize(text)
          #nltk.download('stopwords')
#         from nltk.corpus import stopwords
#         stopwordlist = list(stopwords.words('english'))

#         import spacy
#         from spacy.lang.en.stop_words import STOP_WORDS
#         from string import punctuation

          #stopwords = list(STOP_WORDS)
          #stopwords = stopwordlist.extend (['(',')','-',':',',',"'s",'!',':',"'","''",'--','.',':','?',';''[',']','``','o','’','“','”','”','[',';'])

          #nlp = spacy.load('en_core_web_sm')
          doc = nlp(text)

          tokens = [token.text for token in doc]

          punctuation = punctuation + '\n'
          word_frequencies = {} #making a dictionary
          for word in doc:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] =1                
                else:
                    word_frequencies[word.text] +=1 #if any word is present more than 1 time
          max_frequency = max(word_frequencies.values())
          for word in word_frequencies.keys():
                word_frequencies[word] = word_frequencies[word]/max_frequency
                sentence_tokens = [sent for sent in doc.sents]

          sentence_scores = {} #create dictionary
          for sent in sentence_tokens:
                for word in sent:
                    if word.text.lower() in word_frequencies.keys():
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word.text.lower()]
                        else:
                            sentence_scores[sent] += word_frequencies[word.text.lower()]

          #from heapq import nlargest
          select_length = int(len(sentence_tokens)*.3) #selecting only 10% of the sentences
          summary = nlargest(select_length,sentence_scores,key = sentence_scores.get)
          final_summary = [word.text for word in summary]
          summary = ' '.join(final_summary)
          #st.write('', str(summary).strip('][\''))#for streamlit
          st.write('', str(summary))#for streamlit
else: pass
