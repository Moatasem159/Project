
def railfence_encryption(plain_text, rails):
    # Create empty rails
    fence = [[] for _ in range(rails)]
    # Direction of movement (down or up)
    down = False
    row = 0

    for char in plain_text:
        fence[row].append(char)
        # Change direction if we reach the top or bottom rail
        if row == 0 or row == rails - 1:
            down = not down
        # Move to the next rail
        row += 1 if down else -1

    # Concatenate all the rails
    cipher_text = ''.join([''.join(rail) for rail in fence])
    return cipher_text




def railfence_decryption(cipher_text, rails):
    # Create empty rails
    fence = [[] for _ in range(rails)]
    # Direction of movement (down or up)
    down = None
    row = 0

    for char in cipher_text:
        # If we reach the top or bottom rail, change direction
        if row == 0:
            down = True
        elif row == rails - 1:
            down = False
        fence[row].append(None)  # Placeholder for characters

        # Move to the next rail
        row += 1 if down else -1

    # Fill in the rails with characters from the cipher text
    idx = 0
    for rail in range(rails):
        for col in range(len(fence[rail])):
            fence[rail][col] = cipher_text[idx]
            idx += 1

    # Reconstruct the message
    plain_text = ''
    row = 0
    for _ in range(len(cipher_text)):
        plain_text += fence[row].pop(0)
        # Change direction if we reach the top or bottom rail
        if row == 0:
            down = True
        elif row == rails - 1:
            down = False
        row += 1 if down else -1

    return plain_text