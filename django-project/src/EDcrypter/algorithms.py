
def caesarCipherE(text, key):
    result = ""
    
    for char in text:
        if char.isupper():
            shifted = (ord(char) - 65 + key) % 26 + 65
            result += chr(shifted)
        elif char.islower():
            shifted = (ord(char) - 97 + key) % 26 + 97
            result += chr(shifted)
        elif char.isdigit():
            shifted = (int(char) + key) % 10
            result += str(shifted)
        else:
            pass
    
    return result

def caesarCipherD(text, key):
    result = ""

    for char in text:
        if char.isupper():
            shifted = (ord(char) - 65 - key) % 26 + 65
            result += chr(shifted)
        elif char.islower():
            shifted = (ord(char) - 97 - key) % 26 + 97
            result += chr(shifted)
        elif char.isdigit():
            shifted = (int(char) - key) % 10
            result += str(shifted)
        else:
            pass

    return result

def atBashE(text):
    encipheredtext = ""
    for letter in text:
        if letter.isalpha():
            if letter.islower():
                encipheredtext += chr(219 - ord(letter))
            else:
                encipheredtext += chr(155 - ord(letter))
        else:
            encipheredtext += letter
    return encipheredtext

def atBashD(text):
    decipheredtext = ""
    for letter in text:
        if letter.isalpha():
            if letter.islower():
                decipheredtext += chr(219 - ord(letter))
            else:
                decipheredtext += chr(155 - ord(letter))
        else:
            decipheredtext += letter
    return decipheredtext

def vigenereE(text, key):
    encipheredtext = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0
    for letter in text:
        if letter.isalpha() or letter.isdigit():
            if letter.islower():
                letter_value = ord(letter) - 97
                key_value = ord(key[key_index % key_length]) - 65
                encipheredtext += chr(((letter_value + key_value) % 26) + 97)
            elif letter.isupper():
                letter_value = ord(letter) - 65
                key_value = ord(key[key_index % key_length]) - 65
                encipheredtext += chr(((letter_value + key_value) % 26) + 65)
            else:
                letter_value = int(letter)
                key_value = ord(key[key_index % key_length]) - 65
                encipheredtext += str((letter_value + key_value) % 10)
            key_index += 1
        else:
            encipheredtext += letter
    return encipheredtext

def vigenereD(text, key):
    decipheredtext = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0
    for letter in text:
        if letter.isalpha() or letter.isdigit():
            if letter.islower():
                letter_value = ord(letter) - 97
                key_value = ord(key[key_index % key_length]) - 65
                decipheredtext += chr(((letter_value - key_value) % 26) + 97)
            elif letter.isupper():
                letter_value = ord(letter) - 65
                key_value = ord(key[key_index % key_length]) - 65
                decipheredtext += chr(((letter_value - key_value) % 26) + 65)
            else:
                letter_value = int(letter)
                key_value = ord(key[key_index % key_length]) - 65
                decipheredtext += str((letter_value - key_value) % 10)
            key_index += 1
        else:
            decipheredtext += letter
    return decipheredtext

def beaufortE(text, key):
    ##text = text.upper()
    ##key = key.upper()
    encipheredText = ""
    for i in range(len(text)):
        char = text[i]
        key_char = key[i % len(key)]
        if char.isalpha():
            shift = ord(key_char) - ord(char.upper())
            encipheredChar = chr((shift % 26) + ord('A'))
            if char.islower():
                encipheredChar = encipheredChar.lower()
            encipheredText += encipheredChar
        elif char.isdigit():
            shift = ord(key_char) - ord('0')
            encipheredText += str((shift % 10 + ord(char) - ord('0')) % 10)
        else:
            encipheredText += char
    return encipheredText

def beaufortD(text, key):
    ##text = text.upper()
    ##key = key.upper()
    decipheredText = ""
    for i in range(len(text)):
        char = text[i]
        key_char = key[i % len(key)]
        if char.isalpha():
            shift = ord(key_char) - ord('A')
            decipheredChar = chr((ord('A') + shift - ord(char.upper())) % 26 + ord('A'))
            if char.islower():
                decipheredChar = decipheredChar.lower()
            decipheredText += decipheredChar
        elif char.isdigit():
            shift = ord(key_char) - ord('0')
            decipheredText += str((ord('0') + 10 + ord(char) - shift - ord('0')) % 10)
        else:
            decipheredText += char
    return decipheredText

def railFenceE(text, key):
    fence = [['\n' for i in range(len(text))] for j in range(key)]
    
    dirDown = False
    row = 0
    col = 0
    for char in text:
        if row == 0 or row == key-1:
            dirDown = not dirDown
        fence[row][col] = char
        col += 1
        if dirDown:
            row += 1
        else:
            row -= 1
    
    encipheredtext = ""
    for i in range(key):
        for j in range(len(text)):
            if fence[i][j] != '\n':
                encipheredtext += fence[i][j]
    
    return encipheredtext


def railFenceD(text, key):
    fence = [['\n' for i in range(len(text))] for j in range(key)]
    
    dirDown = False
    row = 0
    col = 0
    for char in text:
        if row == 0 or row == key-1:
            dirDown = not dirDown
        fence[row][col] = '*'
        col += 1
        if dirDown:
            row += 1
        else:
            row -= 1
    
    index = 0
    for i in range(key):
        for j in range(len(text)):
            if fence[i][j] == '*' and index < len(text):
                fence[i][j] = text[index]
                index += 1
    
    decipheredtext = ""
    dirDown = False
    row = 0
    col = 0
    for i in range(len(text)):
        if row == 0 or row == key-1:
            dirDown = not dirDown
        if fence[row][col] != '*':
            decipheredtext += fence[row][col]
            col += 1
        if dirDown:
            row += 1
        else:
            row -= 1
    
    return decipheredtext

def gronsfeldE(text, key):
    keyLen = len(key)
    encipheredtext = ''
    for i, char in enumerate(text):
        keyValue = int(key[i % keyLen], 36) - 10
        if char.isupper():
            charValue = ord(char) - ord('A')
            encipheredCharValue = (charValue + keyValue) % 26
            encipheredChar = chr(encipheredCharValue + ord('A'))
        elif char.islower():
            charValue = ord(char) - ord('a')
            encipheredCharValue = (charValue + keyValue) % 26
            encipheredChar = chr(encipheredCharValue + ord('a'))
        elif char.isdigit():
            charValue = ord(char) - ord('0')
            encipheredCharValue = (charValue + keyValue) % 10
            encipheredChar = chr(encipheredCharValue + ord('0'))
        else:
            encipheredChar = char
        encipheredtext += encipheredChar
    return encipheredtext

def gronsfeldD(text, key):
    keyLen = len(key)
    decipheredtext = ''
    for i, char in enumerate(text):
        keyValue = int(key[i % keyLen], 36) - 10
        if char.isupper():
            charValue = ord(char) - ord('A')
            decipheredCharValue = (charValue - keyValue) % 26
            decipheredChar = chr(decipheredCharValue + ord('A'))
        elif char.islower():
            charValue = ord(char) - ord('a')
            decipheredCharValue = (charValue - keyValue) % 26
            decipheredChar = chr(decipheredCharValue + ord('a'))
        elif char.isdigit():
            charValue = ord(char) - ord('0')
            decipheredCharValue = (charValue - keyValue) % 10
            decipheredChar = chr(decipheredCharValue + ord('0'))
        else:
            decipheredChar = char
        decipheredtext += decipheredChar
    return decipheredtext
