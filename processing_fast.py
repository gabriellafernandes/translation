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
import re
import pandas as pd
from w3lib.html import remove_tags
from unidecode import unidecode
import os


def remove_space_before_punctuation(input_string):
    result = re.sub(r'\s*([.,;!?])\s*', r'\1', input_string)
    return result


def remove_vowels(word):
    vowels = "aeiouAEIOU"
    return "".join([char for char in word if char not in vowels])


def normalize(s):
    s = s.lower()
    s = ''.join(unidecode(s))
    s = remove_tags(s)
    return s

def remove_stopwords(s):
    removal_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    edit_string_as_list = s.split()
    final_list = ' '.join([word for word in edit_string_as_list if word not in removal_list])
    return final_list


def process_text(sentence_original): 
    sentence_transmit = remove_stopwords(sentence_original)
    sentence_transmit = remove_space_before_punctuation(sentence_transmit)
    sentence_transmit = remove_vowels(sentence_transmit)
    return sentence_transmit
                                                  

sentence = "Sarah is in her car, driving through morning traffic to reach her office. She works at a marketing firm, and her days are usually busy. Her work involves analyzing data, creating marketing strategies, and coordinating teams. Her mornings are often filled with meetings and brainstorm sessions."
sentence = normalize(sentence)
print("initial normalization: ", sentence)
print("processed text: ", process_text(sentence))

path = r"C:\Users\gabri\OneDrive - Universidade do Porto\Desktop\en"
files = [f for f in os.listdir(path) if f.endswith('.txt')]

df = pd.DataFrame(columns = ['original', 'processed'])
sum_compressed = 0
sum_original = 0

count = 0
for ind in range(50):
    file_path = os.path.join(path, files[ind])
    with open(file_path, 'r', encoding='utf-8') as file:
      data = file.read()
    data = normalize(data)
    data = data.strip().split('\n')
    print(ind)
    for d in range(len(data)):
        if len(data[d]) > 0:
            df.loc[count, 'original'] = data[d]
            sum_original += len(data[d])
            df.loc[count, 'processed'] = process_text(data[d])
            sum_compressed += len(df.loc[count, 'processed'])
            count += 1

df.to_csv("processed_translation.csv", encoding='utf-8', index=False)
    
compression = 100 * (1 - sum_compressed / sum_original)
compression
