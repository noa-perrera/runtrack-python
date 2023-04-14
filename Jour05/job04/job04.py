def message_coder(message, shift):
    result = ''
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            result += shifted_char.upper() if char.isupper() else shifted_char
        else:
            result += char
    return result

print(message_coder("Je suis noa !",3))