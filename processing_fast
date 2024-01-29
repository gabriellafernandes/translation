# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:31:11 2024

@author: gabri
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:34:59 2024

@author: gabriella
"""
import nltk
import spacy
import re
import pandas as pd
from w3lib.html import remove_tags
import unicodedata
import os

nltk.download('stopwords')
from nltk.corpus import stopwords
nlp = spacy.load('en_core_web_sm')


def remove_space_before_punctuation(input_string):
    result = re.sub(r'\s*([.,;!?])\s*', r'\1', input_string)
    return result


def remove_vowels(word):
    vowels = "aeiouAEIOU"
    return "".join([char for char in word if char not in vowels])


def normalize(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')
    s = remove_tags(s)
    s = s.lower()
    return s

def remove_stopwords(s):
    removal_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    edit_string_as_list = s.split()
    final_list = ' '.join([word for word in edit_string_as_list if word not in removal_list])
    return final_list


def process_text(sentence_original, compressed):
    sentences = normalize(sentence_original)
    sentences = sentences.strip().split('\n')
    sentences_transmit = []
    if (compressed == True):    
        for i in range(len(sentences)):
            if len(sentences[i]) > 0:
              sentences_transmit.append(remove_stopwords(sentences[i]))
              sentences_transmit[-1] = remove_space_before_punctuation(sentences_transmit[-1])
              sentences_transmit[-1] = remove_vowels(sentences_transmit[-1])
        return sentences_transmit
    
    else:
        for i in range(len(sentences)):
            if len(sentences[i]) > 0:
              sentences_transmit.append(sentences[i]) 
              sentences_transmit[-1] = remove_space_before_punctuation(sentences_transmit[-1])
        return sentences_transmit
                                                  

sentence = "Sarah is in her car, driving through morning traffic to reach her office. She works at a marketing firm, and her days are usually busy. Her work involves analyzing data, creating marketing strategies, and coordinating teams. Her mornings are often filled with meetings and brainstorm sessions."
print(process_text(sentence, True))
print(process_text(sentence, False))

path = r"C:\Users\gabri\OneDrive - Universidade do Porto\Desktop\en"
files = [f for f in os.listdir(path) if f.endswith('.txt')]

df = pd.DataFrame(columns = ['original', 'processed'])

for ind in range(1):
    file_path = os.path.join(path, files[ind])
    with open(file_path, 'r', encoding='utf-8') as file:
      data = file.read()
    # data = re.sub(r'\d+\.\d+', replace_dot_with_comma, data)
    # data = data.replace(".", ". ")
    df.loc[ind, 'original'] = process_text(data, False)
    df.loc[ind, 'processed'] = process_text(data, True)
    # print(len(df.loc[ind, 'original']))
    # print(len(df.loc[ind, 'processed']))


df.to_csv("processed_translation", encoding='utf-8', index=False)
compression = 100 * (1 - sum(len(i) for i in df.loc[ind, 'processed']) / 
                      sum(len(i) for i in df.loc[ind, 'original']))
compression

# dataset = pd.read_csv('e1.txt', error_bad_lines=False, engine="python")

# print(dataset.head())
# dataset_hf = Dataset.from_pandas(dataset)
# train_test = dataset_hf.train_test_split(test_size=0.3)

# valid_test = train_test['test'].train_test_split(test_size=0.5)

# train_valid_test_dataset = DatasetDict({
#     'train': train_test['train'],
#     'validation': valid_test['train'],
#     'test': valid_test['test']
# })
