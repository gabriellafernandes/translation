# -*- coding: utf-8 -*-
import numpy as np
import math
import pandas as pd

def snr_to_noise_level(snr_dB):
    noise_l = math.sqrt(1 / (10 ** (snr_dB / 10)))
    return noise_l

def add_awgn_noise(sentence, noise_l):
    """
    Add AWGN noise to a sentence.

    Parameters:
    - sentence (str): The input sentence.
    - noise_level (float): The standard deviation of the Gaussian noise.

    Returns:
    - str: The sentence with added AWGN noise.
    """
    values = []
    for c in sentence: 
        values.append(ord(c))
        
    # Generate Gaussian noise
    noise = np.random.normal(0, noise_l, len(values))
    
    noisy_sentence_array = values + noise
    
    # Clip values to ensure they are valid ASCII characters
    noisy_sentence_array = np.clip(noisy_sentence_array, ord(' '), ord('~'))

    # Convert back to string
    noisy_sentence = ''.join([chr(int(value)) for value in noisy_sentence_array])

    return noisy_sentence
    
    
snr_dB = 0
noise_level = snr_to_noise_level(snr_dB)

df = pd.read_fwf("europarl-v7.de-en.txt")
df = df.dropna(axis=1)
print('a')

noise_translation = []
for i in df['Resumption of the session']:
    noise_translation.append(add_awgn_noise(i, noise_level))
    
df['Noisy'] = noise_translation

print(df)

print('a')
df.to_csv('output.csv', index=False)
