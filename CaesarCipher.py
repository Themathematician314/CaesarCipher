#The point of this series of lecture notes is to start out with absolutes of Python. This is also to limit test my brain to see how much I can recall in one hour for my Programming Challenge.
#We shall start out with a basic Caesar Cipher.

"""The Ceasar Cipher is the most basic cipher of all time. It rotates the letters by up to 25 and each value becomes encrypted by the rotated amount. The rotation is fixed which is the bad part. 
However, if we know the amount we rotated by, we can crack the ciphertext to get the plaintext back.
We can demonstrate a basic caesar cipher below."""

from pydoc import plain

def Ceasar_Cipher():

    plaintext = input("Enter any sentence you want: ")
    plaintext = plaintext.lower()
    plaintext =''.join(plaintext.split())
    sentence_list = []
    cipher_sentence_list = []

#This is the dictionary portion where we convert the text to numbers. 
    converter_dictionary = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    reconverter_dictionary = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
    
    encryption_rotation = int(input("Enter a number between 1 and 25: "))
    for letter in plaintext:
        sentence_list.append(converter_dictionary[letter])

    while encryption_rotation <= 0 or encryption_rotation >= 26:
        encryption_rotation = int(input("Enter a number between 1 and 25: "))
    if 0 < encryption_rotation < 26:
        for plaintext_converted in sentence_list:
            cipher_letter = reconverter_dictionary[(plaintext_converted + encryption_rotation) % 26]
            cipher_sentence_list.append(cipher_letter)
    for i in cipher_sentence_list:
        print(type(i))

    print(cipher_sentence_list)
    print(type(cipher_sentence_list))
    print(''.join(str(ch) for ch in cipher_sentence_list))

def Caesar_Reverse():
    
    ciphertext = input("Enter any sentence you want: ")
    ciphertext = ciphertext.lower()
    ciphertext =''.join(ciphertext.split())
    sentence_list = []
    plaintext_sentence_list = []
    plaintext = ''.join(plaintext_sentence_list)

#This is the dictionary portion.
    converter_dictionary = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    reconverter_dictionary = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

    for letter in ciphertext:
        sentence_list.append(converter_dictionary[letter])

    for decryption_rotation in range(0, 26):
        decrypted_list = []
        for ciphertext_letter in sentence_list:
            plaintext_letter = reconverter_dictionary[(ciphertext_letter + decryption_rotation) % 26]
            decrypted_list.append(plaintext_letter)
        print(''.join(str(ch) for ch in decrypted_list), "The decryption value is ", decryption_rotation, " and the encryption value is", 26 - decryption_rotation, ".")
    
def main():
    Ceasar_Cipher()
    Caesar_Reverse()

if __name__ == "__main__":
    main()
