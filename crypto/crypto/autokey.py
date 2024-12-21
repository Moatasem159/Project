def autokey_encryption(plain_text, key):
    key = key.upper()
    cipher_text = ''
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            if char.islower():
                offset = ord('a')
            else:
                offset = ord('A')

            key_char = key[key_index]
            key_index += 1

            key_value = (ord(key_char) - offset) % 26
            new_char = chr(((ord(char) - offset + key_value) % 26) + offset)
            cipher_text += new_char

            key += new_char.upper()  # Append the new character to the key
        else:
            cipher_text += char
    return cipher_text

def autokey_decryption(cipher_text, key):
    key = key.upper()
    plain_text = ''
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            if char.islower():
                offset = ord('a')
            else:
                offset = ord('A')

            key_char = key[key_index]
            key_index += 1

            key_value = (ord(key_char) - offset) % 26
            new_char = chr(((ord(char) - offset - key_value) % 26) + offset)
            plain_text += new_char

            key += char.upper()  # Append the current cipher character to the key for decryption
        else:
            plain_text += char
    return plain_text

# Example usage
'''plain_text = "Hello"
key = "key"

cipher_text = autokey_encrypt(plain_text, key)
print("Cipher Text:", cipher_text)

decrypted_text = autokey_decrypt(cipher_text, key)
print("Decrypted Text:", decrypted_text)'''