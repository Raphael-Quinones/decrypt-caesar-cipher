import string
import textstat
import random
from langdetect import detect
from collections import Counter


def caesar_bruteforce(ciphertext):
    for key in range(1, 26):  # Try all possible key values
        encrypted_text, _key  = caesar_encrypt(ciphertext, key)
        if is_readable(encrypted_text):
            return encrypted_text, key

def caesar_encrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext, key

def caesar_freqanalysis(ciphertext):
    letter_frequency = Counter(ciphertext.upper())
    most_common = letter_frequency.most_common(1)[0][0]
    ascii_offset = ord('A')

    key = (ord(most_common) - ord('E')) % 26  # Calculate the key based on the most common letter (assuming 'E' is the most frequent in English)

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = chr((ord(char.upper()) - ascii_offset - key) % 26 + ascii_offset)
            plaintext += decrypted_char if char.islower() else decrypted_char.lower()
        else:
            plaintext += char

    return plaintext, key

def is_readable(text):
    # Current Workaround
    # If text is detected as english, text is therefore decrypted
    language = detect(text)
    if language == 'en':  # Adjust the threshold as needed
        return True
    else:
        return False

def get_random_splice(text):
    words = text.split()
    if len(words) <= 6:
        return text
    else:
        start_index = random.randint(0, len(words) - 6)
        end_index = start_index + 6
        return ' '.join(words[start_index:end_index])
    
if __name__ == "__main__":
    encrypted_text = "Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.."
    spliced_text = get_random_splice(encrypted_text)

    first_try, key = caesar_freqanalysis(spliced_text)
    if is_readable(first_try):
        print("Freqal won!")
        plaintext = caesar_encrypt(encrypted_text, key)
        print(plaintext)
    else:
        print("Bruteforce won!")
        _encryptedsplice, key = caesar_bruteforce(spliced_text)
        plaintext = caesar_encrypt(encrypted_text, key)
        print(plaintext)
        







        
