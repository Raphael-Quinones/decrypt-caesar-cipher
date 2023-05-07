import string
import textstat
import random
import streamlit as st
from langdetect import detect
from collections import Counter


def caesar_bruteforce(ciphertext):
    for key in range(1, 26):  # Try all possible key values
        encrypted_text, _key  = caesar_encrypt(ciphertext, key) # Run caesar encryption for every value
        if is_readable(encrypted_text):
            # If text is readable, return the encrypted text and key
            return encrypted_text, key

def caesar_encrypt(ciphertext, key):
    plaintext = "" # Store plaintext for decrypted text
    for char in ciphertext: # Check every letter in the string
        if char.isalpha(): # Check if character is in alphabet
            # If character is uppercase, set ascii_offset to Unicode point of 'A', else use Unicode point of 'a'
            # This will  be useful in preserving character capitalization
            ascii_offset = ord('A') if char.isupper() else ord('a') 
            # ord(char) - ascii_offset, results to a number 0 to 25 that represents a letter in the alphabet
            # ord(char) - ascii_offset - key, shifts the character/letter
            # modulo 26 to keep the range to 0 to 25 after shifting
            # + ascii_offset to convert the letter to it's upper or lower case Unicode point equivalent
            # chr() to convert to letter
            decrypted_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            plaintext += decrypted_char # add to decrypted plaintext
        else:
            # Runs if character is not in the alphabet
            plaintext += char
    return plaintext, key

def caesar_freqanalysis(ciphertext):
    letter_frequency = Counter(ciphertext.upper()) # Counts the letter frequency of each letter. .upper() to make sure all letters are the same. 'A' is different from 'a'
    most_common = letter_frequency.most_common(1)[0][0] # Too long to explain, gets the most common letter in the text
    ascii_offset = ord('A') # Set the offset to 'A' since we used .upper()

    key = (ord(most_common) - ord('E')) % 26  # Calculate the key based on the most common letter (assuming 'E' is the most frequent in English)

    plaintext = "" # Storage for decrypted text
    for char in ciphertext: # run for every character in text
        if char.isalpha(): # Runs if in the alphabet
            # Almost same functionality as in caesar_encrypt()
            decrypted_char = chr((ord(char.upper()) - ascii_offset - key) % 26 + ascii_offset)
            # Almost same functionality as in caesar_encrypt()
            # if char.islower() else decrypted_char.lower() -- this line converts character to lowercase if original is in lowercase
            plaintext += decrypted_char if char.islower() else decrypted_char.lower()
        else:
            # Runs if character is not in the alphabet
            plaintext += char

    return plaintext, key

def is_readable(text):
    # Current Workaround
    # If text is detected as english, text is therefore decrypted
    language = detect(text)
    if language == 'en': 
        return True
    else:
        return False

def get_random_splice(text): # Used for testing a small string from the whole text
    words = text.split() # Splits the whole text into a list separated by spaces
     # A string of 6 words are to be sampled
    if len(words) <= 6: # If the whole text is less than 6 words, return the tet
        return text
    else:
        # Randomly select a number as the start_index 
        # Minus 6 to avoid splicing over the length of the whole words list
        start_index = random.randint(0, len(words) - 6)
        # end index of the splice
        end_index = start_index + 6
        return ' '.join(words[start_index:end_index])
    
def main():# Driver function
    st.title("Caesar Cipher Decryptor")
    st.write("Made by Raphael Quinones")
    st.markdown("[Source Code](https://github.com/Raphael-Quinones/decrypt-caesar-cipher)")



    encrypted_text = st.text_input("Enter the encrypted text here")
    if (encrypted_text):
        spliced_text = get_random_splice(encrypted_text) # Get sample first, before encrypting the whole text

        first_try, key = caesar_freqanalysis(spliced_text) # Try frequency analysis first before bruteforcing
        if is_readable(first_try): # If the text is 'readable' it means it's been decrypted
            print("Freqal won!")
            plaintext, key = caesar_encrypt(encrypted_text, key) # After decrypting the sample, decrypt the whole text
            st.write("Decrypted:" + plaintext)
            st.write("Key shift: " + str(key))

        else:
            print("Bruteforce won!")
            _encryptedsplice, key = caesar_bruteforce(spliced_text) # Extract just the key
            plaintext,key  = caesar_encrypt(encrypted_text, key) # After decrypting the sample, decrypt the whole text
            st.write(plaintext)
            st.write("Key shift: " + str(key))

        st.write("Refresh to decrypt another text")
    
if __name__ == "__main__":
    main()
        







        
