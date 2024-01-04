import numpy as np
import math


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
    
    

# Example usage
snr_dB = 0
noise_level = snr_to_noise_level(snr_dB)

# Example usage
original_sentence = "This is a sample sentence."
noisy_sentence = add_awgn_noise(original_sentence, noise_level)

print("Original Sentence:", original_sentence)
print("Noisy Sentence:", noisy_sentence)




print(f"SNR: {snr_dB} dB")
print(f"Noise Level: {noise_level}")
