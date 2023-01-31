def caesar_encrypt(word, shift):
    encrypted_word = ""
    for letter in word:
        if letter.isalpha():
            num = ord(letter)
            num += shift

            if letter.isupper():
                if num > ord('Z'):
                    num -= 26 # Return to the beginning of the alphabet
                elif num < ord('A'):
                    num += 26 # Return to the end of the alphabet

            elif letter.islower():
                if num > ord('z'):
                    num -= 26 # Return to the beginning of the alphabet
                elif num < ord('a'):
                    num += 26 # Return to the end of the alphabet

            encrypted_word += chr(num)

        else:  #For characters that are not characters, the encrypted_word action isNo.
            encrypted_word += letter

    return encrypted_word

print(caesar_encrypt("Python", 3))