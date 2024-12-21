def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def affine_encryption(plain_text, a, b):
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                cipher_text += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            elif char.isupper():
                cipher_text += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
        else:
            cipher_text += char
    return cipher_text



import math
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  #
def count_letters_use(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():
            char = char.upper()
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts
def most_two_letters_used(text):
    letter_counts = count_letters_use(text)
    most_common_count = 0
    second_common_count = 0
    most_common_letter = ''
    second_common_letter = ''
    for letter, count in letter_counts.items():
        if count > most_common_count:
            second_common_count = most_common_count
            second_common_letter = most_common_letter
            most_common_count = count
            most_common_letter = letter
        elif count > second_common_count:
            second_common_count = count
            second_common_letter = letter
    return most_common_letter, second_common_letter

def getKey(index_L1,index_L2):
    index_L1 = ord(index_L1) - ord('A')  
    index_L2 = ord(index_L2) - ord('A')  
    for a in range(1, 26):
        if math.gcd(a, 26) == 1:
            inv_a = mod_inverse(a, 26)
            if inv_a is not None:  
                b = (index_L1 - 4 * a) % 26
                if (index_L2 - 19 * a) % 26 == b:
                    return a, b
    return None, None
def affine_decryption(cipherText, a, b):
    plainText = ''
    for ch in cipherText:
        if ch.isalpha():
            ch = ch.upper()
            inv = mod_inverse(a, 26)
            c_index = alphabet.index(ch)
            p_index = inv * (c_index - b) % 26
            p_ch = alphabet[p_index]
            plainText += p_ch
        else:
            plainText += ch
    return plainText
